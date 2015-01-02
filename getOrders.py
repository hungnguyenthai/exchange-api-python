#! /usr/bin/python 
import sys
import requests
from QuoineApiSettings import Settings

api = Settings()

hdrs = {
   "user-agent": api.UserAgent,
   "X-Quoine-Device": api.DeviceName,
   "X-Quoine-User-Id": api.UserId,
   "X-Quoine-User-Token": api.UserToken
  }

ccy_list = ["AUD","IDR","HKD","SGD","JPY","PHP","USD"]

if len(sys.argv) > 1:
  currency = sys.argv[1]
else:
  print "No Currency provided - must be one of %s" % ', '.join(ccy_list)
  sys.exit(1)

if currency not in ccy_list:
  print "Invalid currency '%s' - must be one of %s " % (currency, ', '.join(ccy_list))
  sys.exit(1)

base_currency = "BTC"

url = api.BaseURL + api.GetOrdersURI % (base_currency,currency)

try:
   r = requests.get(url,headers=hdrs)
   print r.status_code
   print r.text
except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
