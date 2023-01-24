import tweepy

# Set up your Twitter API keys
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    # Define the product you want to share
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")
    product_link = input("Enter product link: ")
    discount_coupon = input("Enter discount coupon (if any): ")
    product = {
        "name": product_name,
        "price": product_price,
        "link": product_link
    }
    # Compose the tweet
    if discount_coupon:
        tweet = f"Check out {product['name']}! Only {product['price']} with {discount_coupon} coupon! {product['link']}"
    else:
        tweet = f"Check out {product['name']}! Only {product['price']}! {product['link']}"
    # Share the tweet
    api.update_status(tweet)
    print(f"Product Shared: {product['name']}")
