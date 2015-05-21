#! /usr/bin/python
import sys
import requests

url = "https://quoine-stag1.herokuapp.com/fiat_transactions?currency=USD"

hdrs = {
   "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0",
   "X-Quoine-Device": "api",
   "X-Quoine-User-Id": "59",
   "X-Quoine-User-Token": "sXdvyT6q1Kxo2xLaGr8J"
  }

try:
   print "Headers: ", repr(hdrs)
   print "\n"
   print "URL : ", url
   print "\n"
   r = requests.get(url,headers=hdrs)
   print r.headers
   print r.request.headers
   print r.status_code
   print r.text
except requests.exceptions.HTTPError as e:
   print "Error: \n"
   print e
