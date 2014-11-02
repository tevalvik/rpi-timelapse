import time
import datetime
import picamera

VIDEO_DAYS = 5
FRAMES_PER_HOUR = 1
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

#date = datetime.datetime.now().time() # gives current time without date
#print (datetime.datetime.now().time())
#
#start = datetime.time(16, 15) 
#end = datetime.time(16,17)
#print start
#print end
#print (start <= date <= end)

def time_check():
	current_time = datetime.datetime.now().time()
	start = datetime.time(16)
	end = datetime.time(16,27)
	return start <= current_time <= end

while time_check():
	print "time check works"
	time.sleep(5)
	
