import collections

start_word = ["hi","hey","yo"]

maxlen = 1000

word_freqs =collections.Counter()

with open('c:/Users/user/Desktop/Testing.txt',"r+",encoding="UTF-8") as f:
    for line in f:
        words = line.lower().split(" ")

        if len(words)>maxlen:
            maxlen = len(words)
        for word in words:
            if not(word in start_word):
                word_freqs[word]+=1

print(word_freqs.most_common(20))