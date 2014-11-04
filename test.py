import time
import datetime
import picamera

VIDEO_DAYS = 5
FRAMES_PER_HOUR = 1
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def time_check():
	current_time = datetime.datetime.now().time()
	start = datetime.time(16)
	end = datetime.time(21,59)
	return start <= current_time <= end

	
def capture_photo():
	time_now = datetime.datetime.now().time()
	with picamera.PiCamera() as camera:
		time.sleep(2)
		camera.capture('/home/pi/timelapse/dtu/frame%s.jpg' % time_now)

if time_check():
	capture_photo()
else:
    print "hello"

