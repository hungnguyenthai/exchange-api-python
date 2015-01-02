#! /usr/bin/python
import os
import sys
import json
import requests
from QuoineApiSettings import Settings

api = Settings()

url = api.BaseURL + api.GetProductsURI

if len(sys.argv) > 1:
  url = "%s/%s" % (url, sys.argv[1])

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
