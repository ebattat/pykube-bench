from pykube_bench.elk.elk_operations import ELkOperations


def test_upload_json_to_es_461():
    """
    This test upload json to elasticsearch
    :return:
    """
    elk_operations = ELkOperations()
    json_file = 'template/kube_cluster_data_os_461.json'
    index = 'json_index'
    doc_type = 'json_doc_type'
    assert elk_operations.upload_json_to_es(json_file=json_file, index=index, doc_type=doc_type)


def test_upload_json_to_es_462():
    """
    This test upload json to elasticsearch
    :return:
    """
    elk_operations = ELkOperations()
    json_file = 'template/kube_cluster_data_os_462.json'
    index = 'json_index'
    doc_type = 'json_doc_type'
    assert elk_operations.upload_json_to_es(json_file=json_file, index=index, doc_type=doc_type)


def test_upload_json_to_es_361():
    """
    This test upload json to elasticsearch
    :return:
    """
    elk_operations = ELkOperations()
    json_file = 'template/linux_timestamp_361.json'
    index = 'json_linux_timestamp_index'
    doc_type = 'json_doc_type'
    assert elk_operations.upload_json_to_es(json_file=json_file, index=index, doc_type=doc_type)


def test_upload_json_to_es_362():
    """
    This test upload json to elasticsearch
    :return:
    """
    elk_operations = ELkOperations()
    json_file = 'template/linux_timestamp_362.json'
    index = 'json_linux_timestamp_index'
    doc_type = 'json_doc_type'
    assert elk_operations.upload_json_to_es(json_file=json_file, index=index, doc_type=doc_type)


def test_is_es_index_exist():
    """
    This test verify if index exist in elasticsearch
    :return:
    """
    index = 'json_index'
    elk_operations = ELkOperations()
    assert elk_operations.is_es_index_exist(index=index)


def test_delete_es_index():
    """
    This test delete index from elasticsearch
    :return:
    """
    pass
