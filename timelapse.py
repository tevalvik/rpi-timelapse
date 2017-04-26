import time
import datetime
import picamera

PATH = '/home/pi/timelapse/images/'

def time_check():
	''' Checks whether the time is within a given timeframe. '''
	"Time on the pi is one hour off. 06 = 07"
	current_time = datetime.datetime.now().time()
	start = datetime.time(6)
	end = datetime.time(15)
	return start <= current_time <= end
	
def capture_photo():
	''' Takes a photo and stores it with the time taken as the name.'''
	time_now = datetime.datetime.now()
	with picamera.PiCamera() as camera:
		time.sleep(30)
		print "Taking photo"
                camera.capture(PATH + "im%s.jpg" % time_now)
		# camera.capture('/home/pi/timelapse/images/im%s.jpg' % time_now)
		print "Photo taken at %s " % time_now

# Taking pictures in the given timeframe.
while True:
	if time_check():
		capture_photo()
	else:
		current_time = datetime.datetime.now().time()
		print "Sleep for 1 minute at %s " % current_time
		time.sleep(60)

