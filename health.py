import random

health = 50
difficulty = 2

potion_health = int(random.randint( health / 2, health) / difficulty)

health = health + potion_health

print(health)



