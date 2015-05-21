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
msg = "Ticker Price @ Quoine.com"
r = requests.get(url)
if r.status_code == 200:
   if r.text == "null":
      print "No content returned for URL %s" % url
   else:
      data = json.loads(r.text)
      #print data
      ask = ""
      bid = ""
      ccy = ""
      line = ""
      for d in data:
        if d["product_type"] == "CASH":
          for key, value in d.iteritems():
            if key == "market_ask":
               ask = value
            elif key == "market_bid":
               bid = value
            elif key == "currency_pair_code":
               ccy = value
          if ccy == "BTCIDR" or ccy == "BTCPHP" or ccy == "BTCJPY":
            line =  "%s %s/%s" % (ccy,'{0:01,.0f}'.format(bid),'{0:01,.0f}'.format(ask))  
          else:
            line =  "%s %s/%s" % (ccy,'{0:01,.2f}'.format(bid),'{0:01,.2f}'.format(ask))  
          msg = msg + "\n" + line
      print "\n"
      print msg 
else:
   print "\nError %s while calling URL %s:\n" % (r.status_code,url)
