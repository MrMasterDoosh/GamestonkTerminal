import os
from dotenv import load_dotenv

load_dotenv()

# https://www.alphavantage.co
API_KEY_ALPHAVANTAGE = os.getenv("GT_API_KEY_ALPHAVANTAGE") or "8TFJ5T90OM1ACHAV"

# https://financialmodelingprep.com/developer
API_KEY_FINANCIALMODELINGPREP = (
    os.getenv("GT_API_KEY_FINANCIALMODELINGPREP") or "NkWYm2ei_DG_msQcnWsi"
)

# https://www.quandl.com/tools/api
API_KEY_QUANDL = os.getenv("GT_API_KEY_QUANDL") or "NkWYm2ei_DG_msQcnWsi"

# https://www.reddit.com/prefs/apps
API_REDDIT_CLIENT_ID = os.getenv("GT_API_REDDIT_CLIENT_ID") or "WejqJB1iaxr56w"
API_REDDIT_CLIENT_SECRET = os.getenv("GT_API_REDDIT_CLIENT_SECRET") or "lirmfilcWY064V9oLHqq9PiMt9CGvQ"
API_REDDIT_USERNAME = os.getenv("GT_API_REDDIT_USERNAME") or "xsmiley"
API_REDDIT_USER_AGENT = os.getenv("GT_API_REDDIT_USER_AGENT") or "MSent"
API_REDDIT_PASSWORD = os.getenv("GT_API_REDDIT_PASSWORD") or "Xsmileyftw1!"

# https://polygon.io
API_POLYGON_KEY = os.getenv("GT_API_POLYGON_KEY") or "6sxIomRFZPK6hmDBcwS682b2d5Hwyqd4"

# https://developer.twitter.com
API_TWITTER_KEY = os.getenv("GT_API_TWITTER_KEY") or "hZfciOpkCxbEEcUMgo6mxqNcy"
API_TWITTER_SECRET_KEY = os.getenv("GT_API_TWITTER_SECRET_KEY") or "g3qdM4BAUhWpokRgKegmXbgTa2jKHU3Nb5oebHcMXjB9TKrdoA"
API_TWITTER_BEARER_TOKEN = os.getenv("GT_API_TWITTER_BEARER_TOKEN") or "AAAAAAAAAAAAAAAAAAAAAGW0OwEAAAAANRGK5ItH5hyR%2Bj9DOOwReTnsv68%3DOjRkU3eNrbbIa3CAcoqcgrZ5g35oOqBxuBxxjil9PlX3Ra6vCW"

# https://fred.stlouisfed.org/docs/api/api_key.html
API_FRED_KEY = os.getenv("GT_FRED_API_KEY") or "99a5b0372bebb225b1860b13dadf1dc0"

# https://newsapi.org
API_NEWS_TOKEN = os.getenv("GT_API_NEWS_TOKEN") or "1d78d7361eae48d2831cc714ee49e251"

# Robinhood
RH_USERNAME = os.getenv("GT_RH_USERNAME") or "saadqazi23@gmail.com"
RH_PASSWORD = os.getenv("GT_RH_PASSWORD") or "9052850043"

# https://developer.oanda.com
OANDA_ACCOUNT = os.getenv("GT_OANDA_ACCOUNT") or "salikqazi@gmail.com"
OANDA_TOKEN = os.getenv("GT_OANDA_TOKEN") or "fb10c0015a1308a31049077140efb0a1-4d2c521058a2477f3ff62ce4f1dd8b56
"

# https://tradier.com/products/market-data-api
TRADIER_TOKEN = os.getenv("GT_TRADIER_TOKEN") or "REPLACE_ME"

# Selenium Webbrowser drivers can be found at https://selenium-python.readthedocs.io/installation.html
WEBDRIVER_TO_USE = "chrome"
PATH_TO_SELENIUM_DRIVER = PATH  # Replace with "PATH"

# https://coinmarketcap.com/api/
COINMARKETCAP_KEY = os.getenv("GT_CMC_API_KEY") or "c4c7f749-8171-4185-9c42-86ba69117426"
