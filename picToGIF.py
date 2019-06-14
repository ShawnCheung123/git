import imageio
import argparse
parser = argparse.ArgumentParser(description = 'in and out')
parser.add_argument('--fileIn', type = str, default = './origin.jpg')
parser.add_argument('--fileOut', type = str, default = './result.gif')
parser.add_argument('--fps', type = int, default = 25)
args=parser.parse_args()

frames=[]
for i in range(0,9999999):
    frames.append(imageio.imread(args.fileIn + str(i) + '.jpg'))
imageio.mimsave(args.fileOut, frames, 'GIF', duration = 1/args.fps)
