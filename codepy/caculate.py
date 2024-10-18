import math

c = 3e8
fl1 = 1575.42e6
fl2 = 1227.6e6
b1 = c / fl1
b2 = c / fl2


def mwcaculate(l1, l2, p1, p2):
    if l1 != 0 and l2 != 0 and p1 != 0 and p2 != 0:
        lwn = ((fl1 - fl2) / (fl2 + fl2)) * (p1 / b1 + p2/ b2) - l1 + l2
        return lwn


def gfcaculate(l1, l2):
    if l1 != 0 and l2 != 0:
        lgf = b1 * l1 - b2 * l2
        return lgf

def ifnull(l):
    if l=='':
        l=0
    return l