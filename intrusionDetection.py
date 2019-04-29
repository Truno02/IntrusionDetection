import time
from serial import Serial
from picamera import PiCamera
from flask import Flask, render_template, session, request, redirect, url_for
from multiprocessing import Process, Value
from PIL import Image
import glob
import datetime
import os

app = Flask(__name__)

# global variables
serialDevice = "/dev/ttyUSB0" # default for RaspberryPi
maxwait = 3 # seconds to try for a good reading before quitting
picturePath = "/home/pi/static/pictures" # path to the pictures
logPath = "/home/pi/static/logs" # path to the logs
doorWidth = 915 # in mm
percentTrigger = 0.8 # percent missing of door width to trigger alert
myPassword = "passport"

# webpages
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != myPassword:
            error = 'Invalid credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
	
@app.route("/home")	
def home():
	if session.get("logged_in") == True:
	
		# grab past records
		pastRecords=os.listdir(logPath)

		# grab past images
		pastPictures=os.listdir(picturePath)

		# grab latest picture
		pictureList = glob.glob(picturePath + "/*.jpg")
		latestImage = os.path.basename(max(pictureList, key=os.path.getctime))
		
		# grab latest record
		logList = glob.glob(logPath + "/*.txt")
		latestRecord = os.path.basename(max(logList, key=os.path.getctime))
		
		return render_template("home.html", pastRecords = pastRecords, pastPictures = pastPictures, latestImage = latestImage, latestRecord = latestRecord, doorSize = doorWidth)
	else:
		return redirect(url_for('login'))
		
@app.route("/logout")
def logout():
		session['logged_in'] = False
		return redirect(url_for('login'))
		
@app.route("/changePass", methods=['POST'])
def changePass():
	if session.get("logged_in") == True:
		newPassword = request.form['newPassword']
		if newPassword != "":
			global myPassword 
			myPassword = newPassword
		return redirect(url_for('home'))
	else:
		return redirect(url_for('login'))

@app.route("/changeDoor", methods=['POST'])
def changeDoor():
	if session.get("logged_in") == True:
		newSize = request.form['newSize']
		if newSize != "":
			global doorWidth 
			doorWidth = newSize
		return redirect(url_for('home'))
	else:
		return redirect(url_for('login'))
	
	
# functions
def measure(portName):
    ser = Serial(portName, 57600, 8, "N", 1, timeout=1)
    timeStart = time.time()
    valueCount = 0

    while time.time() < timeStart + maxwait:
        if ser.inWaiting():
            bytesToRead = ser.inWaiting()
            valueCount += 1
            if valueCount < 2: # 1st reading may be partial number; throw it out
                continue
            testData = ser.read(bytesToRead)
            if not testData.startswith(b'R'):
                # data received did not start with R
                continue
            try:
                sensorData = testData.decode('utf-8').lstrip('R')
            except UnicodeDecodeError:
                # data received could not be decoded properly
                continue
            try:
                mm = int(sensorData)
            except ValueError:
                # value is not a number
                continue
            ser.close()
            return(mm)

    ser.close()
    raise RuntimeError("Expected serial data not received")
	
def takePicture(camera, x):
	# take the picture with no delay
	camera.start_preview()
	time.sleep(0.5)
	camera.capture(picturePath + "/intruder" + str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second) + ".jpg")
	camera.stop_preview()

def takeLog(distance, x):
	# takes the logging for the intrusions of the day
	file = open(logPath + "/" + str(x.year) + str(x.month) + str(x.day) + ".txt", "a+")
	file.write("Intrusion - " + str(x) + "\n")
	file.write("	picture: intruder" + str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second) + ".jpg\n")
	file.write("	distance: " + str(distance) + "mm away\n\n");
	file.close()

def detectIntruderLoop(loop_on):
	camera = PiCamera()
	previousValue = 0
	lastFailed = False
	
	while True:
		if loop_on.value == True:
			distance = measure(serialDevice)
			currSize = len(str(distance))
			sizeDiff = abs(currSize - len(str(previousValue))) 
			
			# checks for bad reads
			if sizeDiff > 0:
				lastFailed = True
			else:
				lastFailed = False

			#print distance
			if (distance < percentTrigger * doorWidth and currSize >= 3 and lastFailed != True):
				print "Took picture and made record"
				x = datetime.datetime.now()
				takePicture(camera, x)
				takeLog(distance, x)
				time.sleep(2)
				
			previousValue = distance
			time.sleep(2)
			
		
if __name__ == '__main__':
	detectionOn = Value('b', True)
	p = Process(target=detectIntruderLoop, args=(detectionOn,))
	p.start()
	app.secret_key = os.urandom(24)
	app.run(host='0.0.0.0', debug=True, use_reloader=False)
	p.join()