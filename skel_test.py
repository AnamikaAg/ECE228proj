#Skeletonization


import cv2
import numpy as np



def skel_try(img):
	#img = cv2.imread('sofsk.png',0)
	size = np.size(img)
	skel = np.zeros(img.shape,np.uint8)

	ret,img = cv2.threshold(img,127,255,0)
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
	done = False

	while( not done):
	    eroded = cv2.erode(img,element)
	    temp = cv2.dilate(eroded,element)
	    temp = cv2.subtract(img,temp)
	    skel = cv2.bitwise_or(skel,temp)
	    img = eroded.copy()

	    zeros = size - cv2.countNonZero(img)
	    if zeros==size:
	        done = True

	cv2.imshow("skel",skel)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return skel

####




def skel1(img):

# Read the image as a grayscale image
	#img = cv2.imread('A://testimg5.jpg', 0)

	# Threshold the image
	ret,img = cv2.threshold(img, 127, 255, 0)

	# Step 1: Create an empty skeleton
	size = np.size(img)
	skel = np.zeros(img.shape, np.uint8)

	# Get a Cross Shaped Kernel
	element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

	# Repeat steps 2-4
	while True:
	    #Step 2: Open the image
	    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
	    #Step 3: Substract open from the original image
	    temp = cv2.subtract(img, open)
	    #Step 4: Erode the original image and refine the skeleton
	    eroded = cv2.erode(img, element)
	    skel = cv2.bitwise_or(skel,temp)
	    img = eroded.copy()
	    # Step 5: If there are no white pixels left ie.. the image has been completely eroded, quit the loop
	    if cv2.countNonZero(img)==0:
	        break

	# Displaying the final skeleton
	cv2.imshow("Skeleton",skel)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return skel



#im1 = cv2.imread('005_colorized-Mask000.png',0)

#print(skel1(im1))

