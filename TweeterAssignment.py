import tweepy


ACCESS_TOKEN = "334730155-7MNFSsRauoXqkoqAtEGiKjIvj8R7SwMWFygdWEgu"
ACCESS_SECRET = "rbeHAQtIUW5JasVeRUibWT7zitbUTlgqJSpftZhfKAERn"
CONSUMER_KEY = "UenXi0CsY3CKlMWkxgAXohFpl"
CONSUMER_SECRET = "X0lXPQqAVGUSVCQZSNjQdISco23H0VJB7XaT6fCpx991XwqlzP"
SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
    i+=1
    f.write(res.user.screen_name)
    f.write(' ')
    f.write('[')
    f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
    f.write(']')
    f.write(" ")
    f.write('"')
    f.write(res.text.replace('\n',''))
    f.write('"')
    f.write(" ")
    f.write(str(res.user.followers_count))
    f.write(" ")
    f.write(str(res.retweet_count))
    f.write('\n')
f.close
print("Tweets retrieved ",i)
