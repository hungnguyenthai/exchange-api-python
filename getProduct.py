#! /usr/bin/python
import os
import sys
import json
import requests
from QuoineApiSettings import Settings

api = Settings()
ccy_list = ["BTCAUD","BTCIDR","BTCHKD","BTCSGD","BTCJPY","BTCPHP","BTCUSD"]
url = api.BaseURL + api.GetProductURI

if len(sys.argv) == 3:
  product_code       = sys.argv[1]
  currency_pair_code = sys.argv[2]

  if product_code <> "CASH":
     print "Product code is not valid '%s' should be 'CASH'" % product_code 
     sys.exit(1)

  if currency_pair_code not in ccy_list:
     print "Currency code is not valid '%s' should be one of %s" % (currency_pair_code,' , '.join(ccy_list)) 
     sys.exit(1)

  url = url % (product_code,currency_pair_code)
else:
  print "Product code and Currency pair need to be supplied e.g. Python getProduct.py BTCUSD CASH" 
  sys.exit(1)

print url

r = requests.get(url)
if r.status_code == 200:
   if r.text == "null":
      print "No content returned for URL %s" % url
   else:
      data = json.loads(r.text)
      print data
      #for d in data:
      #  print "++++++++++++++++++++++\n"
      #  print repr(d)
        #if d["product_type"] == "CASH":
        #  for key, value in d.iteritems():
        #    if key == "id" or key == "currency_pair_code":
        #       print key, value
      print "\n"
else:
   print "\nError %s while calling URL %s:\n" % (r.status_code,url)