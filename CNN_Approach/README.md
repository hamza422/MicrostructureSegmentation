**Boundary segmentation with CNN:**

The Deep Learning project involves the following steps which must be performed in the below order:
1. **Generating dataset:** *Generate_Dataset.py* - The original image and dataset cannot be shared as per the data confidentiality agreement with the client. 
Hence, select any image and organize it into the folder as required in the code to check for the working of this module. 
2. **Choose a network architecture to work with:** *Models.py* contains the model class for Unet, Unet with batch normalization, Unet with dropout
3. **Training, Validation and Testing the model:** *Train_Model.py* and *Dataset_Loader* - Loads dataset, trains and validates the trained model, the best model obtained during training is saved into the models folder
4. **Script integrated with GUI:** *UnetApproach.py* - Loads the saved best model and the input image from the path specified, predicts the output of the best model for each input and saves them in the designated folder
5. **Test scripts for each module:** *Test_Generate_Dataset.py*, *Test_Train_Model.py* and *Test_UnetApproach.py* - contain the testing code for each module

**Steps to run the scripts**
1. Create a conda environment:
conda create --name *name-of-new-env* python=3.6

2. Activate this environment:
conda activate *<name-of-new-env>*

3. See the list of all packages installed in this env using
conda list

4. Install the missing packages on which the project has a dependency
(The cuda and cudatoolkit packages are necessary if you are using a GPU to train the model. During development, our model was trained on a GTX 1080 processor)

5. Use this command to install torch and torchvision :
pip install torch==1.2.0+cpu torchvision==0.2.2.post3 -f https://download.pytorch.org/whl/torch_stable.html

6. Install the necessary packages using pip
Kindly install the following packages to run the code:
* torch                     1.2.0
* torchvision               0.2.2
* scikit-image              0.15.0
* pytorch                   1.1.0
* pillow                    6.0.0
* python                    3.6.8
* numpy                     1.16.3
* matplotlib                3.1.0
* torchtest

7. After the environment is set up, run any python file from the project:
python *any-python-file*
OR
Run the project in an IDE (eg: Visual Studio Code)





