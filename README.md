# spotting_spider_monkeys
Python script to generate 14 fps videos for the Zooniverse Spotting Spider Monkeys project for British Science Week.

The function executes within the current work directory and converts all Flirpy '.png' frames into 14 fps videos with three arguments: length indicating the number of frames per video (for this project 140 = 10s), stride indicating the overlap between videos in frames (for this project 28 = 2s) and a marker to identify the final video names.

The output is a subfolder named videos containing N videos (computed by N = (F - L) / S where F = number of png image frames, L = length argument and S = stride argument). The videos are named using the marker argument with the names: MARKER_n where n is the video number from 1 to N.