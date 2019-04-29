# Intrusion Detection
Feel Unsafe? This prototype has got you covererd.

A simple security mechanism can cost hundreds of dollars these days and the you are still not the one in full control over it. The Intrusion Detection System that was created is a prototype for veratile security. This detection system can be placed just about anywhere that you have internet. This system monitors an area using an ultrasonic sensor and when the user defined distance is intruded upon by an outsider a snapshot is then taken of the culprit. A log of all previous offenses are stored on a local server that you can acccess and view. This lets you not miss anything and even keep track of potentially repeat intruders.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
## Prerequisites
* Raspberry Pi Zero W
![Pi Zero W](https://i.imgur.com/hYTxbHU.png)
* MaxBotix USB Ultrasonic sensor
![MaxBotic=x USB sensor](https://i.imgur.com/ZSyAQko.png)
* Raspberry Pi Zero W compatible camera
![Pi Camera](https://i.imgur.com/HT9Xe3I.png)

Along with these items there is a need for an internet connection and connection cables.
## Installing
Once you have obtained the necessary hardware to run the project you must start setting up your raspberry pi zero w. The very first thing that you must do to allow a raspberry pi to work is to put an operating system on it so that it can run. Use a microSD and put rasbian-lite or desktop on it. This project was done with python, flask, and html so there are a few packages that are needed to be on the raspberry pi to let it run. To begin the installation you must first update your raspberry pi this can be done with the commands below.
```
sudo apt-get install update
sudo apt-get install upgrade
```
Once this is done your libraries will be up to date. So to continue installing the proper packages so that the project can run. If you have other means to get the respective packages that is fine too.
```
sudo apt-get install python
sudo apt-get install python-flask
sudo apt-get install python-serial
sudo apt-get install python-picamera
sudo apt-get install python-pil
```
After this is complete you should have the necessary installations on the raspberry pi to run the project. So, next is to place the files on the raspberry pi. Personally I use filezilla but place all of the Intrusion Detection files on to the Raspberry Pi. The location can vary but you may need to change global variables 'picturePath' and 'logPath' to correspondingly match the location. For basic use just keep the files in raspberry pi root.

*NOTE: you will need to edit the configuration of the Raspberry Pi to allow the camera to be used. This can be done by entering 'raspi-config' in the command line and then finding the camera under interface options. The Wifi for the Raspberry Pi Zero W can also be set up here.

## Assembly
Now that all the corresponging software is installed you can start assembling the device together.
The final result should look similar to the image below.
![Full Assembly](https://i.imgur.com/eLpMkKJ.jpg)

The MaxBotix ultrasonic sensor should be connected to the available usb on the Raspberry Pi Zero W, there will need to a usb to microUSB converter to allow the maxBotix ultrasonic sensor to work with the Raaspberry Pi. In the case shown, we are using the on-chip Wifi from the Raspberry Pi Zero W. This was configured in the 'raspi-config' interface. Also the camera must be connected at the bottom with a ribbon cable.

### Running the Tests
Making sure that the raspberry pi has a connection to the internet source that you are on and it has power we can finally initialize the product. If you are unsure of how to connect to the Raspberry Pi at this point you can use PuTTY, and as long as you are on the same internet source as your Pi you can establish a connection by using the ip-address of the Raspberry Pi. Now go to where the files are located and then run the command below to start the program.

```
sudo python intrusionDetection.py
```

Once this command has been run it will start a python flask local webserver that is able to be accessed by units on the same local network. Direct yourself to the local webserver by entering the addess 'http://yourRaspberryPiIP:5000' once you connect to this server you can view the information of the intruders that your sensor has picked up. The webserver login should look like the image below.

![webServer](https://i.imgur.com/O3a0SkK.png)

Once you are on this login page uses the default password that is located in the global variables on the 'intrusionDetection.py' file. You can change this to whatever sort of password that you would like, it will be your password for the site.

Now please log in and now every single time the sensor detects an intruder within the range decided it will take a picture and log it on the site. If you want more or less range also on the detection you can adjust that along with the password on the webserver.

![webServer](https://i.imgur.com/N2XHV7f.png)

#### Authors
* Trenton Bruno
* Ludovic Tabondjou
