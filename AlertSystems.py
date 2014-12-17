from pushbullet import PushBullet
import os

class PushBulletAlert:
	def __init__(self, api_key, imagedir):
		self.pb = PushBullet(api_key)
		self.imagedir = imagedir

	def sendAlert(self, image):
		imagedata = open(os.path.join(self.imagedir, image), 'rb')
		success, file_data = self.pb.upload_file(imagedata, 'Motion detected: ' + image)
		success, push = self.pb.push_file(**file_data)
		return success 
