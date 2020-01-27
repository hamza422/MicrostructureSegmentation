import numpy as np
import cv2
from PIL import Image

class Images:
	#Variables
	color_Image=None
	orignal_Image=None
	dim_x=None
	dim_y=None

	#Constructor
	def __init__(self):
		self.data = []

	#read Image Function
	def read_Image(self):
		self.color_Image =Image.open("Histogram_Approach_color.jpeg")
		self.orignal_Image =Image.open("Histogram_Approach_original.jpeg")