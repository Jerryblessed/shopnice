
from square.client import Client
from flask import Flask

app = Flask(__name__)

from square.client import Client

# To read your secret credentials
# config = configparser.ConfigParser()
# config.read("config.ini")

# Retrieve credentials based on is_prod
# CONFIG_TYPE = config.get("DEFAULT", "environment").upper()
PAYMENT_FORM_URL = "https://sandbox.web.squarecdn.com/v1/square.js"
    
# APPLICATION_ID = "sq0idp-aduaT2vl7FqqJSxnJCunrQ"
# LOCATION_ID = "LPJEF0MM5CCWB"
# ACCESS_TOKEN = "EAAAEbWfN7h2kCEG77jDau8SBhcdKmh-6fSw-e_JKD7NZ9jjTsTzUTVNFELz1v1t"
ACCESS_TOKEN = "EAAAlvt0y1pukQHTDGVqMQvuW6Fvkj36JwBhBU4kVyAPeWRBlxZ6rps8wSVquCji"


client = Client(
    access_token=ACCESS_TOKEN,
    environment="production",
    user_agent_detail="sample_app_python_payment", # Remove or replace this detail when building your own app
)


result = client.merchants.list_merchants()

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)
  
# if __name__ == "__main__":
#     app.run(host='localhost', debug=True, port=5000)


# import logging
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from flask import Flask, render_template
# from pydantic import BaseModel
# from square.client import Client
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/callback', methods=['GET'])
# def callback():
#     # Retrieve data from Square response
#     access_token = "example_access_token"
#     merchant_id = "example_merchant_id"
#     refresh_token = "example_refresh_token"

#     # Render the login template with data
#     return render_template("index.html", access_token=access_token, merchant_id=merchant_id, refresh_token=refresh_token)

# if __name__ == "__main__":
#     app.run(host='localhost', debug=True, port=5000)
