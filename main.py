from Hatena import Hatena
from tinydb import TinyDB
db = TinyDB("db.json")


print "Please type bookmark URL"
type_url = raw_input()
print "I will bookmark \n {}.\nOK? y/n".format(type_url)
type_bool = raw_input()
if type_bool == 'y':
    URL = type_url
    bots = db.all()
    for bot in bots:
        hatena = Hatena(username=bot['username'],password=bot['password'],proxyserver=bot['proxyserver'])
        hatena.bookmark(url=URL)
        hatena.close()
else:
    pass
