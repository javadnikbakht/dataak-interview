from elasticsearch import Elasticsearch

elasticsearch_host = "localhost"
elasticsearch_port = 9200
index_name = "dataak_index"

elastic = Elasticsearch(hosts=[{"host": elasticsearch_host, "port": elasticsearch_port, "scheme": "http"}])