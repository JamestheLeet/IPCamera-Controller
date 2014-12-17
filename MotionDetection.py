import cv2
import os

class MotionDetection:
	def __init__(self, motionlevel, threshold, directory):
		self.__image0 = None
		self.__image1 = None
		self.__image2 = None
		self._MOTION_LEVEL = motionlevel
		self._THRESHOLD = threshold
		self._DIRECTORY = directory
	
	def _updateImage(self, image):
		self.__image2 = self.__image1
		self.__image1 = self.__image0
		self.__image0 = image
	
	def _ready(self):
		return self.__image0 != None and self.__image1 != None and self.__image2 != None

	def _getMotion(self):
		if not self._ready():
			return None
		d1 = cv2.absdiff(self.__image1, self.__image0)
		d2 = cv2.absdiff(self.__image2, self.__image0)
		result = cv2.bitwise_and(d1, d2)
		(value, result) = cv2.threshold(result, self._THRESHOLD, 255, cv2.THRESH_BINARY)
		scalar = cv2.sumElems(result)
		print ' - scalar:', scalar[0], scalar
		return scalar
	
	def detectMotion(self, image):
		self._updateImage(image)
		motion = self._getMotion()
		if motion and motion[0] > self._MOTION_LEVEL:
			return True
		return False
	
	def saveImage(self, file_name):
		cv2.imwrite(os.path.join(self._DIRECTORY, file_name), self.__image0)
		print ' - Image saved:', file_name
