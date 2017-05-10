from Hatena import Hatena
from Register import Register
from tinydb import TinyDB
import sys
db = TinyDB("db.json")

# register = Register(proxyserver='199.188.72.7:8800')

args = sys.argv
if args[1] == 'bookmark':
    URL = args[2]
    bots = db.all()
    for bot in bots:
        hatena = Hatena(username=bot['username'],password=bot['password'],proxyserver=bot['proxyserver'])
        hatena.bookmark(url=URL)
        hatena.close()
