# Your code here
import re

store = {}

def printHistogram(word, count):
  print(f"{word}:{' ' * (16  - len(word))}{'#' * count}")

with open('./robin.txt', 'r') as file:
  for line in file:
    for word in line.split():
      word = re.sub('\W+', '', word.lower())

      if not word.isalpha():
        continue

      if word not in store:
        store[word] = 1
      else:
        store[word] += 1

store = sorted(list(store.items()), key = lambda item: item[1], reverse = True)

for word in range(len(store) - 1):
  printHistogram(store[word][0], store[word][1])