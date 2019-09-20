import random as rand

list_id = ['L', '|_', '/_', '!', 'l']

lower_bound = len(list_id) * 10 // 100
upper_bound = len(list_id) * 60 // 100

sampled = rand.sample(list_id, rand.randint(lower_bound, upper_bound))

print(sampled)
