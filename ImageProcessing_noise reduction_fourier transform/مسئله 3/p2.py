#!/usr/bin/env python
# coding: utf-8

# In[118]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('man.jpg',0)
plt.imshow(img, cmap = 'gray')


# In[119]:


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.log(np.abs(fshift)+1)

plt.imshow(magnitude_spectrum, cmap = 'gray')


# In[124]:


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.ones((x,y))
center_coordinates = (int(y/2),100)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),220)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),15)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),38)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),305)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),282)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)


new_fshift=fshift*mask
magnitude_spectrum = np.log(np.abs(new_fshift)+1)
plt.imshow(magnitude_spectrum, cmap = 'gray')


# In[ ]:





# In[123]:



f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.ones((x,y))
center_coordinates = (int(y/2),100)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),220)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),15)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),38)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),305)
color = 0
radius = 17
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)

center_coordinates = (int(y/2),282)
color = 0
radius = 17
thickness = -1
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





# In[ ]:




