# Download image
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('dog.jpeg')
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2  # Your code here
mpimg.imsave("dog_grey.jpeg", gray_img_01, cmaFp="gray")
print(gray_img_01[0, 0])
