
import os, sys
import zipfile
import imageio
from PIL import Image
import fire

def mkgif(path_to_zip_file):
    images = []

    if(os.path.exists(path_to_zip_file) == False):
        return 'Archive not found...'

    directory_to_extract_to = "./tmp"

    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    
    # create array of images and resize
    for imgFile in os.listdir(directory_to_extract_to):
        if imgFile.endswith(('jpg', 'png')):
            imgFilePath = directory_to_extract_to +'/'+ imgFile
            images.append( imgFilePath )
            
            #resize images
            im = Image.open(imgFilePath)
            imResize = im.resize((500,500), Image.ANTIALIAS)
            imResize.save(imgFilePath, quality=80)

    #streaming frame to gif
    with imageio.get_writer('./animate.gif', mode='I', fps=5) as writer:
        for filename in images:
            image = imageio.imread(filename)
            writer.append_data(image)
            
    #delete files
        for filename in images:
            os.remove(filename)
    
    return path_to_zip_file

if __name__ == '__main__':
    fire.Fire()
