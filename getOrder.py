#! /usr/bin/python 
import sys
import json
import requests
from QuoineApiSettings import Settings

api = Settings()

hdrs = {
   "user-agent": api.UserAgent,
   "X-Quoine-Device": api.DeviceName,
   "X-Quoine-User-Id": api.UserId,
   "X-Quoine-User-Token": api.UserToken
  }

if len(sys.argv) > 1:
  order_id = sys.argv[1]
else:
  print "No Order Id provided "
  sys.exit(1)

#if api.is_number(order_id) == False or int(order_id) <= 0:
#  print "Invalid Order Id '%s'" % order_id
#  sys.exit(1)

#url = "https://api.quoine.com/orders/%s" % order_id
url = api.BaseURL  + api.GetOrderURI % order_id
print "URL : ", url

try:
   response = requests.get(url,headers=hdrs)
   print response.status_code
   print response.text

except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e

