#http://www.pythonchallenge.com/pc/def/channel.html

from zipfile import ZipFile, ZipInfo
import re

nothing_id = '90052'
zip_file = ZipFile('channel.zip', 'r')
comment = ''
while True:
    content = zip_file.read(nothing_id + '.txt')
    comment += zip_file.getinfo(nothing_id + '.txt').comment
    m = re.search(r'Next nothing is (\d+)$', content)
    if m:
        nothing_id = m.group(1)
    else:
        if content == 'Yes. Divide by two and keep going.':
            nothing_id = str(int(nothing_id)/2)
        else:
            print(content)
            break

print(comment)
