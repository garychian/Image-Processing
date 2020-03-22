#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


#read image
img1 = cv2.imread('shanghai tower 1.jpg')
img2 = cv2.imread('shanghai center 3.jpg')
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)


# In[25]:


#key point 
sift = cv2.xfeatures2d.SIFT_create()
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

#number of keypoints, if match 80%, we say we found they are same
len(keypoints_1),len(keypoints_2)


# In[26]:


img1 = cv2.drawKeypoints(gray1,keypoints_1,img1)
img2 = cv2.drawKeypoints(gray2,keypoints_2,img2)

figure, ax = plt.subplots(1,2,figsize=(16,8))
ax[0].imshow(img1, cmap='gray')
ax[1].imshow(img2, cmap='gray')


# In[27]:


#feature matching 
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50],img2, flags = 2)
plt.imshow(img3),plt.show()


# In[ ]:




