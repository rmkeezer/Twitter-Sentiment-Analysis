from TwitterAPI import TwitterAPI, TwitterRestPager
import sys
import pprint as pp
import json

def main():
    CONSUMER_KEY = 'PODBig7b0xnmNNlGlKFAXJTA7'
    CONSUMER_SECRET = 'EtVMSh1maJrjWKWhBh7Eq4vi0EZylOeobGeaHVPMOfrPGEQXOk'
    ACCESS_TOKEN_KEY = '161721803-fM6Gne4u1vvdX7mY5Nk6d7plBDcuEV2w8UyugMJQ'
    ACCESS_TOKEN_SECRET = 'SWSn7Rzjee8WnDeQXqmwcIvVflYkSL9JPh9TDK1G5kiTD'

    print(sys.argv[1])
    print(sys.argv[2])

    api = TwitterAPI(CONSUMER_KEY,
                     CONSUMER_SECRET,
                     ACCESS_TOKEN_KEY,
                     ACCESS_TOKEN_SECRET,
                     auth_type='oAuth1')

    r = TwitterRestPager(api, 'search/tweets', {'q':sys.argv[1], 'count':100})
    count = 0
    tweets = []
    for item in r.get_iterator():
        count += 1
        if count % 100 == 0:
            print("Working...")
        if count % 1000 == 0:
            print("Saved")
            oldtweets = []
            try:
                f = open(sys.argv[2], 'r')
                oldtweets = f.read().split('\n')
                f.close()
            except:
                pass
            f = open(sys.argv[2], 'a')
            f.write('\n'.join([t for t in tweets if t not in oldtweets]))
            tweets = []
            f.close()
        if 'text' in item:
            tweets.append(item['text'].encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        elif 'message' in item and item['code'] == 88:
            print ('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
            break

if __name__=='__main__':
    main()