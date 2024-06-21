#Want to generate random choices of Heads or Tail

#First way is to import random module
# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

#Alternative to using import alone
# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)

#Now want to generate random # 1-10 with randint()
# import random

# number = random.randint(1,10)
# #print(number)

#Use random.shuffle() -- shuffles order within list
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
    
