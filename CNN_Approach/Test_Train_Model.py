import Train_Model
import Models
import unittest
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torchtest import assert_vars_change
from PIL import Image
import os

class Test_train_model(unittest.TestCase):
    def setUp(self):
        self.inputs = Variable(torch.randn(10, 1,256,256))
        self.targets = Variable(torch.randint(0, 1, (10,1,256,256))).float()
        self.batch = [self.inputs, self.targets]
        self.loss_fn=nn.MSELoss()
# Test case 16
    def test_unet(self):
        self.model = Models.unet()
        print('Unet parameters', [ np[0] for np in self.model.named_parameters() ])
        assert_vars_change(
            model=self.model,
            loss_fn=self.loss_fn,
            optim=torch.optim.Adam(self.model.parameters(),lr=1e-3, weight_decay=0.005),
            batch=self.batch,
            device ='cuda')
# Test case 17
    def test_unet_bn(self):
        self.model = Models.unet_bn()
        print('Unet with batch norm parameters', [ np[0] for np in self.model.named_parameters() ])
        assert_vars_change(
            model=self.model,
            loss_fn=self.loss_fn,
            optim=torch.optim.Adam(self.model.parameters(),lr=1e-3, weight_decay=0.005),
            batch=self.batch,
            device ='cuda')
# Test case 18
    def test_unet_d(self):
        self.model = Models.unet_d()
        print('Unet with dropout parameters', [ np[0] for np in self.model.named_parameters() ])
        assert_vars_change(
            model=self.model,
            loss_fn=self.loss_fn,
            optim=torch.optim.Adam(self.model.parameters(),lr=1e-3, weight_decay=0.005),
            batch=self.batch,
            device ='cuda')
# Test case 19
    def test_input_size_to_model(self):
        self.data_dir = 'Dataset/Data/' 
        self.dl = os.listdir(self.data_dir)
        self.num_images = len(self.dl)
        self.required_size = 256
        for index in range(0,self.num_images) :
            print('Verifying Image ', self.dl[index])
            data = Image.open(os.path.join(self.data_dir,self.dl[index]))
            self.assertEqual(Train_Model.check_input_size_model(data,self.required_size),True)
        
# if __name__ == '__main__':
#     unittest.main()