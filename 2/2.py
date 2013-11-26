# http://www.pythonchallenge.com/pc/def/ocr.html

fp = open("2.input")
str = fp.read()
charset = set(str)
res = {} 
res_str = ''
for c in charset:
    if str.count(c) < 10:
        res[str.index(c)] = c
for idx in sorted(res):
    res_str += res[idx]
print(res_str)
