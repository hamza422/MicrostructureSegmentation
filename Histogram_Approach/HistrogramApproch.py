import numpy as np
import cv2
from PIL import Image
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from AugmentedImageData import AugmentedData

class HistrogramApproch:
	

	color_Image=cv2.imread("Boundries.tif",0) 
	orignal_Image=cv2.imread("Boundries.tif",0) 
	output_image=cv2.imread("Boundries.tif",0) 
	path = 'output'

	def __init__(self):
		self.data = []



	def get_Images(self):
		
		self.orignal_Image=cv2.imread('original.tif',0) 
		self.color_Image=cv2.imread('color.tif',1) 
		self.output_image=cv2.imread('original.tif',1) 
		#print(Croped_Orignal_Images[24]+ " "+Croped_Color_Images[24])
		self.Find_Segments()


	def get_concat_h(self,im1, im2,im3):
			out = np.concatenate((im1, im2,im3), axis=1)
			cv2.imshow('output_img',out)
			cv2.waitKey(0)
			cv2.destroyAllWindows()

	def Find_Segments(self):
		buf = []
		A = []
		number_of_segments = 0
		count_red = 0
		count_green = 0
		count_blue = 0
		rows_color,cols_color,channels_c = self.color_Image.shape 
		rows_original,cols_original,channels_o = self.color_Image.shape

		for x in range(0, 250, 10):
			for y in range(0, 250, 10):
				for z in range(0, 250, 10):
					sought = [x, y, z]
					# Find all pixels where the 3 RGB values match "sought", and count
					result = np.count_nonzero(np.all(self.color_Image == sought, axis=2))
					if result != 0:
						co_i = []
						co_j = []
						print(result)
						#print("\n")
						number_of_segments =number_of_segments + 1
						for i in range(rows_color):
							for j in range(cols_color):
								if self.color_Image[i,j][0] == sought[0] and self.color_Image[i,j][1] == sought[1] and self.color_Image[i,j][2] == sought[2]:

									buf.append(self.orignal_Image[i][j])
									co_i.append(i)
									co_j.append(j)
						print("\nLength of buffer")
						print(len(buf))
						print("\nLength of co-ordinate array")
						print(len(co_i))
						A.append(np.mean(buf))
						print("\nMean buffer value of the segment")
						print(np.mean(buf))

						if np.mean(buf) < 130.0:
							for a in range(0, len(co_i), 1):
								#print("Test1")
								#print("pixel co-ordinates are :" )
								#print(co_i[a],co_j[a])
								#output_image.putpixel(((co_i[a]), (co_j[a])), (255, 0, 0, 255))
								self.output_image[(co_i[a]), (co_j[a])][0] = 255
								self.output_image[(co_i[a]), (co_j[a])][1] = 0
								self.output_image[(co_i[a]), (co_j[a])][2] = 0
								count_red = count_red+1
							#print("\nSegment colored red")
							#print("\nNumber of pixels colored")
							#print(count_red)
                       
						elif np.mean(buf) >  130.0 and np.mean(buf) < 180.0:
							for a in range(0, len(co_i), 1):
								#print("Test2")
								#print("pixel co-ordinates are :")
								#print(co_i[a], co_j[a])
								#output_image.putpixel(((co_i[a]), (co_j[a])), (0, 255, 0, 255))
								self.output_image[(co_i[a]), (co_j[a])][0] = 0
								self.output_image[(co_i[a]), (co_j[a])][1] = 255
								self.output_image[(co_i[a]), (co_j[a])][2] = 0
								count_green=count_green+1
							#print("\nSegment colored green")
							#print("\nNumber of pixels colored")
							#print(count_green)
                
						elif np.mean(buf) > 180.0:
							for a in range(0, len(co_i), 1):
								#print("Test3")
								#print("pixel co-ordinates are :")
								#print(co_i[a], co_j[a])
								#output_image.putpixel(((co_i[a]), (co_j[a])), (0, 0, 255, 255))
								self.output_image[(co_i[a]), (co_j[a])][0] = 0
								self.output_image[(co_i[a]), (co_j[a])][1] = 0
								self.output_image[(co_i[a]), (co_j[a])][2] = 255
								count_blue=count_blue+1
							#print("\nSegment colored blue")
							#print("\nNumber of pixels colored")
							#print(count_blue)

						else:
							print("\nNothing done")

						#A = np.asarray(buf)
						#buf.clear()
						del buf[:]
						del co_i[:]
						del co_j[:]
						count_red = 0
						count_green = 0
						count_blue = 0

	#	print(A)
		print("\nNumber of segments")
		print(number_of_segments)
		#self.get_concat_h(self.orignal_Image,self.color_Image,self.output_image)
		cv2.imshow('color_img',self.color_Image)
		cv2.imshow('original_img',self.orignal_Image)
		cv2.imshow('output_img',self.output_image)
		cv2.imwrite('output_image.tif', self.output_image)
		#cv2.waitKey(0)
        #cv2.destroyAllWindows()		

Process=HistrogramApproch()
Process.get_Images()
