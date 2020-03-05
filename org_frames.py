# Imports
from __future__ import print_function
import numpy as np
import os
import gc
import itertools
import argparse
import subprocess
import shutil

gc.enable()

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--stride", type=float, required=True, help="stride between frames")
ap.add_argument("-l", "--length", type=float, required=True, help="length of videos in frames")
ap.add_argument("-m", "--marker", type=str, required=True, help="marker for video sequence")
args = vars(ap.parse_args())

stride = args["stride"]
vid_len = args["length"]
marker = args["marker"]

filetype = '.png'

imgs = []
cwd = os.getcwd()

for file in os.listdir(cwd):
    if file.endswith(filetype):
        imgs.append(file)
        
imgs = sorted(imgs)

imgs_len = len(imgs)
	
num_of_vids = int(np.floor((imgs_len - vid_len) / stride))
        
if not os.path.exists('videos'):
    os.makedirs('videos')

for vid in range(0, num_of_vids):

    new_folder = 'frames'
        
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
		
    vid_imgs = imgs[int(stride*vid):int((stride*vid)+vid_len)]
	
    i = 0
	
    vidname = marker + '_' + str(vid+1)
		
    for file in vid_imgs:
        
        i = i + 1
	
        img = cv2.imread(file)

        cv2.imwrite(new_folder + '/' + str(i) + '.png', img)
		
    os.chdir(cwd + '/' + new_folder)
		
    subprocess.check_call('ffmpeg -r 14 -i %1d.png -vcodec libx264 -pix_fmt yuv420p -crf 28 -an ' + vidname + '.mp4', shell=True)
		
    os.chdir(cwd)
	
    shutil.move(cwd + '/' + new_folder + '/' + vidname + '.mp4', cwd + '/videos/' + vidname + '.mp4')
	
    shutil.rmtree(os.path.join(cwd, new_folder), ignore_errors = True)