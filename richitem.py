import tweepy

# Enter your Twitter API credentials here
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    # Get item details from user input
    item_name = input("Enter item name: ")
    price_before_prompt = input("Is there a price before? (y/n)")
    price_before = input("Enter original price: ") if price_before_prompt.lower() == 'y' else None
    deal_price_prompt = input("Is there a deal price? (y/n)")
    deal_price = input("Enter deal price: ") if deal_price_prompt.lower() == 'y' else None
    voucher_code = input("Enter voucher code (optional): ")
    item_url = input("Enter item URL (optional): ")
    add_affiliate = input("Do you want to add affiliate link? (y/n)")

    # Construct tweet text
    if price_before:
        tweet_text = f"{item_name} is on sale! Before: ${price_before}"
    else:
        tweet_text = f"Check out the following sale: {item_name}"
    if deal_price:
        tweet_text += f", Now: ${deal_price}"
       if voucher_code:
        tweet_text += f" Use code {voucher_code} at checkout!"
    if item_url:
        if add_affiliate.lower() == 'y':
            # Add hidden affiliate link 
            affiliate_link = "https://go.skimresources.com?id=100269X1558466&xs=1&url="
            item_url = affiliate_link + item_url
        tweet_text += f" Check it out here: {item_url} "
    tweet_text += "#ad"

    # Post tweet
    api.update_status(tweet_text)

    print("Tweet posted!")
    # Add a prompt asking if the user wants to post another tweet
    another_tweet = input("Do you want to post another tweet? (y/n)")
    if another_tweet.lower() == 'n':
        break
