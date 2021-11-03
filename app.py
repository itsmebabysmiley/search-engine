from flask import Flask, render_template, request
import json
import math


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
    
    with open('sample.json', 'r') as myfile:
        data=myfile.read()   

    res = json.loads(data)
    result = []
    for r in res:
        
        body ={
            'name' :        r['name'],
            'related name': r['related name'],
            'short_story':  r['short_story'],
            'characters':   r['characters'],
            'genres' :     [c.capitalize() for c in r['genres']],
            'author' :      r['author'],
            'publisher' :   r['Publisher']
        }
        result.append(body)
    
    # json_formatted_str = json.dumps(result, indent=2)
    # print(json_formatted_str)
    page_total = math.ceil(len(res)/page_size)
    return render_template('search.html', res=result[page_no::page_total], page_total = page_total, page_no = page_no, keyword = keyword )
    
    
    

if __name__ == '__main__':
    app.run(debug=True)
