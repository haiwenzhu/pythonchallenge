# http://www.pythonchallenge.com/pc/def/oxygen.html

import Image
import re

im = Image.open('oxygen.png')

x = 0
y = 0
res = ''
while y < im.size[1]:
    p = im.getpixel((0, y))
    if p[0] == p[1] and p[1] == p[2]:
        break
    y += 1

while x < im.size[0]:
    p = im.getpixel((x, y))
    if p[0] == p[1] and p[1] == p[2]:
        res += chr(p[0])
    x += 7

print(res)
print(''.join([chr(int(i)) for i in re.findall('\d+', res)]))
