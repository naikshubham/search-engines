import numpy as np
from elasticsearch import Elasticsearch
from indexES import ESCreateIndex

class ReadES:
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        if self.es.ping():
            print('Connected to ES!')
        else:
            print('Could not connect!')
            sys.exit()

        print("*********************************************************************************")

    def read_es(self):
        res = self.es.get(index="uc1_duplicatevideo_b", id=1)
        # print(res['_source']['uc1_feature_vector'][:20])
        # print(type(res['_source']['uc1_feature_vector']))        
        # v1 = bytes(res['_source']['uc1_feature_vector'], 'utf-8')

    def DuplicateSearch(self, q):
        #Search by Keywords
        b={
                'query':{
                    'match':{
                        "video_name":q
                        # "boost":1.0
                    }
                }
            }
        # b = {"size": 1,
        #         "query" : {
        #                 "script_score" : {
        #                     "query" : {
        #                         "match_all": {}
        #                     },
        #                     "script" : {
        #                         "source": "cosineSimilarity(params.query_vector, 'uc1_feature_vector') + 1.0", 
        #                         "params": {"query_vector": q}
        #                     }
        #                 }
        #             }
        #         }



        res= self.es.search(index='uc1_duplicatevideo_b',body=b)
        print("Keyword Search:\n")
        for hit in res['hits']['hits']:
            print(str(hit['_score']) + "\t" + hit['_source']['video_name'])

        print("*********************************************************************************")

        # return

reades = ReadES()
reades.read_es()
with open("video.mp4", "rb") as file:
    y = file.read()
    # x = np.frombuffer(y, np.uint8)
    x = list(y)
    # print(type(x), x[:10])
# reades.DuplicateSearch(x)
reades.DuplicateSearch('video')

