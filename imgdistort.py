import skimage
from scipy import *
from scipy import ndimage
from skimage import data
from skimage import filters
import os
# filename = os.path.join(skimage.data_dir, './test.png')
from skimage import io
moon = io.imread('test.png')

import matplotlib.pyplot as plt
from scipy import misc
import numpy as np

moon[150:170] = 200
#moon=moon + 0.4 * moon.std() * np.random.random(moon.shape)

#moon[range(400), range(400)] = 240


blurred_face = ndimage.gaussian_filter(moon, sigma=5)#change value of sigma to change the level of blur
blurred_face= ndimage.rotate(blurred_face, 30)#change value of angle



#very_blurred = ndimage.gaussian_filter(moon, sigma=5)
print blurred_face.shape
plt.imshow(blurred_face)
plt.show()