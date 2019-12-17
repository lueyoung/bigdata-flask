#!/usr/local/bin/python
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
    parser.add_option("-f","--file",action="store",type="str",dest="fn",default="",help="the file selected")
    (options,args) = parser.parse_args()

    return options

options = parse_opts(OptionParser(usage="%prog [options]"))
def main():

        
if __name__ == '__main__':
  main()
