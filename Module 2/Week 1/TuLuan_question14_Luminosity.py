# Download image
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('dog.jpeg')
gray_img_01 = 0.21*img[:, :, 0] + 0.72*img[:, :, 1] + 0.07*img[:, :, 2]  # Your code here
mpimg.imsave("dog_grey.jpeg", gray_img_01, cmaFp="gray")
print(gray_img_01[0, 0])
