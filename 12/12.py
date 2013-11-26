# http://www.pythonchallenge.com/pc/return/evil.html

#output is images
with open('evil2.gfx', 'rb') as fp:
    content = fp.read()
    for id in range(5):
        wp = open(str(id), 'wb')
        wp.write(content[id::5])
