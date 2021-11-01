from flask import Flask
from flask import render_template
from elasticsearch import Elasticsearch
from werkzeug.wrappers import response

# es = Elasticsearch()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('homepage.html')


@app.route("/search")
def search():
    body = {
        'size' : '10',
        'query' : {
            "match_all" : {}
        }
    }
    # res = es.search(index="",body=body)
    '''
    continue...
    '''
    return render_template('search.html',)
    
    
    

if __name__ == '__main__':
    app.run(debug=True)
