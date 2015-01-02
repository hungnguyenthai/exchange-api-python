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

try:
   url = api.BaseURL + api.GetAccountsURI 
   r = requests.get(url,headers=hdrs)
   print r.status_code
   print r.text
except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
