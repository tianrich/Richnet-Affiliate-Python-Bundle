import tweepy

# Set up your Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    # Get the message to tweet
    message = input("Enter your tweet or 'q' to quit: ")
    if message == 'q':
        break
    # Add the #ad hashtag to the end of the message
    message += " #ad"

    # Post the tweet
    api.update_status(message)

    print("Tweet successfully sent!")
