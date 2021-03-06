# Image-Processing
## Gaussian Blur
- Gaussian blur known as Gaussian smoothing is the result of blurring an image by a gaussian function. It is typically used for reducing image  noise and reducing detail. 
- Mathematically, applying a Gaussian blur to an image is the same as convolving the image with Gaussian function.
- Since the Fourier transform of a Gaussian is another Gaussian, applying a Guassian blur has the effect of reducing the image’s high-frequency components; at same time, a Gaussian blur is thus a low pass filter.  
- A box blur (also known as a box linear filter) is a spatial domain linear filter in which each pixel in the resulting image has a value equal to the average value of its neighboring pixels in the input image. It is a form of low-pass ("blurring") filter. A 3 by 3 box blur can be written as 1/9 * determinant matrix:

  ![](https://github.com/yoyoberenguer/Gaussian-Blur/blob/master/boxblur.png)
### Example with 3x3 convolution kernel
  <img src = "https://github.com/garychian/Image-Processing/blob/master/Gaussian%20Blur/example%20with%20Gaussian%20blur.png" width = 240 height = 360>
  
## Prewitt
- The Prewitt operator is used in image processing, particularly within edge detection algorithms
- Technically, it is a discrete differentiation operator, computing an approximation of the gradient of the image intensity function.
- At each point in the image, the result of the Prewitt operator is either the corresponding gradient vector or the norm of this vector. The Prewitt operator is based on convolving the image with a small, separable, and integer valued filter in horizontal and vertical directions and is therefore relatively inexpensive in terms of computations like Sobel and Kayyali operators. On the other hand, the gradient approximation which it produces is relatively crude, in particular for high frequency variations in the image. 
- Mathematically, the operator uses two 3×3 kernels which are convolved with the original image to calculate approximations of the derivatives - one for horizontal changes, and one for vertical. If we define A as the source image, and Gx and Gy. are two images which at each point contain the horizontal and vertical derivative approximations, the latter are computed as:
  
  <img src = "https://github.com/yoyoberenguer/Sobel-Feldman/blob/master/Assets/Graphics/Prewitt1.png">
- The x-coordinate is defined here as increasing in the "right"-direction, and the y-coordinate is defined as increasing in the "down"-direction. At each point in the image, the resulting gradient approximations can be combined to give the gradient magnitude, using:

  <img src = "https://github.com/yoyoberenguer/Sobel-Feldman/blob/master/Assets/Graphics/Prewitt2.png">
- Use this equation shown below, we can calcuate the gradient's direction:

  <img src = "https://github.com/yoyoberenguer/Sobel-Feldman/blob/master/Assets/Graphics/Prewitt3.png">
### Example with original image

  <img src = "https://github.com/garychian/Image-Processing/blob/master/Prewitt/prewitt%20with%20original%20image.png" width = 240 height = 360>

### Example with image after Gaussian Blur

  <img src = "https://github.com/garychian/Image-Processing/blob/master/Prewitt/prewitt%20with%20GB%20image.png" width = 240 height = 360>
  
### Conclusion:
The image noise will affect the performace of edge detection, so add guassian blur to filter the images are necessary for getting good performance. 


## Canny

## SIFT(Scale Invariant Feature Transform)
### Pipeline
#### 1. Constructing a scale Space
To make sure that features are scale-independent

> Scale space is a collection of images having different scales, generated from a signle image.

> Difference of Gaussian is a feature enhancement algorithm that involves the subtraction of one blurred version of an original image from another, less blurred version of the original 
##### Here is a visual explanation how DOG works
<img src = "https://cdn.analyticsvidhya.com/wp-content/uploads/2019/09/Screenshot-from-2019-09-25-12-48-03.png" width = 240 >

#### 2. Keypoint Localisation
Identifyling the suitable features or keypoints

##### Local Max and local Min
> To locate the local Max and Min, we go through every pixel in the image and compare it with its neighboring pixels
##### Keypoint Selection
> Eliminate the keypoints that have low contrast, or lie very close to the edge

#### 3. Orientation Assignment
Ensure the keypoints are rotation invariant
##### Calculate Magnitude and Orientation

<img src = "https://cdn.analyticsvidhya.com/wp-content/uploads/2019/09/Screenshot-from-2019-09-25-19-22-24.png">

> The magnitude represents the intensity of the pixel and the orientation gives the direction for the same


#### 4. Keypoint Descriptor
Assign a unique figerprint of each keypoint
##### Keypoint Descriptor
We will first take a 16×16 neighborhood around the keypoint. This 16×16 block is further divided into 4×4 sub-blocks and for each of these sub-blocks, we generate the histogram using magnitude and orientation.

<img src = "https://cdn.analyticsvidhya.com/wp-content/uploads/2019/09/Screenshot-from-2019-09-26-20-10-52.png">

##### Here is my results using my images

<img src = "https://github.com/garychian/Image-Processing/blob/master/SIFT/Image%20point.png" width = 600 height = 300>

###### Feature Matching 

<img src = "https://github.com/garychian/Image-Processing/blob/master/SIFT/point%20match.png" width = 600 height = 500>

### End Note

SIFT is a very useful method to explore the same objects in two pictures. When thers is more than 80% points match, we can say two images have same objects. 

