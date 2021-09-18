import cv2
import numpy as np
import glob
 
img_array = []
for filename in sorted(glob.glob('/home/rafael/Documentos/DL-artigo/PaintTransformer/inference/output/michael_scott/*.png')):
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('michael_scott.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 5, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()