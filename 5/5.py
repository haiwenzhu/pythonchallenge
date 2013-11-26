#http://www.pythonchallenge.com/pc/def/peak.html
import cPickle

for item in cPickle.load(open('level5.input')):
        print(''.join([t[0]*t[1] for t in item]))
