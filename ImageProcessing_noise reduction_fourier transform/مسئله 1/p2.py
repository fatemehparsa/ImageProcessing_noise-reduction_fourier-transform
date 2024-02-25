#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# In[2]:


img = cv.imread('jungle.jpg',0)
plt.imshow(img)


# In[4]:


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum1 = np.abs(fshift)
magnitude_spectrum2 = np.log(np.abs(fshift)+1)
cv.imwrite('magnitude_spectrum1.jpg', magnitude_spectrum1)
cv.imwrite('magnitude_spectrum2.jpg', magnitude_spectrum2)

plt.figure(figsize = (20,60))
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum1, cmap = 'gray')
plt.title('Magnitude 1'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(magnitude_spectrum2, cmap = 'gray')
plt.title('Magnitude 2'), plt.xticks([]), plt.yticks([])
plt.show()


# In[ ]:




