print("question no 1")
#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc). Q.2- Get the IP address of some common sites like Google,
# Facebook by using DNS lookup. Q.3- Using Tweepy library try to extract tweets from Twitter.
#An access token is an object that describes the security context of a process or thread.
#  The information in a token includes the identity and privileges of the user account associated with the process or thread.
# When a user logs on, the system verifies the user's password by comparing it with information stored in a security database.
#If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.

#my acccess token for twittwer
#consumer_key="uhHcvdFqHeHsRsUUwkXqJgx2Lggsjdjn"
#consumer_secret='f6q2F7IB4WiEwZj9Bt7Uvtd8QlXOrhRthUrM30UxhqR5yukl'
#access_token='2492560340-yJLTXsJ2NQuKar73n0FgwBWobGS1ERevggvgvgv'
#access_token_secret='Bo3ZglMKQWUGclAID6Yi5vKpdXcXC5URLAoZvvbhjhbjhjdh'

print("question no 2")
# C:\Users\RAHUL TIWARI>nslookup google.com
# Server:  UnKnown
# Address:  2405:200:800::1
#
# Non-authoritative answer:
# Name:    google.com
# Addresses:  2404:6800:4002:806::200e
#           216.58.221.46
#
#
# C:\Users\RAHUL TIWARI>nslookup facebook.com
# Server:  UnKnown
# Address:  2405:200:800::1
#
# Non-authoritative answer:
# Name:    facebook.com
# Addresses:  2a03:2880:f126:83:face:b00c:0:25de
#           31.13.78.35
#
#
# C:\Users\RAHUL TIWARI>nslookup twitter.com
# Server:  UnKnown
# Address:  2405:200:800::1
#
# Non-authoritative answer:
# Name:    twitter.com
# Addresses:  104.244.42.129
#           104.244.42.1



print("question no 3")
import tweepy
consumer_key="uhHcvdFqHeHsRskXqJgx2Lkkk"
consumer_secret='f6q2F7IB4WiEwZj9Bt7Uvtd8QlXOrhRBLCeEAthUrM30hhggg'
access_token='2492560340-yJLTXsJ2NQuKar73n0FgwBWobGS1bnnjnnj2'
access_token_secret='Bo3ZglMKQWUGclAID6Yi5vKpdXcXC5URLAoZ6vhhhvjbhjccb'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
m=str(input("enter any HASH tag for search:"))
tweets=api.search(m,lang='en',count="10",tweet_mode='extended')
print("tweets")
for tweet in tweets:
    print("---------------------------------")
    print(tweet.full_text)
    print("---------------------------------")






print("question 4")
#A library is a collection of functions / objects that serves one particular purpose.
#  you could use a library in a variety of projects. (Various specialized services in our case)

#An API is an interface for other programs to interact with your program or library  without having direct access.
#  ( giving specifications for our need to various vendors in our case)















