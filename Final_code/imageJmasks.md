# Using imageJ for binarizing network data 

Currently we use grayscale membrane data which is not very similar morphologically to ER network data. Here are steps to extract binary images from ER data using ImageJ. Can use it as an interactive example as well as for training our networks better. 

## Install ImageJ 
[Download FIJI (FIJI is just ImageJ)](https://imagej.net/Fiji/Downloads) 

## Image Processing Examples on ImageJ
* ImageJ can open .tif files directly as a t-stack. Depending on the channels used, it also has an option of separating an image stack into different channels
### sample image of an ER network 
<img src="https://gist.github.com/AnamikaAg/cd83b85b67ee4af56dc08845dece4337/raw/z1.png" alt="z1.png" height="300" align="middle"/>

This image is an RGB stack

### sample binarization

Using Process > Binary > Make Binary 

<img src="https://gist.github.com/AnamikaAg/cd83b85b67ee4af56dc08845dece4337/raw/z2.png" alt="z2.png" height="300" align="middle"/>

### sample edge detection

Can use this on the RGB image, but better results with Binary image for our purpose. Use Process > Binary > Outline OR Process > Find Edges

<img src="https://gist.github.com/AnamikaAg/cd83b85b67ee4af56dc08845dece4337/raw/z3.png" alt="z3.png" height="300" align="middle"/>

### sample skeletonization

On the Binary image, use Process > Binary > Skeletonize

<img src="https://gist.github.com/AnamikaAg/cd83b85b67ee4af56dc08845dece4337/raw/z4.png" alt="z4.png" height="300" align="middle"/>

### other options to explore : 
separate channels (Image > Color > Split Channels), applying filters (Process > Filters > ..) 
