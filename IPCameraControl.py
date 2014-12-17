import urllib2
from time import sleep
import cv2
import numpy

class IPCamera:
	def __init__(self, address, port, user, password):
		self.address = str(address)
		self.port = str(port)
		self.user = str(user)
		self.password = str(password)

	def callPos(self, preset):
		preset = int(preset)
		if preset > 16:
			return False
		elif preset < 1:
			return False
		else:
			preset = str((preset - 1) * (61 - 31) // (16 - 1) + 31)
			response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=' + preset + '&onestep=0&sit=' + preset)
			return True

	def panUp(self, time):
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=0&onestep=0&sit=0')
		sleep(time)
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=1&onestep=0&sit=1')
		return True

	def panDown(self, time):
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=2&onestep=0&sit=2')
		sleep(time)
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=3&onestep=0&sit=3')
		return True

	def panLeft(self, time):
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=4&onestep=0&sit=4')
		sleep(time)
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=5&onestep=0&sit=5')
		return True

	def panRight(self, time):
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=6&onestep=0&sit=6')
		sleep(time)
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=7&onestep=0&sit=7')
		return True

	def hPatrol(self, onoff):
		action = str(29 - onoff)
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=' + action + '&onestep=0&sit=' + action)
		return True

	def vPatrol(self, onoff):
		action = str(27 - onoff)
		response = urllib2.urlopen('http://' + self.address + ':' + self.port + '/decoder_control.cgi?loginuse=' + self.user + '&loginpas=' + self.password + '&command=' + action + '&onestep=0&sit=' + action)
		return True

	def getImage(self):
		url = 'http://' + self.address + ':' + self.port + '/snapshot.cgi?user=' + self.user + '&pwd=' + self.password
		img = urllib2.urlopen(url).read()
		img = cv2.imdecode(numpy.fromstring(img,dtype=numpy.uint8),cv2.CV_LOAD_IMAGE_COLOR)
		return img


