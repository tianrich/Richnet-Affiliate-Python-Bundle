import tweepy

# Set up your Twitter API credentials
consumer_key = 'soMBgaf6BpB8X4hmqvmmBvGIM'
consumer_secret = 'sKIsctMsZX0iDeglHQS7TfvIzPff71BE6UuQumdnipz27e8Khn'
access_token = '2763850618-Lb7uHchyi1VLhYi7aJqqYQJsnSELW1b2sP3Qh3t'
access_token_secret = 'TzmoAf9QOuULnANa1k4Ye5BHWVSdn0NGR73EChygHwDlT'

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
