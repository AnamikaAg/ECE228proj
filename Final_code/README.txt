== Description of software ==
The software uses three seperate codes for preprocessing, deep learning and postprocessing.

1) preprocessing_imageJ.ipynb : Filter out the fluorescence light from the input image of an ER netwrok.
2) uNet-ER-new.ipynb : Deep learning U-net segmentation of ER-network data.
3) skel_test.py : Postprocessing of an input image to build a network structure.

-------------------------------------------------------------------------------------------------------------------------------------------------
			1) Preprocessing of the Images - preprocessing_imageJ.ipynb  	
-------------------------------------------------------------------------------------------------------------------------------------------------
== Installation details: ==

Language: Python(Notebook)
Required Packages: CV2, numpy, matplotlib, PIL.

== Input/Output details ==
Input details(Any format, .JPG,TIF,etc.):  	A noisy image of an ER network with fluorescence light.

Output details (.JPG): 				Filtered image with a reduction in the fluorescence light that, 
		       				facilitates better visualization of network present in the cell.

== How the code works ==

1) Call the Image that needs to be filtered in the section Input image of the code.
2) Run the code
   Method used:
   The code picks up the color of the pixels that are not in fluorescence light and,
   swaps those colors into the fluorescence light pixels position.
3) Get the output filtered image. The output image will be saved in the same folder with the name, "filteredimage.jpg".
4) Use Image J software to visualize the skeleton of the image.

-------------------------------------------------------------------------------------------------------------------------------------------------
			2) Deep learning model for feature extraction - uNet-ER-new.ipynb 	
-------------------------------------------------------------------------------------------------------------------------------------------------
== Installation details: ==

Language: Python(Notebook)
Required Packages: tensorflow, numpy, Keras, pickle, matplotlib, sys, data 


== Input/Output details: ==
Input details(JPG,TIF,etc.):  	Training dataset (provided upon request, email ana057@ucsd.edu)
				Test data (008_colorized-RGB.tif) also provided upon request. 
				Code data.py includes:
				geneTrainNpy(image_path = "ERdata_Images/", mask_path = "ERdata_Masks/",image_prefix = "Image",mask_prefix = "Mask").
				Training/Test data used, Image dimensions:
				IMG_HEIGHT = 512.
				IMG_WIDTH = 512.
				IMG_CHANNELS = 1.

Output details (.JPG): 		Image after segmentation.(Variable "predict" in the code).

== How the code works ==

1) Build a deep learning model to train the data (available upon request)
   model = tf.keras.Model(inputs=[inputs], outputs=[outputs])
   model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss='binary_crossentropy', metrics=['accuracy']).
2) Use the model to predict the outcome of a new image from model.predict
3) Visualize the error, accuracy, and the output image.

-------------------------------------------------------------------------------------------------------------------------------------------------
			2) Postprocessing of images - skel_test.py	
-------------------------------------------------------------------------------------------------------------------------------------------------
== Installation details: ==

Language: Python (.py)
Required Packages: CV2, numpy


== Input/Output details: ==

Function to use: 		skel1(img, name).
Input details(JPG,TIF,etc.):  	img: Inputs in a binary mask that and a string that's the filename/path.
				name: File path.

Output details (.JPG):		The skeleton image at the provided filepath.

== How the code works ==
1) The function skel1(img, name) read the image as a grayscale image.
2) Apply thresholding.
2) Use packages from CV2 to develop skeleton .


