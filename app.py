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
import time
 
def parse_opts(parser):
    parser.add_option("-p","--port",action="store",type="int",dest="port",default=8080,help="the working port")
    (options,args) = parser.parse_args()

    return options

options = parse_opts(OptionParser(usage="%prog [options]"))
# Instantiate our Node
app = Flask(__name__)
app.secret_key = os.urandom(24) 
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/searching', methods=['GET','POST'])
def searching():
    return render_template('searching.html')

@app.route('/healthz', methods=['GET'])
def healthz():
    response = {
        'status': "normal",
        'time': str(asctime()),
    }
    return jsonify(response), 200

def checkpoint_ret():
    values = request.form
    required = ['id']
    if not all(k in values for k in required):
        return 'Missing values', 400
    response = do_search(values.get("id"),marker='temp')
    return render_template('ret_v3.html',msgs=response,id=values.get("id"))
@app.route('/spark_ret', methods=['GET','POST'])
def spark_ret():
    f = "/text/README.md.Spark"
    t = time.time()
    ret = mk_png(f,t)
    #return render_template('ret_v4.html')
    return render_template(ret)
@app.route('/hadoop_ret', methods=['GET','POST'])
def hadoop_ret():
    f = "/text/README.txt.Hadoop"
    t = time.time()
    ret = mk_png(f,t)
    return render_template(ret)

def mk_png(f,t):
    ret = "ret." + str(t) + ".html"
    cmd = ""
    os.system("rm -f /tmp/ret.png")
    os.system("rm -f /templates/ret.png")
    cmd = "/wcount.py -f " + f
    os.system(cmd)
    cmd = "yes | cp /tmp/ret.png /static/img/ret." + str(t) + ".png"
    os.system(cmd)
    cmd = "yes | cp /ret.html.sed /templates/" + ret
    os.system(cmd)
    cmd = "sed -i s?{{.n}}?" + str(t) + "?g /templates/" + ret 
    os.system(cmd)
    return ret
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=options.port)
