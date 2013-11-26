# http://www.pythonchallenge.com/pc/return/italy.html

import Image
im = Image.open('wire.png')
im_new = Image.new(im.mode, (100, 100))
data = list(im.getdata())
idx = 0
x = y = top = left = 0
bottom = right = 99
direction = 'R' # R=right, L=left, D=down, U=up
while idx < 10000:
    im_new.putpixel((x,y), data[idx])
    idx += 1
    if direction == 'R':
        if x == right:
            top += 1
            y += 1
            direction = 'D'
        else:
            x += 1
    elif direction == 'D':
        if y == bottom:
            right -= 1
            x -= 1
            direction = 'L'
        else:
            y += 1
    elif direction == 'L':
        if x == left:
            bottom -= 1
            y -= 1
            direction = 'U'
        else:
            x -= 1
    elif direction == 'U':
        if y == top:
            left += 1
            x += 1
            direction = 'R'
        else:
            y -= 1
im_new.show()
