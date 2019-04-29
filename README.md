# IntrusionDetection
Feel Unsafe? This prototype has got you covererd.

A simple security mechanism can cost hundreds of dollars these days and the you are still not the one in full control over it. The Intrusion Detection System that was created is a prototype for veratile security. This detection system can be placed just about anywhere that you have internet. This system monitors an area using an ultrasonic sensor and when the user defined distance is intruded upon by an outsider a snapshot is then taken of the culprit. A log of all previous offenses are stored on a local server that you can acccess and view. This lets you not miss anything and even keep track of potentially repeat intruders.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
## Prerequisites
* Raspberry Pi Zero W
![Pi Zero W](https://i.imgur.com/hYTxbHU.png)
* MaxSonar USB Ultrasonic sensor
![MaxSonar USB sensor](https://i.imgur.com/ZSyAQko.png)
* Raspberry Pi Zero W compatible camera
![Pi Camera](https://i.imgur.com/HT9Xe3I.png)

Along with these items there is a need for an internet connection and connection cables.
## Installing
Once you have obtained the necessary hardware to run the project you must start setting up your raspberry pi zero w. The very first thing that you must do to allow a raspberry pi to work is to put an operating system on it so that it can run. Use a microSD and put rasbian-lite or desktop on it. This project was done with python, flask, and html so there are a few packages to install to let it run. To begin the installation you must first update your raspberry pi this can be done with the commands below.
```
sudo apt-get install update
sudo apt-get install upgrade
```
