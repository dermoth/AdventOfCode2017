#!/usr/bin/env python3

# We know two words are anagrams if they sahre the same count of
# letters. Convert words to letter counts
def word2key26(word):
    wordlist = []
    for letter in range(ord('a'), ord('z')+1):
        count = 0
        for w2l in word:
            if ord(w2l) == letter:
                count += 1
        wordlist.append(count)
    return tuple(wordlist)

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        dic = set()
        for word in line.split():
            key = word2key26(word)
            if key in dic:
                dic = None
                break
            dic.add(key)
        if dic is not None:
            count += 1

print(count)

