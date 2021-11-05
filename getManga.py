from elasticsearch import Elasticsearch
import json
es = Elasticsearch()


def search():
    out_file = open('track_id_name.json', "x")
    out_file.write('[')
    body = {
        'size': 103,
        "query": {
            "match_all": {}
        }
        
    }
    res = es.search(index='manga_index', doc_type='', body=body)
    
    result = []
    for r in res['hits']['hits']:
        body = {
            'name' :r['_source']['name'],
            'id' : r['_id']
        }
        out_file.write(json.dumps(body))
        out_file.write(',')
    out_file.write(']')
    out_file.close()
        

if __name__ == '__main__':
    search()
    # print(json.dumps(tep, indent=4))
