# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# Get text
# Trim whitespaces
# Calculate frequency

# Get text

import re

if __name__ == "__main__":

  mapping = {
    11.53: "E",
     9.75: "T",
     8.46: "A",
     8.08: "O",
     7.71: "H",
     6.73: "N",
     6.29: "R",
     5.84: "I",
     5.56: "S",
     4.74: "D",
     3.92: "L",
     3.08: "W",
     2.59: "U",
     2.48: "G",
     2.42: "F",
     2.19: "B",
     2.18: "M",
     2.02: "Y",
     1.58: "C",
     1.08: "P",
     0.84: "K",
     0.59: "V",
     0.17: "Q",
     0.07: "J",
     0.07: "X",
     0.03: "Z"
  }

  file = open("./ciphertext.txt", "r")
  content = file.read()

  # print(content.replace(" ", "").replace("\n", ""))
  clean_content = re.sub(r"\s+", "", content)
  store = {}
  word_count = 0
  for character in clean_content:
    if character.isalpha() != True:
      continue

    if character not in store:
      store[character] = 1
    else:
      store[character] += 1

    word_count += 1
  # Get most frequent letter

  for item in store:
    store[item] = round((store[item] / word_count) * 100, 2)

  key_value = sorted(list(store.items()), key = lambda item: item[1], reverse = True)

  print(key_value)
  decripted_content = content
  # Got the correct mapping, don't know how to replace
  cache = {}
  for index in reversed(range(len(key_value))):
    print(f"Replacing {key_value[index]}")
    print(f"With {mapping[key_value[index][1]]}")
    decripted_content = re.sub(f"{key_value[index][0]}", mapping[key_value[index][1]], decripted_content)
    # break

  print(decripted_content)