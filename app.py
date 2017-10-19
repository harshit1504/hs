# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") == "age":
        number1=req.get("result").get("parameters").get("number")
        res=age(number1)
        return res
    if req.get("result").get("action") == "weight":
        number2=req.get("result").get("parameters").get("unit-weight").get("amount")
        res=weight(number2)
        return res
    if req.get("result").get("action") == "3months":
        b1=req.get("result").get("parameters").get("bool")
        boo=str(b1)
        res=months(boo)
        return res
    

    




def age(number):
    if number<18 or number>60 :
        speech = "Your age Doesn't belong in eligible age group. Sorry, you cant donate blood"
    if number>=18 and number <=60 :
        speech = "What Is your Weight"    
        
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }    

def weight(number):
    if number > 50:
        speech = "Have You Donated Blood in past 3 months?"
    if number < 50:
        speech = "Sorry! You must be above 50 KG to donate blood."   
    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }   
    
def months(a): 
    if a =="yes":
        speech = "Sorry you can't donate blood"
    if a =="no":
        speech = "You Can Donate Blood if you fulfill these requirements:- \n Never has been tested HIV positive. \n Not suffering from ailments like cardiac arrest, hypertension, blood pressure, cancer, epilepsy, kidney ailments and diabetes. \n Hasn't undergone ear/body piercing or tattoo in the past 6 months. \n Haven't undergone immunization in the past 1 month. \n Never treated for rabies or received Hepatitis B vaccine in the past 6 months. \n Hasn't consumed alcohol in the past 24 hours. \n Haven't undergone major dental procedures or general surgeries in the past 1 month. \n Haven't had fits, tuberculosis, asthma and allergic disorders in the past. \n In case of female donors: \n \t  Not pregnant or breastfeeding. \n \t Haven't had miscarriage in the past 6 months. \n Do you fulfill these requirements?"    
     return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }  

    

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
