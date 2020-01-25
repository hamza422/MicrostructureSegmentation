import numpy as np
import cv2
from PIL import Image
import matplotlib
from random import randrange

matplotlib.use("agg")
import matplotlib.pyplot as plt

from collections import defaultdict

class HistrogramApproch:
    color_Image = cv2.imread("Boundries.tif", 0)
    orignal_Image = cv2.imread("Boundries.tif", 0)
    output_image = cv2.imread("Boundries.tif", 0)
    path = 'output'
    orignal_Image_path=""
    color_Image_path=""
    save_image_path=""
    by_color =defaultdict(int)

    def __init__(self,orignal,color,savePath):
        self.data = []
        self.orignal_Image_path=orignal
        self.color_Image_path=color
        self.save_image_path=savePath

    def get_Images(self):
        self.orignal_Image = cv2.imread(self.orignal_Image_path, 0)
        self.color_Image = cv2.imread(self.color_Image_path, 1)
        self.output_image = cv2.imread(self.orignal_Image_path, 1)
        print(str(self.orignal_Image.shape) + " " + str(self.color_Image.shape))
        # print(Croped_Orignal_Images[24]+ " "+Croped_Color_Images[24])
        self.Find_color()
        self.Find_Segments()

    def get_concat_h(self, im1, im2, im3):
        print("Dimentions")
        print(str(im1.shape) + " " + str(im2.shape) + " " + str(im3.shape))
        out = np.concatenate((im1, im2, im3), axis=1)
        cv2.imshow('output_img', out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def Find_color(self):
        image = self.color_Image
        # defaultdict(int)
        image_data = image
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                #print(image[i][j])
                self.by_color[(image[i][j][0],image[i][j][1],image[i][j][2])] += 1
        #print(self.by_color)

    def color_Segmented_image(self, buf,co_i,co_j):
        if np.mean(buf) < 130.0:
            for a in range(0, len(co_i), 1):
                self.output_image[(co_i[a]), (co_j[a])][0] = 255
                self.output_image[(co_i[a]), (co_j[a])][1] = 0
                self.output_image[(co_i[a]), (co_j[a])][2] = 0


        elif np.mean(buf) > 130.0 and np.mean(buf) < 180.0:
            for a in range(0, len(co_i), 1):
                self.output_image[(co_i[a]), (co_j[a])][0] = 0
                self.output_image[(co_i[a]), (co_j[a])][1] = 255
                self.output_image[(co_i[a]), (co_j[a])][2] = 0


        elif np.mean(buf) > 180.0:
            for a in range(0, len(co_i), 1):
                self.output_image[(co_i[a]), (co_j[a])][0] = 0
                self.output_image[(co_i[a]), (co_j[a])][1] = 0
                self.output_image[(co_i[a]), (co_j[a])][2] = 255

        else:
            print("\nNothing done")

    def Find_Segments(self):
        buf = []
        A = []
        number_of_segments = 0
        count_red = 0
        count_green = 0
        count_blue = 0
        rows_color, cols_color, channels_c = self.color_Image.shape
        rows_original, cols_original, channels_o = self.color_Image.shape

        
        for a in self.by_color:
            if a[0]==255 and a[1]==255 and a[2]==255 :
                print("No segment")

            else:
                sought = [a[0], a[1], a[2]]
                # Find all pixels where the 3 RGB values match "sought", and count
                result = np.count_nonzero(np.all(self.color_Image == sought, axis=2))
                if result != 0:
                    co_i = []
                    co_j = []
                    print(result)
                    # print("\n")
                    number_of_segments = number_of_segments + 1
                    for i in range(rows_color):
                        for j in range(cols_color):
                            if self.color_Image[i, j][0] == sought[0] and self.color_Image[i, j][1] == sought[1] and \
                                    self.color_Image[i, j][2] == sought[2]:
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
                    self.color_Segmented_image(buf,co_i,co_j)
                    # buf.clear()
                    del buf[:]
                    del co_i[:]
                    del co_j[:]
                    count_red = 0
                    count_green = 0
                    count_blue = 0
        print(self.by_color)
        print("\nNumber of segments")
        print(number_of_segments)
        # self.get_concat_h(self.orignal_Image, self.color_Image, self.output_image)
        cv2.imshow('color_img', self.color_Image)
        cv2.imshow('original_img', self.orignal_Image)
        cv2.imshow('output_img',self.output_image)
        cv2.imwrite(self.save_image_path+"/output_image_"+str(randrange(100))+".tif", self.output_image)
        # self.output_image.savefig("output_image.tif")
        cv2.waitKey(1)
        

       



#ha= HistrogramApproch("OrignalImage000000.tif","ColoredImage000000.tif","D:\SoftwareEnginnering\test\WithGui")
#ha.get_Images()