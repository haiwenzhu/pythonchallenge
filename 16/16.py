#http://www.pythonchallenge.com/pc/return/mozart.html

import Image
import sys 

if __name__ == '__main__':
    im = Image.open('mozart.gif')
    width = im.size[0]
    height = im.size[1]
    data = list(im.getdata())
    new_im = Image.new(im.mode, im.size)
    for h in range(height):
        i = h * width
        j = i + width
        idx = data[i:j].index(195)
        data[i:j] = data[i+idx:j] + data[i:i+idx]
        #data[i:i+width-idx] = tmp[idx:]
        #data[i+width-idx:j] = tmp[0:idx]
    new_im.putdata(data)
    new_im.show()
