# -*- coding: utf-8 -*-

import requests

token = "d8e9c68b-c0dc-afac-c7f0-558e5fea9eca"

user = "t4k3nok0"


requests.post("http://api.justyo.co/yo/",
data={'api_token' : token , 'username' : user})

print user + "にYoしました" 
