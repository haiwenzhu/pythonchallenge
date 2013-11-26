# http://www.pythonchallenge.com/pc/return/5808.html

import Image

im = Image.open('cave.jpg')
odd = even = Image.new(im.mode, (im.size[0], im.size[1]))
data = list(im.getdata())
for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        if x % 2 == y % 2 :  
            odd.putpixel((x/2, y/2), data[x + y*im.size[0]])  
        else:  
            even.putpixel((x/2, y/2), data[x + y*im.size[0]])  

odd.save('odd.jpg', 'jpeg')
even.save('even.jpg', 'jpeg')
