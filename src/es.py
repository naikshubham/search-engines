from datetime import datetime
from elasticsearch import Elasticsearch
from indexES import ESCreateIndex
import cv2
import numpy as np
import os
import sys
import json
import glob
# cap_1 = cv2.VideoCapture('v1.mp4')
# cap_2 = cv2.VideoCapture('v2.mp4')
# frame_1 = [frame for frame in cap_1.read()]
# frame_2 = [frame for frame in cap_2.read()]

# video_names = ["v1.mp4", "v2.mp4"]
# frames = np.array([frame_1, frame_2])
# for ele in frames[0]:
#     print(ele)
# a_bytes = frames.tostring()
# print(type(a_bytes))
# print(a_bytes)
# a2 = np.fromstring(a_bytes, dtype=frames.dtype)
# print("After loading, content of the text file:")
# print(type(a2))
# print(np.array_equal(frames, a2))


# with open("v1.mp4", "rb") as file:
#     y = file.read()

class IndexES:
    def __init__(self):
        pass

    def create_features(self):
        base_path = 'videos/'
        video_names = []
        videos = []
        for video in glob.glob(base_path+os.sep+'*.*'):
            video_name = video.split('/')[-1].split('.')[0]
            video_names.append(video_name)
            with open(video, "rb") as file:
                x = file.read()
                x = np.frombuffer(x, np.uint8).tolist()
                # print(type(x))
                videos.append(x)
        return video_names, videos

    def index_es(self):
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        if es.ping():
            print('Connected to ES!')
        else:
            print('Could not connect!')
            sys.exit()

        print("*********************************************************************************")
        c=0
        video_names, videos = self.create_features()

        # vi = []
        # for v in videos:
        #     if b'\n' in v:
        #         v = v.replace(b'\n', b'')
        #         vi.append(v)

        for video_name, frame in zip(video_names, videos):
            # print(video_name,type(frame))
            b = {"video_name":video_name,
                "uc1_feature_vector":frame, #.decode('latin1'),
                }	
                    #print(json.dumps(tmp,indent=4))		
            # b = json.dumps(b)
            # print(type(b))
            res = es.index(index="uc1_duplicatevideo_b", id=c, body=b)
            c+=1
            print('res->', res)
        print("Indexing completed")

if __name__ == "__main__":
    createindex_obj = ESCreateIndex()
    createindex_obj.create_indices()
    index_obj = IndexES()
    index_obj.index_es()



