import time
import datetime
import picamera

def time_check():
	""" Checks whether the time is within a range """
	current_time = datetime.datetime.now().time()
	start = datetime.time(07)
	end = datetime.time(18)
	return start <= current_time <= end
	
def capture_photo():
	""" Takes a photo and stores it with the time taken as the name"""
	time_now = datetime.datetime.now().time()
	with picamera.PiCamera() as camera:
		time.sleep(2)
		camera.capture('/home/pi/timelapse/dtu/frame%s.jpg' % time_now)

# Loop taking pictures within a given time.
while True:
	if time_check():
		capture_photo()
	else:
		time.sleep(3600)

