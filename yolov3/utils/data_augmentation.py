import imgaug as ia
import imgaug.augmenters as iaa
import imageio
import random
import shutil
import os


def data_augmentation(path):
    ia.seed(2)

    seq = iaa.Sequential([
        iaa.Sometimes(0.5,
                    iaa.Grayscale(alpha=(0.1, 0.5))),
        iaa.Sometimes(0.5,
                        iaa.Multiply((0.5, 1.5), per_channel=0.5)),
        iaa.Sometimes(0.5,
                    iaa.MultiplyHueAndSaturation(mul_saturation=(0.5, 1.5))),
        iaa.Sometimes(0.5,
                    iaa.GaussianBlur(sigma=(0, 2.0))),
        iaa.Sometimes(0.8,
                    iaa.MultiplyBrightness((0.5, 1.5))),
        iaa.AddToBrightness((-30, 30)),
        iaa.Sometimes(0.6,
                iaa.MultiplyHueAndSaturation(mul_saturation=(0.5, 1.5)))
    ], random_order=True)

    i=0
    for fname in os.listdir(path):

        try:
            img = imageio.imread(os.path.join(path, fname), pilmode="RGB")
            print(i)
            if i % 5 == 0:
                img_aug = seq.augment_image(img)
                imageio.imwrite(os.path.join(path, fname.replace(".jpg","_imgaug.jpg")), img_aug)
                fname_txt = fname.replace('.jpg', '.txt')
                print( os.path.join(path,  fname_txt.replace(".txt","_imgaug.txt")))
                shutil.copyfile(os.path.join(path, fname_txt), os.path.join(path, fname_txt.replace(".txt","_imgaug.txt")))

        except:
            print('Error reading img')
        i+=1