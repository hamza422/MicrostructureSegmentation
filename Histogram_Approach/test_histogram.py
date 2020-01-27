import os
import unittest
import cv2
from HistrogramApproch import HistrogramApproch
from Image import Image
from AugmentedImageData import AugmentedData

class Test_HistogramApproch(unittest.TestCase):
    HIST= HistrogramApproch()
    def test_orignal_Images(self):
        self.HIST.get_Images()
        orignal_Image = cv2.imread('original.tif', 0)
        self.assertEqual(orignal_Image.all(), self.HIST.orignal_Image.all())

    def test_Color_Images(self):
       color_Image = cv2.imread('color.tif', 1)
       self.assertEqual(color_Image.all(), self.HIST.color_Image.all())

    def test_Output_Images(self):
       output_image = cv2.imread('output_image.tif', 1)
       self.assertEqual(output_image.all(), self.HIST.output_image.all())

    def test_AugmentedData(self):
	    DATA = AugmentedData()
	    DATA.crop_Color_Images()
	    DATA.crop_Color_Images()
	    color = len(os.listdir("coloredImage"))
	    original = len(os.listdir("OrignalImage"))
	    self.assertEqual(color,original)
	

if __name__ == '__main__':
    unittest.main()
