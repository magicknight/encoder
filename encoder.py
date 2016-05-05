# By Kishoj Bajracharya
import random
import numpy
from decimal import *
from itertools import product
from numpy.random import randint
import numpy as np


# Code for random linear coding
def linearCode(x):
    power_list = randint(5, size=(len(x), len(x)))
    par_list = np.array(2**power_list)
    result = np.dot(par_list, x)
    data = np.column_stack((par_list, result))


    return data

def encode(x):
    listOfEqns = linearCode(x)
    #for a in li:
    #	print a
    return listOfEqns

def split(n, iter, fill=None):
    return [iter[i:i+n] + [fill] * (i + n - len(iter))
            for i in xrange(0, len(iter), n)]

def ConstructListToArray(alistOfVector):
    return array(alistOfVector)
def ConcatListElements(alist):
    p = ''
    for x in alist:
        p += x
    return p

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    return reduce(lambda x,y:x+y, lst)

def ListOfCharToListOfInt(alist):
    iList = []
    for x in alist:
        # char to hex
        q = toHex(x)
        #print q
        #p = int('0x48', 16)
        # Hex to int
        p = int(q, 16)
        #print p
        iList.append(p)
    return iList

def ListOfIntToListOfString(alist):
    iList = []
    for x in alist:
        iList.append(chr(x))
    return iList


def StringDecodedToListof4(astring):# split the string into pure numbers. four string of pure numbers.
    Decodedlist = []
    c = astring.replace("], [", ', ')
    d = c.replace("[[", '[')
    e = d.replace("]]", ']')
    f = e.replace(", ", ',')
    print f
    f = e.split(',')
    for x in f:
        y = x.strip('][ ')## remove the "]["
        z = float(y)
        Decodedlist.append(z)
    listOfEqns = split(3, Decodedlist)
    return listOfEqns



# Initial data from the three different source nodes
# Say data from node A
def get_raw_data(x):
    int_list = []
    for i in x:
        # Packets whose values are conveted into the decimal values
        int_list.append(ListOfCharToListOfInt(i))


    listAns = []

    # Perform an encoding operation using Random Linear Coding
    encodedlist = []
    for item in product(*int_list):
        print item
        listOfVector = encode(item)
        encodedlist.append(listOfVector)
    encodedlist=np.array(encodedlist)

    #print encodedlist
    encoded_mess = str(encodedlist)
    print 'Encoded Message'
    print encoded_mess
    return encoded_mess


if __name__ == "__main__":
    print get_raw_data(['a2b', 'bc', 'c', 'd'])
