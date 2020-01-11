import cv2
import torch
import  numpy as np
img = cv2.imread("./test.jpg")
print(img.shape)

# COLORMAP_AUTUMN = 0,
# COLORMAP_BONE = 1,
# COLORMAP_JET = 2,
# COLORMAP_WINTER = 3,
# COLORMAP_RAINBOW = 4,
# COLORMAP_OCEAN = 5,
# COLORMAP_SUMMER = 6,
# COLORMAP_SPRING = 7,
# COLORMAP_COOL = 8,
# COLORMAP_HSV = 9,
# COLORMAP_PINK = 10,
# COLORMAP_HOT = 11

CAM = np.random.normal(0,1,size=())
heatmap = cv2.applyColorMap(cv2.resize(CAM,(width,height)),cv2.COLORMAP_JEF) #COLORMAP_JET
result =heatmap*0.3+img*0.5
cv2.imshow('CAM.jpg',result)
