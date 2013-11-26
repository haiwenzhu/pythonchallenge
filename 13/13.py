#http://www.pythonchallenge.com/pc/return/disproportional.html
from xmlrpclib import ServerProxy

server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
#print(server.system.listMethods())
#http://www.pythonchallenge.com/pc/return/evil4.jpg said Bert is evil!
print(server.phone('Bert'))
