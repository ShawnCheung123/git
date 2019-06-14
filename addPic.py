import cv2
import numpy as np
for i in range(27*25+15,30*25):
    img1 = cv2.imread('/home/d201/shenzhenProject/result/'+str(i)+'.jpg')
    img2 = cv2.imread('/home/d201/shenzhenProject/code/finalPSPic/5.png')

    #img2 = cv2.resize(img2,(100,100))
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols]

    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)

    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst

    cv2.imwrite('/home/d201/shenzhenProject/resultV2/'+str(i)+'.jpg',img1)
