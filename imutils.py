import cv2
import numpy as np

def translate(image, x, y):
  M = np.float32([[1,0, x][0,1,y]])
  shifted = cv2.warpAffine(image, M, (image.shape[1],image.shape[0]) )
  return shifted

def rotate(image, deg, scale=1.0):
  (h, w) = image.shape[:2]  
  center = (w//2,h//2)
  M = cv2.getRotationMatrix2D(center, deg, scale)
  rotated = cv2.warpAffine(image, M, (w,h))

  return rotated
