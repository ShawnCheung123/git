import cv2
import os
import argparse
parser = argparse.ArgumentParser(description = 'in and out')
parser.add_argument('--fileIn',type = str,default = './origin.jpg')
parser.add_argument('--fileOut',type = str,default = './result.wmv')
parser.add_argument('--fps', type = int, default = 24)
parser.add_argument('--length', type = int, default = 1920)
parser.add_argument('--hight', type = int, default = 1080)
args=parser.parse_args()


fps = args.fps
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
video_writer = cv2.VideoWriter(filename = args.fileOut, fourcc = fourcc, fps = fps, frameSize = (args.length, args.hight))
for i in range(0,99999999):
    p = i
    if os.path.exists(args.fileIn + str(p) + '.jpg'):
        img = cv2.imread(filename = args.fileIn + str(p) + '.jpg')
        video_writer.write(img)
        print(str(p) + '.jpg' + 'done!')
video_writer.release()
