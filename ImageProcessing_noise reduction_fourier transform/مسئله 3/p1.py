#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('city.jpg',0)
plt.imshow(img, cmap = 'gray')


# In[3]:


###################### magnitude check
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.log(np.abs(fshift)+1)

plt.imshow(magnitude_spectrum, cmap = 'gray')
#####################


# In[36]:



f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.zeros((x,y))
center_coordinates = (int(y/2),int(x/2))
color = 5
radius = 100
thickness = 3
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back100= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

plt.figure(figsize = (20,60))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back100, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back100'), plt.xticks([]), plt.yticks([])
plt.show()


# In[30]:


f = np.fft.fft2(img_back100)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.log(np.abs(fshift)+1)
plt.imshow(magnitude_spectrum, cmap = 'gray')


# In[ ]:





# In[39]:


img = cv.imread('city.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.ones((x,y))
center_coordinates = (int(y/2),int(x/2))
color = 0
radius = 100
thickness = 3
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back100= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

plt.figure(figsize = (20,60))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back100, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back100'), plt.xticks([]), plt.yticks([])
plt.show()


# In[ ]:




