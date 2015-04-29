import time
import datetime
import picamera

def time_check():
	""" Checks whether the time is within a given timeframe. """
	"Time on the pi is one hour off. 06 = 07"
	current_time = datetime.datetime.now().time()
	start = datetime.time(21)
	end = datetime.time(23)
	return start <= current_time <= end
	
def capture_photo():
	""" Takes a photo and stores it with the time taken as the name."""
	time_now = datetime.datetime.now()
	with picamera.PiCamera() as camera:
		time.sleep(10)
		print "Taking photo"
		camera.capture('/home/pi/timelapse/dtu/images/im%s.jpg' % time_now)
		print "Photo taken at %s " % time_now

# Taking pictures in the given timeframe.
while True:
	if time_check():
		capture_photo()
#	else:
#		print "Sleep for 30 minutes."
#		time.sleep(1800)

