from unetmodel import *
import PIL
from PIL import Image
from torchvision.transforms import transforms
trans = transforms.ToPILImage()

path = ''
# --------------------------------
# Device configuration
# --------------------------------
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# if device == 'cuda':
#     print('Initial GPU:',torch.cuda.current_device())
   
#     torch.cuda.set_device(1)
#     print('Selected GPU:', torch.cuda.current_device())

device = 'cpu'
print('Using device: %s'%device)

def check_input_size(input_image,required_size):   
    x_dim,y_dim = input_image.size
    # y_dim = int(input_image.size()[3])
    if x_dim != required_size or y_dim != required_size :
        return False
    else:
        return True

def Unet_test_model_for_user_input(name, user_input_dir, user_output_dir):
    
    print('Unet Implementation for user input')
    # Initialize the model for this run
    if name == 'unet':
        bestESmodel = unet()
    elif name == 'unet_bn':
        bestESmodel = unet_bn()
    elif name == 'unet_d':
        bestESmodel = unet_d()
    else:
        print('Method does not exist')
        return None
    bestESmodel.load_state_dict(torch.load(path+'models/bestESModel_'+name+'.ckpt', map_location='cpu'))
    # bestESmodel = bestESmodel.to(device)
    bestESmodel.eval()
    required_size = 256
    dl = os.listdir(user_input_dir)
    num_images = len(dl)
    for index in range(0,num_images):
        img = Image.open(os.path.join(user_input_dir,dl[index]))
        # compare input dimensions to required dimension
        if check_input_size(img,required_size) == False:
            raise Exception('Invalid Input size')
        else:
            print('Segmenting image '+str(index+1)+'/'+str(num_images))
            img = transforms.ToTensor()(img)
            img = img.to(device)
            img = img.unsqueeze(0)
            output = bestESmodel(img)
            output = output.cpu()
            img = trans(output[0])
           # img.show()
            img.save(user_output_dir+'/'+name+'_%d.tif'%(index))
    return True
  
###############################################################################################################################################
def Initialize_Unet_paths (ImagePath,savePath):
    user_input_dir = ImagePath
    user_output_dir = savePath

    # parameters to select different models ==> Just change here. 
    # name = 'unet'
    name = 'unet_bn'
    # name = 'unet_d'
    Unet_test_model_for_user_input(name, user_input_dir, user_output_dir)

# name = 'unet_bn'
# user_input_dir = 'Unet_input/'
# user_output_dir = 'Unet_output/'
# Unet_test_model_for_user_input(name, user_input_dir, user_output_dir)
