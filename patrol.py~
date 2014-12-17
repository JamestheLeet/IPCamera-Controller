from IPCameraControl import IPCamera
from MotionDetection import MotionDetection
from AlertSystems import PushBulletAlert
import time
#IPCamera stuff
address = ''
port = ''
user = ''
password = ''

#Motion Detection stuff
sensitivity = 75000 #the higher the number the less sensitive it is
threshold = 35
directory = 'images' #where the images are saved

#PushBullet stuff
api_key = ''

cam = IPCamera(address, port, user, password)
detection = MotionDetection(sensitivity, threshold, directory)
pb = PushBulletAlert(api_key, directory)

while True:
	image = cam.getImage()
	if detection.detectMotion(image):
		imt = time.localtime(time.time())
		imagename = str(imt[0]) + '-' + str(imt[1]) + '-' + str(imt[2]) + '-' + str(imt[3]) + '-' + str(imt[4]) + '-' + str(imt[5]) + '.jpg'
		detection.saveImage(imagename)
		pb.sendAlert(imagename)
	time.sleep(1)

