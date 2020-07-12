import json
import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class ESCreateIndex:
    def __init__(self):
        pass
    # connect to ES on localhost on port 9200

    def create_indices(self):
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        if es.ping():
            print('Connected to ES!')
        else:
            print('Could not connect!')
            sys.exit()

        print("*********************************************************************************")


        # index in ES = DB in an RDBMS
        # Read each question and index into an index called questions
        # Indexing only titles for this example to improve speed. In practice, its good to index CONCATENATE(title+body)
        # Define the index


        # Refer: https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html
        # Mapping: Structure of the index
        # Property/Field: name and type  
        b = {"mappings": {
            "properties": {
                    "video_name": { "type": "text"},
                    "uc1_feature_vector": {"type": "binary"}
            }
            }
        }


        ret = es.indices.create(index='uc1_duplicatevideo_b', ignore=400, body=b) #400 caused by IndexAlreadyExistsException, 
        print(json.dumps(ret,indent=4))

        # TRY this in browser: http://localhost:9200/feature-index

        print("*********************************************************************************")