import cv2
from flask import Flask, Response
import threading
import smtplib
import RPi.GPIO as GPIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders
import time

EMAIL_DELAY = 15 
last_email_time = 0

def send_email():
    try:
        fromaddr = "sender's mailid"
        toaddr = "gayathrymw@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Intruder Detected!"
        body = "An intruder has been detected in your home. See the attached image for more details. \nLink to live stream: http://192.168.198.114:5000/video_feed "
        msg.attach(MIMEText(body, 'plain'))
        binary = open("intruder.jpg", 'rb')
        payload = MIMEBase('application', 'octet-stream', Name="intruder.jpg")
        payload.set_payload((binary).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Disposition', "attachment; filename= %s" % "intruder.jpg")
        msg.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(fromaddr, "password")

        text = msg.as_string()
        session.sendmail(fromaddr, toaddr, text)
        session.quit()
        print("Email sent successfully!")
        global last_email_time
        last_email_time = time.time()
        
    except Exception as e:
        print("Failed to send email.",str(e))

def trigger_buzzer():
    #print("buzzerrrrr")
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(3)  
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Initialize GPIO and setup the buzzer pin
BUZZER_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Initialize video capture and face cascade
video_cap = cv2.VideoCapture(0)
face_capture = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def camera_loop():
    while True:
        ret, video_data = video_cap.read()
        if not ret:
            break
        col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
        faces = face_capture.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 0, 0), 5)

        if len(faces) > 0:
            if time.time() - last_email_time >= EMAIL_DELAY:
                #print("Frame shape:", video_data.shape)
                cv2.imwrite("/home/pi/Desktop/intrusion/intruder.jpg", video_data)
                trigger_buzzer()
                send_email()

        # Encode the frame in JPEG format
        ret, jpeg = cv2.imencode('.jpg', video_data)
        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    video_cap.release()
    cv2.destroyAllWindows()

app = Flask(__name__)
@app.route('/video_feed')
def video_feed():
    return Response(camera_loop(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # Start the camera capturing loop in a separate thread
    camera_thread = threading.Thread(target=camera_loop)
    camera_thread.daemon = True
    camera_thread.start()

    app.run(host='0.0.0.0', port=5000, threaded=True)
