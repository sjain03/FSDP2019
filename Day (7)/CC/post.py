# -*- coding: utf-8 -*-
"""
Created on Wed May 15 06:24:00 2019

@author: Sahil
"""

# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com

import json
import requests

Host = "https://enr01fczhvl3q.x.pipedream.net/"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )
