import tweepy
import config

# So far we have installed the tweepy package and created a config with
# sensitive information

# lets create the authorization instance


def OAuth():
    try:
        # Here we are setting up the the authorization so our program can
        auth = tweepy.OAuthHandler(config.API_Key, config.API_Secret)
        auth.set_access_token(config.access_token, config.access_secret)
        return auth

    except Exception:
        return 'It broke'


oauth = OAuth()
api = tweepy.API(oauth)

# api.update_status('Second tweet Using Python and I uploaded an image.')
api.update_with_media(
    'pup.jpeg', status="Second tweet using Python it's a puppy")
print('Tweet is posted.')
