#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('jungle.jpg',0)
plt.imshow(img)


# In[3]:


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum1 = np.abs(fshift)
phase_spectrum = np.angle(fshift)
cv.imwrite('magnitude_spectrum1.jpg', magnitude_spectrum1)
cv.imwrite('phase_spectrum.jpg', phase_spectrum)

plt.figure(figsize = (20,60))
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(phase_spectrum, cmap = 'gray')
plt.title('phase_spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(magnitude_spectrum1, cmap = 'gray')
plt.title('magnitude_spectrum1'), plt.xticks([]), plt.yticks([])
plt.show()


# In[ ]:




