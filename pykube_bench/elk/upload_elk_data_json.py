import json
from datetime import datetime
# connect to our cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Specify your parameters here
FILE_PATH = "template/pods_data.json"
INDEX = "json_index"
DOC_TYPE = "json_doc_type"

# Read data from file
data = json.loads(open(FILE_PATH).read())
data['timestamp'] = datetime.now()
# Upload data to elastic search server
if isinstance(data, dict):    # JSON Object
    es.index(index=INDEX, doc_type=DOC_TYPE, body=data)
else:    # JSON Array
    for record in data:
        es.index(index=INDEX, doc_type=DOC_TYPE, body=record)