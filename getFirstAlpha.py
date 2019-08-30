from pypinyin import pinyin, Style
import demjson

def getStrFirstAplha(str):
    return pinyin(str, style=Style.FIRST_LETTER)[0][0].upper()
f = open('./area.json','r')
jsonDecode = demjson.decode(f.read())
i=1
for item in jsonDecode:
    print(i)
    item['first'] = getStrFirstAplha(item['name'])
    i+=1


nf = open('./areaWithFirstAlpha.json','w')
nf.write(demjson.encode(jsonDecode))
nf.close


