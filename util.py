import random
from pyquery import PyQuery as pq
import re

def genPassword():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 8
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]
    return mypw

def genUsername():
    for i in range(0,100):
        users = []
        domObj = pq(url='http://b.hatena.ne.jp/entry/www.find-job.net/startup/api-2013')
        for userElem in domObj('.username').items():
             users.append( userElem.text() )
        username = random.choice(users)
        chrList = list(username)
        newChrList = []
        vowelList = ['a','i','u','e','o']
        for char in chrList:
            if re.match(r"[aiueo]" , char):
                char = random.choice(vowelList)
            if re.match(r"\d" , char):
                char = str(random.randint(0,9))
            newChrList.append(char)
        newUsername = ''.join(newChrList)
        try:
            validDom = pq(url='http://b.hatena.ne.jp/{}'.format(newUsername))
            print('error',newUsername)
        except Exception:
            break
    return newUsername
