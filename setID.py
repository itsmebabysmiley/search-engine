import json

f = open("sample.json", "r")

res = json.load(f)

f.close()

fo = open("sample_with_id.json", 'a')
fo.write('[')
count = 1
for r in res:
    r['id'] = r['name'][0]+str(count)
    count += 1
    fo.write(json.dumps(r))
    fo.write(',')
    
fo.write(']')
fo.close()