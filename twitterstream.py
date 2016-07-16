import oauth2 as oauth
import urllib2 as urllib
import sys

# See assignment1.html instructions or README for how to get these credentials

api_key = "kdyDA6M0f2W0pK0Kwqy60fYTF"
api_secret = "vp27gUhGD3m2uv0NmlZrcwP6o8QqgGZMbJaud7iZCEHUY9ByyE"
access_token_key = "2599282818-nyiJbM3bskcxiWREiyhP7UwfBVBcbBwcHIVjvO5"
access_token_secret = "om6xk1CUIC4LoIkE62dd7k4ioWr7lfQiiOfZC3YhOeQmv"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  query = sys.argv[1]
  url = "https://stream.twitter.com/1/statuses/sample.json"
  url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + query
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  print "let me test"
  fetchsamples()
