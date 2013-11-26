# http://www.pythonchallenge.com/pc/return/bull.html
import re

# 11 means the previous number 1 is conposed by one number 1
# 21 means the previous number 21 is conposed by tow number 1
# 1211 means the previous number 21 is conposed by one number 2 and one number 1
# 111221 means the previous number 1121 is conposed by one number 2 and one number 2 and two number 1
a = [1, 11, 21, 1211, 111221]
while len(a) != 31:
    num = str(a[len(a)-1])
    res = re.findall(r'((\d)\2*)', num)
    a.append(''.join([str(len(item[0])) + item[1] for item in res]))
print(len(a[30]))
