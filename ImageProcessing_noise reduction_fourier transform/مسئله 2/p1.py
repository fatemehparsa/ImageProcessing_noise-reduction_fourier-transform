#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('peacock.jpg',0)
plt.imshow(img, cmap = 'gray')
###########


# In[36]:


######################  low pass filter test
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.log(np.abs(fshift)+1)
phase_spectrum = np.angle(fshift)
x,y=fshift.shape
mask=np.zeros((x,y))
center_coordinates = (int(y/2),int(x/2))
radius = 10
thickness = -1
color = 1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_magnitude_spectrum=magnitude_spectrum*mask
plt.imshow(new_magnitude_spectrum, cmap = 'gray')
#####################


# In[37]:


#low pass filter: you should set parametrs radius and thickness###########
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.zeros((x,y))
center_coordinates = (int(y/2),int(x/2))
color = 1
#
radius = 10
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back10= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))
#
mask=np.zeros((x,y))
radius = 20
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back20= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))
#
mask=np.zeros((x,y))
radius = 50
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back50= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

#
mask=np.zeros((x,y))
radius = 100
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back100= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

plt.figure(figsize = (20,60))
plt.subplot(151),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(img_back10, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back10'), plt.xticks([]), plt.yticks([])
plt.subplot(153),plt.imshow(img_back20, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back20'), plt.xticks([]), plt.yticks([])
plt.subplot(154),plt.imshow(img_back50, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back50'), plt.xticks([]), plt.yticks([])
plt.subplot(155),plt.imshow(img_back100, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back100'), plt.xticks([]), plt.yticks([])
plt.show()
########################################################################


# In[38]:


###################### high pass filter test
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.log(np.abs(fshift)+1)
phase_spectrum = np.angle(fshift)
x,y=fshift.shape
mask=np.ones((x,y))
center_coordinates = (int(y/2),int(x/2))
radius = 10
thickness = -1
color = 0
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_magnitude_spectrum=magnitude_spectrum*mask
plt.imshow(new_magnitude_spectrum, cmap = 'gray')
#####################


# In[39]:



#high pass filter: you should set parametrs radius and thickness###########
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.ones((x,y))
center_coordinates = (int(y/2),int(x/2))
color = 0
#
radius = 10
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back10= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))
#
mask=np.ones((x,y))
radius = 20
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back20= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))
#
mask=np.ones((x,y))
radius = 50
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back50= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

#
mask=np.ones((x,y))
radius = 100
thickness = -1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back100= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

cv.imwrite('img_back20.jpg', img_back20)

plt.figure(figsize = (20,60))
plt.subplot(151),plt.imshow(img, cmap = 'gray', vmin=0, vmax=255)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(img_back10, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back10'), plt.xticks([]), plt.yticks([])
plt.subplot(153),plt.imshow(img_back20, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back20'), plt.xticks([]), plt.yticks([])
plt.subplot(154),plt.imshow(img_back50, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back50'), plt.xticks([]), plt.yticks([])
plt.subplot(155),plt.imshow(img_back100, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back100'), plt.xticks([]), plt.yticks([])
plt.show()
########################################################################


# In[43]:


###################### band pass filter test
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.log(np.abs(fshift)+1)
phase_spectrum = np.angle(fshift)
x,y=fshift.shape
mask=np.zeros((x,y))
center_coordinates = (int(y/2),int(x/2))
radius = 52
thickness = 35
color = 1
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_magnitude_spectrum=magnitude_spectrum*mask
plt.imshow(new_magnitude_spectrum, cmap = 'gray')
#####################


# In[46]:



#band pass filter: you should set parametrs radius and thickness###########
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
x,y=fshift.shape
mask=np.zeros((x,y))
center_coordinates = (int(y/2),int(x/2))
color = 1
#
radius = 52
thickness = 35
mask = cv.circle(mask, center_coordinates, radius, color, thickness)
new_fshift=fshift*mask
img_back= np.real(np.fft.ifft2(np.fft.ifftshift(new_fshift)))

plt.figure(figsize = (20,60))
plt.subplot(151),plt.imshow(img, cmap = 'gray', vmin=0, vmax=255)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(img_back, cmap = 'gray', vmin=0, vmax=255)
plt.title('img_back'), plt.xticks([]), plt.yticks([])

plt.show()
########################################################################


# In[ ]:




