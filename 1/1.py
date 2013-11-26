# http://www.pythonchallenge.com/pc/def/map.html
import string

hint_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_str = ''

for key in hint_str:
    #hint_str = hint_str.replace(key, letter_map[key])
    if key.isalpha():
        if ord(key)+2 > 122:
            new_str += chr(ord(key) - 24) # ord(key) + 2 - 26
        else:
            new_str += chr(ord(key)+2)
    else:
        new_str += key

print(new_str)

#use string.maketrans
print(string.translate(hint_str, string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))
print(string.translate('map', string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))
