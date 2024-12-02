from art import logo, vs
from game_data import data
import random


#print(logo)

score = 0

random_choice_a = random.choice(data)
follower_count_a = random_choice_a.get("follower_count")
print(follower_count_a)

random_choice_b = random.choice(data)
follower_count_b = random_choice_b.get("follower_count")
print(follower_count_b)

if follower_count_a > follower_count_b:
    score += 1
    print(score)
