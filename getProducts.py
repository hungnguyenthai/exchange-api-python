#! /usr/bin/python
import os
import sys
import json
import requests

if len(sys.argv) > 1:
  ccy = sys.argv[1]
  if ccy == "USD":
    ccy_id = "1"
  elif ccy == "EUR":
    ccy_id = "3"
  elif ccy == "JPY":
    ccy_id = "5"
  elif ccy == "SGD":
    ccy_id = "7"
  elif ccy == "HKD":
    ccy_id = "9"
  elif ccy == "IDR":
    ccy_id = "11"
  elif ccy == "AUD":
    ccy_id = "13"
  elif ccy == "PHP":
    ccy_id = "15"
  else:
    print "error = currency supplied %s is not valid" % ccy
    sys.exit(-1)
  url = "https://api.quoine.com/products/%s" % ccy_id
  print "\nRetrieving products for currency %s" % ccy
else:
  print "\nRetrieving ALL products "
  url = "https://api.quoine.com/products"

print "URL : \n", url

r = requests.get(url)
if r.status_code == 200:
   if r.text == "null":
      print "No content returned for URL %s" % url
   else:
      data = json.loads(r.text)
      print data
      print "\n"
else:
   print "\nError %s while calling URL %s:\n" % (r.status_code,url)
