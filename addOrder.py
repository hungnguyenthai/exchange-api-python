#! /usr/bin/python 
import sys
import json
import numbers
import requests
from QuoineApiSettings import Settings

api = Settings()
ccy_list = ["BTCAUD","BTCIDR","BTCHKD","BTCSGD","BTCJPY","BTCUSD","BTCPHP"]
product_list = ["CASH"]

hdrs = {
   'Content-type': 'application/json', 
   'Accept': 'text/plain',
   "user-agent": api.UserAgent,
   "X-Quoine-Device": api.DeviceName,
   "X-Quoine-User-Id": api.UserId,
   "X-Quoine-User-Token": api.UserToken
  }

order = {}
price = 0
quantity = 0
order_type = ""
side = ""
currency_pair_code = ""
product_code = ""

if len(sys.argv) < 7:
  print "Full set of Order details not provided, should be <price> <quantity> <side> <order type> <currency pair> <product> "
  sys.exit(1)

try: 
  price = float(sys.argv[1])
  if price <= 0:
     print "Invalid price '%s' - must be greater than zero " % sys.argv[1]
     sys.exit(1)
  else:
     order['price'] = price
except ValueError:
  print "Invalid price '%s' provided " % sys.argv[1]
  sys.exit(1)

try: 
  quantity = float(sys.argv[2])
  if quantity <= 0:
     print "Invalid quantity '%s' - must be greater than zero " % sys.argv[2]
     sys.exit(1)
  else:
     order['quantity'] = quantity
except ValueError:
  print "Invalid price '%s' provided " % sys.argv[2]
  sys.exit(1)

side = sys.argv[3]
if side.lower() <> "buy" and side.lower() <> "sell":
  print "Invalid order side '%s' provided - must be either 'buy' or 'sell' " % side
  sys.exit(1)
else:
  order['side'] = side

order_type  = sys.argv[4]
if order_type .lower() <> "limit" and order_type.lower() <> "market" and order_type.lower() <> 'range':
  print "Invalid order type '%s' provided - must be 'limit', 'market' or 'range' " % order_type 
  sys.exit(1)
else:
  order['order_type'] = order_type

currency_pair_code  = sys.argv[5]
if currency_pair_code.upper() not in ccy_list:
  print "Invalid currency pair '%s' provided - must be one of %s " % (currency_pair_code," , ".join(ccy_list)) 
  sys.exit(1)
else:
  order['currency_pair_code'] = currency_pair_code

product_code  = sys.argv[6]
if product_code.upper() not in product_list:
  print "Invalid product code '%s' provided - must be one of %s " % (product_code," , ".join(product_list)) 
  sys.exit(1)
else:
  order['product_code'] = product_code

url = api.BaseURL + api.AddOrderURI

request = {}
request['order'] = order

try:
   response = requests.post(url,data=json.dumps(request),headers=hdrs)
   print response.status_code
   print response.headers
   print response.text

except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
