from fruitmand import fruitmand
import random

# def print_random_fruit(n):
#     for _ in range(n):
#         random_fruit = random.choice(fruitmand)
#         print(random_fruit['name'])



aantal_keer = int(input("Hoe vaak wil je een willekeurige fruitnaam laten printen? "))

for _ in range(aantal_keer):
    random_fruit = random.choice(fruitmand)
    print(random_fruit['name'])



