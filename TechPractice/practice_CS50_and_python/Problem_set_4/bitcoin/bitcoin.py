import json
import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
USD =  o["bpi"]
USD_rate = USD["USD"]
rate = USD_rate["rate_float"]
#print(rate)

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    # elif not sys.argv[1].isdigit():
    #     sys.exit("Command-line argument is not a number")
    else:
        qty = sys.argv[1]
        qty = float(qty)
        print(f"${(rate*qty):,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    print("Error with request")