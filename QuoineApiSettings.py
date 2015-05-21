#! /usr/bin/python

class Settings():

   	UserAgent  = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"
	UserId     = "555555555"
	DeviceName = "anything"
        # staging.heroku.com : https://quoine-stag1.herokuapp.com
        # prod.heroku.com : https://quoine-prod.herokuapp.com
        UserToken = "1FakeToken"
	Headers = {
   		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0",
		"X-Quoine-Device": DeviceName,
   		"X-Quoine-User-Id":UserId,
   		"X-Quoine-User-Token": UserToken
  	}

	# Base URL for API calls
        # production quoinecom 
	BaseURL = "https://api.quoine.com/"
        # staging3
	#BaseURL = "https://quoine-stag3.herokuapp.com/"

	# URI parts for calling API - to be added to BaseURL per call
	GetAccountsURI    = "accounts"				# [GET] 				
	GetOrderURI       = "orders/%s"				# [GET] 				
	GetOrdersURI      = "orders?currency_pair_code=%s%s"	# [GET] 				
	GetProductURI     = "products/code/%s/%s"               # [GET] 				
	GetProductsURI    = "products"				# [GET] 				
        GetPriceLadderURI = "products/%s/price_levels"          # [GET]
        AddOrderURI       = "orders"                            # [POST]
	CancelOrderURI    = "orders/%s/cancel"	        	# [PUT]

if __name__ == "__main__":
  gbl = Settings()
  print gbl.UserAgent
  print gbl.UserId
  print gbl.DeviceName
  print gbl.BaseURL
  print gbl.UserToken
