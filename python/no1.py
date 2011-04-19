from itertools import cycle
from string import ascii_lowercase, maketrans


msg = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "
       "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm "
       "jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")


def take(n, xs):
    return [xs.next() for _ in xrange(n)]


def drop(n, xs):
    for _ in xrange(n):
        xs.next()

    return xs


def rotate(n, xs):
    return take(len(xs), drop(n, cycle(xs)))


def translate(msg):
    return msg.translate(maketrans(ascii_lowercase,
                                   ''.join(rotate(2, ascii_lowercase))))


if __name__ == '__main__':
    print translate(msg)
    print translate("map")
