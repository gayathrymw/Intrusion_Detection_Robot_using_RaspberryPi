# Guardzilla - Intrusion Detection Robot using RaspberryPi

Guardzilla is an autonomous robot, which detects any human faces intruding on private property. This project is a comprehensive surveillance solution that leverages a Raspberry Pi, a USB webcam, and Python to monitor an area for potential intruders.

## Project Overview
The robot uses OpenCV for real-time face detection and sends email alerts whenever an intruder is detected. These alerts include attached images of the detected faces for user verification. Furthermore, the system offers live video streaming via a Flask web server, enabling users to monitor their environment remotely.

The robot's movements can be controlled remotely through a web interface that can be accessed from a mobile device, increasing its versatility and ease of use.

This system is designed to be effective, user-friendly, and affordable, making home security more accessible for everyone.

## Features
* Real-time Face Detection: The system uses OpenCV to detect faces in real-time. Any detected faces are treated as intruders, triggering the system's alert mechanisms.

* Email Alerts: When an intruder is detected, the system sends an email alert to the user. This email includes an image of the intruder's face for verification.

* Live Video Streaming: Users can monitor their environment in real-time through the system's video stream. This stream is accessible through any web browser, enabling remote surveillance.

* Remote Control: The robot's movements can be controlled remotely through a web interface. This interface is designed to be user-friendly and can be accessed from any mobile device.

<p align="center">
  <img src="https://github.com/gayathrymw/Intrusion_Detection_Robot_using_RaspberryPi/assets/91821885/42648ef3-938e-4f4c-8078-11a59d2e27fd" alt="flowchart" width="170" height="300">
</p>

## Components Required
* Raspberry Pi (Version: 4)
* Motor Driver (Version L2981)
* Chassis or Robot body
* USB Webcam
* SD Card
* GPIO Buzzer
* Battery or Power Bank
* Jumper Wires

## Installation
1. On your Raspberry Pi, with Raspberry Pi OS, Install the Required Python Libraries and Other Dependencies.
```
pip install flask opencv-python gpiozero numpy imutils
sudo apt-get install libncurses5-dev libncursesw5-dev
```
2. Git Clone this repository
<br>Make necessary changes in the code of "integrate.py", such as the sender's email-id, password and receiver's email id to the owner's mail id.
```
git clone https://github.com/gayathrymw/Intrusion_Detection_Robot_using_RaspberryPi/
```

3. Run the application. You can run the 3 Python codes in three different terminals to access all functionalities at the same time.
```
python integrate.py
python move.py
python phonemove.py
```
4. Access the live video feed and control interface through your web browser. If your Raspberry Pi and your computer are on the same network, just navigate to ```
http://<RaspberryPi_IP>:5000/  ```
for the live video feed and ```http://<RaspberryPi_IP>:5005/ ```
for the control interface (replace <RaspberryPi_IP> with the actual IP address of your Raspberry Pi).

## Images of the Robot
<p align="center">
  <img src="https://github.com/gayathrymw/Intrusion_Detection_Robot_using_RaspberryPi/assets/91821885/cb5c1dee-b436-4b82-a6d6-eba1bab3eaac" alt="robot1" width="250" height="250">
  <img src="https://github.com/gayathrymw/Intrusion_Detection_Robot_using_RaspberryPi/assets/91821885/c80d5836-f162-4994-ac5a-d6e8bffd11a5" alt="robot1" width="250" height="250">
</p>


