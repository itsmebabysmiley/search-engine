from flask import Flask, render_template, request
import json
import math
import random


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('homepage.html')


@app.route('/search', methods=['GET'])
def search():
    page_size = 15
    keyword = request.args.get('keyword')

    if request.args.get('page'):
        page_no = int(request.args.get('page'))
    else:
        page_no = 1

    with open('sample_with_id.json', 'r') as myfile:
        data=myfile.read() 
    
    res = json.loads(data)
    result = []
    for r in res:
        # print(r['id'])
        img_list = [r['img_list'][i] for i in random.sample(range(0, 10), 3)]
        
        body = {
            'id':          r['id'],
            'name':        r['name'],
            'related name': r['related name'],
            'short_short_story':  str(r['short_story'][0:100])+"...",
            'short_story': r['short_story'],
            'characters':   r['characters'],
            'genres':      [c.capitalize() for c in r['genres']],
            'author':      r['author'],
            'publisher':   r['publisher'],
            'img':         img_list
        }
        result.append(body)

    page_total = math.ceil(len(res)/page_size)
    return render_template('search.html', res=result[page_no-1::page_total], page_total = page_total, page_no = page_no, keyword = keyword )


@app.route('/manga/<id>')
def manga_page(id):
    arg = id.split('=')
    id = arg[1]
    print(id)
    with open('sample_with_id.json', 'r') as myfile:
        data=myfile.read() 
    res = json.loads(data)
    
    index = 0
    for v in res:
        if v['id'] == id:
            break
        index += 1
    print(index)
    
    result = {
        'name':         res[index]['name'],
        'related name': '' if res[index]['related name'][0] == '' else ','.join(res[index]['related name']),
        'short_story':  res[index]['short_story'],
        'characters':   res[index]['characters'],
        'genres':       ','.join(c.capitalize() for c in res[index]['genres']) ,
        'author':       res[index]['author'],
        'publisher':    res[index]['publisher']
    }
    img = res[index]['img_list'][0]
    return render_template('manga_page.html',res = result, img = img)


if __name__ == '__main__':
    #hi nice to see u ><
    pass