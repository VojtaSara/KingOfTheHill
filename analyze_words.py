from collections import Counter
from random import choices

with open('input.txt', encoding="utf-8") as f:
    lines = f.readlines()
    all_words = []
    for line in lines:
        all_words += line.split()
    
    Counter = Counter(all_words)
    most_occur = Counter.most_common(500)
    most_occur_separated = list(map(list, zip(*most_occur)))
    for i in range(15):
        print(choices(most_occur_separated[0],most_occur_separated[1])[0]) 

