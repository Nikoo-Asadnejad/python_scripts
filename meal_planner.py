import random

proteins = ['chicken breast', 'tofu', 'boiled egg', 'lentils']
veggies = ['spinach', 'zucchini', 'broccoli', 'carrots']
carbs = ['quinoa', 'brown rice', 'sweet potato', 'oats']
spices = ['turmeric', 'paprika', 'cumin', 'garlic']

def generate_meal():
    return f"Meal: {random.choice(proteins)}, {random.choice(veggies)}, {random.choice(carbs)} with {random.choice(spices)}"

print(generate_meal())
