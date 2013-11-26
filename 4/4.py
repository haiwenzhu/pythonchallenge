#http://www.pythonchallenge.com/pc/def/linkedlist.html
import urllib
import re

url_prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing_id = '11631'
while True:
    fp = urllib.urlopen(url_prefix + nothing_id)
    response = fp.read()
    print(url_prefix + nothing_id)
    print(response)
    m = re.search(r'next nothing is (\d+)$', response)
    if m:
        nothing_id = m.group(1)
    else:
        if response == 'Yes. Divide by two and keep going.':
            nothing_id = str(int(nothing_id)/2)
        else:
            print(response)
            break
