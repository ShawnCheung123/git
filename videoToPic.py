import cv2
import argparse
parser = argparse.ArgumentParser(description = 'in and out')
parser.add_argument('--fileIn', type = str, default = './origin.jpg')
parser.add_argument('--fileOut', type=str, default = './result.jpg')
parser.add_argument('--startFrame', type=int, default = 0)
parser.add_argument('--endFrame', type=int, default = 99999999)
args = parser.parse_args()

video = cv2.VideoCapture(args.fileIn)
c = args.startFrame
if video.isOpened():
    rval,frame = video.read()
else:
    rval = False
while rval:
    rval,frame = video.read()
    if c % 1 == 0:
        cv2.imwrite(args.fileOut + str(c) + '.jpg', frame)
    c += 1
    if c > args.endFrame:
        break
    print(c)
