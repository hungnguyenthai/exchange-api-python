#! /usr/bin/python
import os
import sys
import json
import requests

url = "https://api.quoine.com/products/%s/price_levels"

ccy_id = "1"
ccy    = "USD"

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
   
url = url % ccy_id

print "\nURL : ", url

r = requests.get(url)
if r.status_code == 200:
   if r.text == "null":
      print "No content returned for URL %s" % url
   else:
      data = json.loads(r.text)
      print "\n"
      print "Currency %s has Ask price levels: \n" % ccy
      print data['sell_price_levels']
      print "\nand Buy price levels: \n" 
      print data['buy_price_levels']
      print "\n"
else:
   print "\nError %s while calling URL %s:\n" % (r.status_code,url)
