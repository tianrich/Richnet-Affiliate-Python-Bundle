import tweepy
import getpass
import time

# enter your Twitter API keys
consumer_key = input("Enter your consumer key: ")
consumer_secret = input("Enter your consumer secret: ")
access_token = input("Enter your access token: ")
access_token_secret = input("Enter your access token secret: ")

# connect to the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    # item information
    item_name = input("Enter the item name: ")
    price_before = input("Enter the price before the deal: ")
    deal_price = input("Enter the deal price: ")
    product_link = input("Enter the product link: ")
    use_voucher_code = input("Do you want to use a voucher code? (y/n): ")
    if use_voucher_code.lower() == 'y':
        voucher_code = input("Enter the voucher code: ")
    else:
        voucher_code = None

        # Add affiliate link
    affiliate_link = "YOUR AFFILIATE HTTPS LINK GOES HERE"
    final_link = affiliate_link + product_link 

    # tweet message
    message = f'{item_name} on sale! #ad Before: ${price_before}, Now: ${deal_price}'
    if voucher_code:
        message += f' Use code {voucher_code} at checkout! '
    message += f'Link: {affiliate_link}{product_link}'

    # post the tweet
    tweet = api.update_status(message)
    print(f'Tweet sent! Tweet id: {tweet.id}')

    # wait for a certain amount of time before posting the next tweet
    time.sleep(3600) # waits for 1 hour before posting the next tweet
