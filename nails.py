import random

with open("nails.txt", "r") as file:
    allText = file.read()
    words = allText.splitlines()
    
print(random.choices(words, k=3))