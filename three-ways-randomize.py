# The random module 

# randint()
# choice()
# shuffle()

# import random 

import random
random.randint(1, 10)
random.randint(100, 1000)
random.randint(55, 59)
random.randint(-10,0)

# choice

pet = ["cats", "dog", "bird", "dinosaur"]
random.choice(pets)
random.choice(pets)
random.choice(pets)
random.choice(pets)


# shuffle()
pets = ["cat","dog","bird", "dinosaur"]
random.shuffle(pets)
pets
['dinosaur', 'bird', 'cat', 'dog']
random.shuffle(pets)
pets
['cat','dinosaur','dog', 'bird']
