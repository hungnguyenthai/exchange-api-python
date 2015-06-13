#! /usr/bin/python 
import sys
import requests
import json
from QuoineApiSettings import Settings

api = Settings()

hdrs = {
   "user-agent": api.UserAgent,
   "X-Quoine-Device": api.DeviceName, 
   "X-Quoine-User-Id": api.UserId, 
   "X-Quoine-User-Token": api.UserToken
  }

try:
   url = api.BaseURL + api.GetBitcoinTransactionsURI
   r = requests.get(url,headers=hdrs)
   #print r.text
   data = json.loads(r.text)
   for tx in data["models"]:
     print tx["id"], ",",tx["transaction_type"],",",tx["created_at"],",",tx["gross_amount"]
except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
