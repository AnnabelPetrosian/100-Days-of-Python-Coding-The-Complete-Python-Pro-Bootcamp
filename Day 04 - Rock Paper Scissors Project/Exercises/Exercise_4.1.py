# Heads or Tails
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

random_coin_sides = random.randint(0, 1)

if random_coin_sides == 1:
    print("Heads")
else:
    print("Tails")