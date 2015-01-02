#! /usr/bin/python 
import sys
import requests

hdrs = {
   "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0",
   "X-Quoine-Device": "api", 
   "X-Quoine-User-Id": "59", 
   "X-Quoine-User-Token": "AE7PzZn5PxaaoEpje4a9"
  }

try:
   #print "Headers: ", repr(hdrs)
   #print "\n"
   #print "URL : https://api.quoine.com/accounts"
   #print "\n"
   r = requests.get("https://api.quoine.com/fiat_transactions?currency=USD",headers=hdrs)
   #print r.headers 
   #print r.request.headers 
   print r.status_code
   print r.text
except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
