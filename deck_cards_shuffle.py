import random, itertools

print("Program to Shuffle Deck of Cards")

print("")

deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Heart", "Diamond"]))
print(deck)
print("")
for i in range(5):
  print(deck[i][0],"of", deck[i][1])