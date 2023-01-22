import pyperclip
import tweepy

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

while True:
    # Get input from user
    amazon_link = input("Enter an Amazon link: ")
    item_name = input("Enter the name of the item: ")
    item_price = input("Enter the price of the item: ")

    # Add affiliate link
    affiliate_link = "richnet-20"
    final_link = amazon_link + "?tag=" + affiliate_link

    # Share link on Twitter with item name, price and #ad
    message = "Check out this great deal on " + item_name + " for only $" + item_price + "! " + final_link + " #ad"
    api.update_status(message)
    print("Link shared on Twitter!")

    # Give option to copy link
    copy_choice = input("Do you want to copy the link? (yes/no): ")
    if copy_choice == "y":
        pyperclip.copy(final_link)
        print("Link copied to clipboard!")
    else:
        print("Link not copied.")
