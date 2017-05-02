from Hatena import Hatena
from tinydb import TinyDB
db = TinyDB("db.json")

bots = db.all()

for bot in bots:
    hatena = Hatena(username=bot['username'],password=bot['password'],proxyserver=bot['proxyserver'])
    hatena.bookmark(url='https://www.youtube.com/watch?v=c-L8Fm0kke0')
    hatena.close()
