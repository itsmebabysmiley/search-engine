from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import json
import math

es = Elasticsearch()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('homepage.html')


@app.route('/search', methods=['GET'])
def search():
    page_size = 10
    keyword = request.args.get('keyword')
    
    if request.args.get('page'):
        page_no = int(request.args.get('page'))
    else:
        page_no = 1
        
    body = {
        'size' : page_size,
        'from' : page_size * (page_no-1),
         'query': {
            'multi_match': {
                'query': keyword,
                'fields': ['name','short_story','characters','genres']
            }
        }
    }

    res = es.search(index='magna_index', doc_type='', body=body)
    result = []
    for r in res['hits']['hits']:
        
        body ={
            'name' :        r['_source']['name'],
            'related name': r['_source']['related name'],
            'short_story':  r['_source']['short_story'],
            'characters':   r['_source']['characters'],
            'genres' :     [c.capitalize() for c in r['_source']['genres']],
            'author' :      r['_source']['author'],
            'publisher' :   r['_source']['Publisher']
        }
        result.append(body)
    
    # json_formatted_str = json.dumps(result, indent=2)
    # print(json_formatted_str)
    page_total = math.ceil(res['hits']['total']['value']/page_size)
    return render_template('search.html', res=result, page_total = page_total, page_no = page_no, keyword = keyword )
    
    
    

if __name__ == '__main__':
    app.run(debug=True)
