import tweepy
import config

# So far we have installed the tweepy package and created a config with
# sensitive information

# lets create the authorization instance


def OAuth():
    try:
        auth = tweepy.OAuthHandler(config.API_Key, config.API_Secret)
        auth.set_access_token(config.access_token, config.access_secret)
        return auth

    except Exception:
        return None


oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('My first tweet Using Python! More on the way.')
print('Tweet is posted.')
