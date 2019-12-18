#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import hashlib
import json
from hashlib import sha256
from time import time, asctime
from uuid import uuid4
from textwrap import dedent
from uuid import uuid4
from flask import Flask, jsonify, request, render_template
from urllib.parse import urlparse
import requests
import pickle
from optparse import OptionParser
from matplotlib import pyplot as plt
 
def parse_opts(parser):
    parser.add_option("-f","--file",action="store",type="str",dest="file",default="",help="the file selected")
    parser.add_option("-n","--num",action="store",type="int",dest="n",default=10,help="number by default")
    (options,args) = parser.parse_args()

    return options

options = parse_opts(OptionParser(usage="%prog [options]"))

def wordcount(str_):
    str_lst = str_.replace('\n', '').lower().split(' ')
    ret = {}
    for j in str_lst:
        if j in ret.keys():
            ret[j] += 1
        else:
            ret[j] = 1
    ret = sorted(ret.items(), key = lambda x: x[1], reverse = True)
    return ret

def do_draw(lst):
    x = []
    y = []
    i = 0
    for t in lst:
        if t[0] == '':
            continue
        else:
            x.append(t[0])
            y.append(t[1])
            i += 1 
        if i >= options.n: break
    plt.bar(x, y, align =  'center') 
    plt.savefig("/tmp/ret.png")

def main():
    #print(options.file)
    str_ = ""
    with open(options.file, 'r') as f:
        str_ = f.read()

    do_draw(wordcount(str_))

if __name__ == '__main__':
  main()
