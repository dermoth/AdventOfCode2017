#!/usr/bin/env python3

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        dic = set()
        for word in line.split():
            if word in dic:
                dic = None
                break
            dic.add(word)
        if dic is not None:
            count += 1

print(count)

