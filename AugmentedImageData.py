from Image import Images
import os
from os import path

#Inherite Image Class To access OrignalImage and colorImage
class AugmentedData(Images):

	#Variables
	List_Of_Colored_Images=[]
	List_Of_Orignal_Images=[]
	savePath=""
	ImageCropXsize = 256
	ImageCropYsize = 256



	#Constructor
	def __init__(self,orignal,color,savePath):
		self.data = []
		self.savePath=savePath
		#Call Parent Class read Image Function
		super(AugmentedData, self).read_Image(orignal,color) 


	#Implement method to crop the Ground Truth images in equal size
	def crop_Color_Images(self):
		infile = 'Colored.jpg'
		Xsize = 4360
		Ysize= 5800
		#Get ColorImage from Image Class
		img = self.color_Image
		width, height = img.size
		i=0
		my_list = []
		
		if(path.isdir(self.savePath+"/coloredImage")!=True):
		    os.mkdir(self.savePath+"/coloredImage")
		# Save Chops of Color image
		for x0 in range(0, width, Xsize):
			for y0 in range(0, height, Ysize):
				box = (x0, y0,x0+Xsize if x0+Xsize <  width else  width - 1,y0+Ysize if y0+Ysize < height else height - 1)
				print('%s %s' % (infile, box))
				my_list.append(img.crop(box))
		infile = 'ColoredImage.tif'
		Xsize = self.ImageCropXsize
		Ysize= self.ImageCropYsize
        #Xsize = 436
		#Ysize= 580

		img = my_list[0]
		width, height = img.size
		for x0 in range(0, width, Xsize):
			for y0 in range(0, height, Ysize):
				box = (x0, y0,x0+Xsize if x0+Xsize <  width else  width - 1,y0+Ysize if y0+Ysize < height else height - 1)
				i=i+1
				name='%s%03d%.03d.tif' % (infile.replace('.tif',''), x0, y0)
				self.List_Of_Colored_Images.append(name)
				img.crop(box).save(self.savePath+"/coloredImage/"+name)




    #Implement method to crop the Orignal images in equal size

	def crop_Orignal_Images(self):
		infile = 'Orignal.jpg'
		Xsize = 4360
		Ysize= 5800
	    #Get Orignal Image from Image Class
		img = self.orignal_Image
		width, height = img.size
		i=0
		my_list = []
		if(path.isdir(self.savePath+"/OrignalImage")!=True):
		    os.mkdir(self.savePath+"/OrignalImage")
		# Save Chops of original image
		for x0 in range(0, width, Xsize):
			for y0 in range(0, height, Ysize):
				box = (x0, y0,x0+Xsize if x0+Xsize <  width else  width - 1,y0+Ysize if y0+Ysize < height else height - 1)
				print('%s %s' % (infile, box))
				my_list.append(img.crop(box))
		infile = 'OrignalImage.tif'
		Xsize = self.ImageCropXsize
		Ysize = self.ImageCropYsize
        #Xsize = 436
		#Ysize= 580
		img = my_list[0]
		width, height = img.size
		for x0 in range(0, width, Xsize):
			for y0 in range(0, height, Ysize):
				box = (x0, y0,x0+Xsize if x0+Xsize <  width else  width - 1,y0+Ysize if y0+Ysize < height else height - 1)
				i=i+1
				name='%s%03d%.03d.tif' % (infile.replace('.tif',''), x0, y0)
				self.List_Of_Orignal_Images.append(name)
				img.crop(box).save(self.savePath+"/OrignalImage/"+name)



#data=AugmentedData()
#data.crop_Color_Images()
#data.crop_Orignal_Images()