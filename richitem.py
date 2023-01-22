import tweepy

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    # Get product information from user input
    product_title = input("Enter product title: ")
    old_price = input("Enter old price: ")
    deal_price = input("Enter deal price: ")
    url = input("Enter product URL: ")
    shop_name = input("Enter shop name: ")
    # Create tweet text
    tweet = f"Check out this deal from {shop_name}! {product_title} is on sale for £{deal_price} (was £{old_price}). #ad #spotted >> {url}"
    # Print tweet text
    print(tweet)
    # Share tweet
    api.update_status(tweet)
