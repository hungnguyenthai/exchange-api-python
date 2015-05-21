#! /usr/bin/python 
import sys
import json
import numbers
import requests
from QuoineApiSettings import Settings

api = Settings()

hdrs = {
   "user-agent": api.UserAgent,
   "X-Quoine-Device": api.DeviceName,
   "X-Quoine-User-Id": api.UserId,
   "X-Quoine-User-Token": api.UserToken
  }

order_id = 0
if len(sys.argv) > 1:
  try: 
    order_id = int(sys.argv[1])
  except ValueError:
    print "Invalid Id '%s' provided " % sys.argv[1]
    sys.exit(1)
else:
  print "No Order Id provided "
  sys.exit(1)

url = api.BaseURL  + api.GetOrderURI % order_id
print url
try:
   response = requests.get(url,headers=hdrs)
   print response.status_code
   print response.text

except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e

