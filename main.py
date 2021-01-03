from os import system
from cv2 import VideoCapture, CAP_PROP_FPS
import argparse

parser = argparse.ArgumentParser(description='Turns a video file into a load of images')
parser.add_argument('--filepath', type=str, help='where the video file you want to turn into images')
args = parser.parse_args()
filepath = args.filepath
if filepath is None:
    print('Filepath argument is required')
else:
    fps = VideoCapture(filepath).get(CAP_PROP_FPS)
    if fps == 0.0:
        print('Could not determine the fps from this file\nDouble check the input file')
    else:
        system('ffmpeg -i {} -vf fps={} -vsync 0 ./output/out%d.png'.format(filepath, fps))
