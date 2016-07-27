import sys
import matplotlib.pyplot as plt
import statistics as st

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])

print("Loading Files...")

f = open('negative-words.txt', errors='replace')
negwords = f.read().split(';')[-1].split()
negwords = {a:1 for a in negwords}
f.close()

f = open('positive-words.txt', errors='replace')
poswords = f.read().split(';')[-1].split()
poswords = {a:1 for a in poswords}
f.close()

f = open(sys.argv[1])
tweets = f.read().split('\n')
f.close()

tbx = []
tby = []
chunksize = int(sys.argv[2])
print("Processing Tweets...")
for chunk in [tweets[i:i+chunksize] for i in range(0, len(tweets), chunksize)]:
    tweetCoord = []
    for tweet in chunk:
        words = tweet.split()
        nrank = sum([1 if negwords.get(w) else 0 for w in words])/(len(words)+1.0)
        prank = sum([1 if poswords.get(w) else 0 for w in words])/(len(words)+1.0)
        tweetCoord.append((nrank, prank))
    tbx.append(st.mean([t[0] for t in tweetCoord]))
    tby.append(st.mean([t[1] for t in tweetCoord]))

print("Saving...")
f = open(str(sys.argv[1]) + "_results", "w")
f.write("\n".join([str(x) for x in list(zip(tbx,tby))]))
f.close()

print("Plotting...")
plt.plot(tbx, tby, 'bo')

f = open(sys.argv[3])
tweets = f.read().split('\n')
f.close()

tbx = []
tby = []
chunksize = int(sys.argv[4])
print("Processing Tweets...")
for chunk in [tweets[i:i+chunksize] for i in range(0, len(tweets), chunksize)]:
    tweetCoord = []
    for tweet in chunk:
        words = tweet.split()
        nrank = sum([1 if negwords.get(w) else 0 for w in words])/(len(words)+1.0)
        prank = sum([1 if poswords.get(w) else 0 for w in words])/(len(words)+1.0)
        tweetCoord.append((nrank, prank))
    tbx.append(st.mean([t[0] for t in tweetCoord]))
    tby.append(st.mean([t[1] for t in tweetCoord]))

print("Saving...")
f = open(str(sys.argv[3]) + "_results", "w")
f.write("\n".join([str(x) for x in list(zip(tbx,tby))]))
f.close()

print("Plotting...")
plt.plot(tbx, tby, 'ro')
plt.xlabel('negative word freq.')
plt.ylabel('positive word freq.')
plt.show()
print(tbx)
print(tby)