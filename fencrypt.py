#
# Simple File Locker using Exclusive or writen in Python 3
# by : https://github.com/iamnubs
#

import os
import sys

path = os.getcwd()
files = os.listdir(path)


def enc(fn):
    pw = sys.argv[3]
    buff = bytearray(open(fn, 'rb').read())
    ret = bytearray(len(buff))
    for c in range(len(buff)):
        ret[c] = buff[c] ^ ord(pw[c % len(pw)])
    return ret


def hello():
    print("""fencrypt is Simple File Locker using exclusive or method to encrypt file by extension
    usage :
    \tencrypt: fencrypt e ".extension" "password"
    \tdecrypt: fencrypt d ".extension" "password" """)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        hello()
    else:
        ext = sys.argv[2]
        if sys.argv[1] == 'e':
            for i in files:
                if i[-(len(ext)):] == ext:
                    open('%sl' % i, 'wb').write(enc(i))
        elif sys.argv[1] == 'd':
            for i in files:
                if i[-(len(ext) + 1):] == '%sl' % ext:
                    open('%s-out%s' % (i[:-len(ext) - 1], i[-len(ext) - 1:-1]), 'wb').write(enc(i))
        else:
            hello()
