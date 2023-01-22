import tweepy

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# Connect to the Twitter API using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    shop_name = input("Enter the shop name: ")
    url_link = input("Enter a link to share: ")
    additional_text = input("Enter additional text to share: ")
    affiliated_link = f"https://go.skimresources.com?id=100269X1558466&xs=1&url="
    message = f"Spotted online - {shop_name} has a sale on at the moment {additional_text} #ad #spotted {affiliated_link}{url_link}"
    api.update_status(message)
    print("Shared to Twitter: ", message)
