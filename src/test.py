
import os
import difflib
import numpy as np
import glob

# with open("F:/LTI/Video_Deduplication/UC_6/Data/med_lab_01.mp4", "rb") as file:
#     x = file.read()

# with open("F:/LTI/Video_Deduplication/UC_6/Data/med_lab_01.mp4", "rb") as file:
#     y = file.read()

base_path = 'Videos/'
video_names = []
videos = []
for video in glob.glob(base_path+os.sep+'*.*'):
    video_name = video.split('/')[-1].split('.')[0]
    video_names.append(video_name)
    with open(video, "rb") as file:
        x = file.read()
        videos.append(x)
vi = []
for v in videos:
    if b'\n' in v:
        v = v.replace(b'\n', b'')
        vi.append(v)
for v in vi:
    if b'\n' in v:
        # v = v.replace(b'\n', b'')
        print('true')

# print([type(v) for v in videos])

# v1 = np.frombuffer(x, np.uint8)
# v2 = np.frombuffer(y, np.uint8)

# print(np.array_equal(v1, v2)) 