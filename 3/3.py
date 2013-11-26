# http://www.pythonchallenge.com/pc/def/equality.html
import re

str = open('level3.input').read()
print(''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', str)))
