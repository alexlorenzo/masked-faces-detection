"""Useful functions to prepare the datasets for YOLO object detection module."""
import os
import glob
import random
import shutil

random.seed(123)

def remove_img_without_label(directory):
    """Remove .txt and .jpg files without labels.
    Search for txt files size = 0 and remove the associated images.
    Paramters
    ----------
    directory: str
        directory with txt and jpg files
    """
    fileList_txt=glob.glob(os.path.join(directory,"*.txt"))

    for filename in fileList_txt:
        if os.stat(filename).st_size==0:
            os.remove(os.path.join(directory, filename))
            img_file = os.path.basename(filename).replace('.txt', '.jpg')
            os.remove(os.path.join(directory, img_file))
            
    
def create_train_test_valid(base_dir, dir_img, dir_label, dir_txt):
    
     dict_split_data = _split_train_test(base_dir, file_type='jpg',
                                         pct_train=0.7, pct_valid=0.2, pct_test=0.1)
     
     for key, list_files in dict_split_data.items():
         # create .txt files
        _create_txt_file(output_dir= dir_txt, split_folder= key, list_files= list_files)
         # images folder 
        os.makedirs(os.path.join(dir_img, key), exist_ok=True)
        # labels folder 
        os.makedirs(os.path.join(dir_label, key), exist_ok=True)
        for filename in list_files:
            # copy images
            _copy_files(filename= filename, output=dir_img, split_folder= key)
            # copy labels
            _copy_files(filename= filename.replace('.jpg', '.txt'), output=dir_label, split_folder= key)


def _split_train_test(dir, file_type= 'jpg', pct_train=0.7, pct_valid=0.25, pct_test=0.1):
    """Split in train, test, validation sets.
    Parameters
    -----------
    dir: str
        Directory to find all images
    file_type: str
        Specify file type (ex: .jpg, .txt)
    pct_train: float64
        Percentage of train images
    pct_valid: float64
            Percentage of valid images
    pct_test: float64
       Percentage of test images"""
               
    dict_split_data= {}      
    assert os.path.exists(dir)
    # list all jpg images
    list_img = glob.glob(os.path.join(dir,'*.'+file_type))   
    nb_images = len(list_img)
    
    dict_split_data['train']= random.sample(list_img, round(nb_images*pct_train))
   
    valid_test = list(set(list_img)-set(dict_split_data['train']))
    
    dict_split_data['valid'] = random.sample(valid_test, round(nb_images*pct_valid)) 
    dict_split_data['test'] = list(set(valid_test)-set(dict_split_data['valid']))
    
    assert set(dict_split_data['valid']) & set(dict_split_data['train'])==set()
    
    return dict_split_data


def _copy_files(filename, output, split_folder):
    """Copy files.
    Parameters
    ----------
    list_dir: list
    split_folder: str
        ex: train, test, valid
    output: str
        directory output
    """
    assert os.path.exists(os.path.join(output, split_folder))

    shutil.copy(filename, os.path.join(output, split_folder))


def _create_txt_file(output_dir, split_folder, list_files):
    """Create txt file with path of images."""
    
    with open(os.path.join(output_dir, split_folder +'.txt'), 'w') as f:
        for item in list_files:
            basename = os.path.basename(item)
            f.write("%s\n" % ('images/'+ split_folder + '/' + basename))



directory = "/data/yolo/obj_train_data"
base_dir = "/data/yolo/obj_train_data"
dir_img = "/data/yolo/images2"
dir_txt = "/data/yolo/"
dir_label = "/data/yolo/labels2"

remove_img_without_label(directory)
create_train_test_valid(base_dir, dir_img, dir_label, dir_txt)
