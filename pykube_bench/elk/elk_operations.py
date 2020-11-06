import json
from datetime import datetime

from elasticsearch import Elasticsearch

es_host = 'localhost'
es_port = 9200


class ELkOperations:
    """
    This class is responsible for ELK operations
    """

    def __init__(self):
        self.es = Elasticsearch([{'host': es_host, 'port': es_port}])

    def upload_json_to_es(self, json_file, index, doc_type):
        """
        This method is upload json kubernetes cluster data into elasticsearch
        :param json_file:
        :param index:
        :param doc_type:
        :return:
        """

        # Read data from file
        data = json.loads(open(json_file).read())
        # utcnow - solve timestamp issue
        data['timestamp'] = datetime.utcnow() #datetime.now()

        # Upload data to elastic search server
        try:
            if isinstance(data, dict):    # JSON Object
                self.es.index(index=index, doc_type=doc_type, body=data)
            else:    # JSON Array
                for record in data:
                    self.es.index(index=index, doc_type=doc_type, body=record)
            return True
        except Exception:
            raise

    def is_es_index_exist(self, index):
        """
        This method verify that input index exist in elasticsearch
        :param index:
        :return:
        """
        try:
            result = self.es.search(index=index, body={"query": {"match_all": {}}})
            return result
            # print("Got %d Hits:" % res['hits']['total']['value'])
            # for hit in res['hits']['hits']:
            #     print("%(_timestamp)s %(openshift)s: %(node1)s" % hit["_source"])
        except Exception:
            raise

        def delete_index_document(index, document):
            """
            This method delete a document id according to index
            :param index:
            :param document:
            :return:
            """
            # @todo - convert to python DELETE /json_index/_doc/RGY_mXUBjd1J4k9bu3qX
            pass
