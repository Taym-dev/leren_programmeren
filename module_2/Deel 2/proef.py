pizza_lijst = [
    {"type": "Margherita", "diameter": 30},
    {"type": "Pepperoni", "diameter": 36},
    {"type": "Vegetarian", "diameter": 32},
    {"type": "Hawaiian", "diameter": 40},
    {"type": "BBQ Chicken", "diameter": 38},
    {"type": "Meat Lovers", "diameter": 42},
    {"type": "Mushroom", "diameter": 34},
    {"type": "Spinach and Feta", "diameter": 36},
    {"type": "Supreme", "diameter": 44},
    {"type": "Buffalo Chicken", "diameter": 35}
]
sorted_pizza_low_to_high = sorted(pizza_lijst, key=lambda x: x['diameter'],reverse=True)
print(sum(pizzas['diameter']for pizzas in pizza_lijst))

print(sorted_pizza_low_to_high)