import UnetApproach
import unittest
from PIL import Image
import datetime
import os

class Test_unetApproach(unittest.TestCase):
    def setUp(self):
        self.user_input_dir = 'Unet_input/'
        self.user_output_dir = 'Unet_output/'

# Test case 10
    def test_bestmodel_location(self):
        self.best_model_dir = 'models/'
        self.dl = os.listdir(self.best_model_dir)
        self.assertIsNotNone(self.dl)
# Test case 11
    def test_userinput_dimension(self):
        self.required_size = 256
        self.user_input_dir = 'Unet_input/'
        self.dl = os.listdir(self.user_input_dir)
        self.num_images = len(self.dl)
        self.img = Image.open(os.path.join(self.user_input_dir,self.dl[0]))
        self.assertTrue(UnetApproach.check_input_size(self.img,self.required_size))
# Test case 15       
    def test_data_with_bestmodel(self):
        self.name = 'unet_bn'
        self.assertTrue(UnetApproach.Unet_test_model_for_user_input(self.name,self.user_input_dir,self.user_output_dir))
# Test case 12
    def test_runtime(self):
        self.name = 'unet_bn'
        starttime = datetime.datetime.now()
        self.input_dir = 'User_input/'
        self.output_dir = 'User_output/'
        self.assertTrue(UnetApproach.Unet_test_model_for_user_input(self.name,self.input_dir,self.output_dir))
        endtime= datetime.datetime.now()
        self.assertLessEqual((endtime-starttime).total_seconds(),5)
# Test case 13
    def test_modeloutput_location(self):
        self.dl = os.listdir(self.user_output_dir)
        self.assertIsNotNone(self.dl)
        
# if __name__ == '__main__':
#     unittest.main()
