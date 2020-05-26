from PIL import Image
import numpy as np

def read_tiff(path,channel = None):
    """
    path - Path to the multipage-tiff file
    """
    img = Image.open(path)
    images = []
    im_channel = []
    for i in range(img.n_frames):
        img.seek(i)

        images.append(np.array(img))
        im_channel.append(images[i][:,:,channel])

        #print(images[i].shape)

    if channel != None:
    	#print(im_channel[0].shape)

    	return np.array([im_channel])
    else:
    	#print("None")
    	return np.array(images)



def unit_tests():
	read_tiff("006_colorized-rgb.tif")
	read_tiff("006_colorized-rgb.tif", channel = 0)
