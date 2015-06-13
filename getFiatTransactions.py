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

ccy_list = ["AUD","CNY","EUR","IDR","HKD","SGD","JPY","PHP","USD"]

if len(sys.argv) > 1:
  currency = sys.argv[1]
else:
  print "No Currency provided - must be one of %s" % ', '.join(ccy_list)
  sys.exit(1)

if currency not in ccy_list:
  print "Invalid currency '%s' - must be one of %s " % (currency, ', '.join(ccy_list))
  sys.exit(1)

try:
   url = api.BaseURL + api.GetFiatTransactionsURI % currency 
   r = requests.get(url,headers=hdrs)
   #print r.text
   data = json.loads(r.text)
   for tx in data["models"]:
     print tx["id"], ",",tx["transaction_type"],",",tx["created_at"],",",tx["gross_amount"],",",tx["net_amount"],",",tx["fee"],",",tx["notes"]
except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
