import sys
import matplotlib.pyplot as plt
import statistics as st

print("Loading Files...")
f = open('tweets_maga_s')
tweets = f.read().split('\n')
f.close()

f = open('negative-words.txt', errors='replace')
negwords = f.read().split(';')[-1].split()
negwords = {a:1 for a in negwords}
f.close()

f = open('positive-words.txt', errors='replace')
poswords = f.read().split(';')[-1].split()
poswords = {a:1 for a in poswords}
f.close()
tbx = []
tby = []
chunksize = 1000
print("Processing Tweets...")
for chunk in [tweets[i:i+chunksize] for i in range(0, len(tweets), chunksize)]:
    tweetCoord = []
    for tweet in chunk:
        words = tweet.split()
        nrank = sum([1 if negwords.get(w) else 0 for w in words])
        prank = sum([1 if poswords.get(w) else 0 for w in words])
        tweetCoord.append((nrank, prank))
    tbx.append(st.mean([t[0] for t in tweetCoord]))
    tby.append(st.mean([t[1] for t in tweetCoord]))
print("Plotting...")
plt.plot(tbx, tby, 'bo')
plt.xlabel('negative word freq.')
plt.ylabel('positive word freq.')
plt.show()
print(tbx)
print(tby)