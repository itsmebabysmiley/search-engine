from serpapi import GoogleSearch
import json


def craw():
  f = open("track_id_name.json", 'r')
  o = open('image_link.json', "a")
  data = json.load(f)

  o.write('[')
  for i in data[96:103]:
    params = {
      "q": i['name'],
      "tbm": "isch",
      "ijn": "0",
      "api_key": "4dda25b6f4a662219104a4357fd004ff2937bb8ec8e28c60a7e5c1d13a6b1090"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']
    img_list = []
    for field in images_results:
      img =field['thumbnail']
      img_list.append(img)
    
    body = {
      'name' : i['name'],
      'img_list' : img_list[0:10]
    }
    o.write(json.dumps(body))
    o.write(',')
  o.write(']')

  o.close()
  f.close()

def check_number():
  f = open("track_id_name.json", 'r')
  data = json.load(f)
  c = 0
  for i in data:
    if i['name'] == 'Doraemon':
     print(c)
     break
    c+=1
    
  f.close()
  
  
if __name__ == '__main__':
  # check_number()
  # De__12k222
  craw()