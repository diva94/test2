import os
from datetime import datetime
#import pysnooper
#with pysnooper.snoop(depth=2):
t = input()
os.system("ffmpeg -i Assignment_firefighter1.mp4 -vf select='eq(pict_type\,I)' -vsync 2 -s 160x90 -f image2 images/thumbnails-%02d.jpeg")
os.system(f"ffmpeg -framerate 1 -pattern_type glob -i 'images/*.jpeg' -ss 30 -t {t} -c:v libx264 -c:a copy -shortest -r 30 -pix_fmt yuv420p firefighter.mp4")
