#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('jungle.jpg',0)
plt.imshow(img)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

backimage1=np.real(np.fft.ifft2(fshift))
backimage2=np.real(np.fft.ifft2(np.fft.ifftshift(fshift)))


plt.figure(figsize = (20,60))
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(backimage1, cmap = 'gray')
plt.title('p3_backimage1'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(backimage2, cmap = 'gray')
plt.title('p3_backimage2'), plt.xticks([]), plt.yticks([])
plt.show()


# In[ ]:




