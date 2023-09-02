# Computer Vision - Dot Recognition
A computer vision program for determining the number of celestial bodies in a photograph.

## How does the program work ?

- Load image for analysis, then convert to grayscale
- Pixel dilation to distinguish glued dots (with Numpy)
- Dot detection with OpenCV's Canny algorithm
- Store all dot coordinates in the variable \<contours>
- Number of dots = cardinal of the set contained in the variable \<contours>

## Constraints

- The program does not yet recognize when two dots overlap
- Dense, bright areas can distort results

## How to use the program ?

- Download the files (main.py and image.jpg) in the same repository
- Launch the program with Python (python/py main.py)

## Upcoming improvements 

- Machine Learning 

## Credits 

- Photography by [Samuel Richard](https://unsplash.com/fr/@mumbolicious)

