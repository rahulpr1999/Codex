import random
import string
print("Generate a random alphabetical character:")
print(random.choice(string.ascii_letters))
print("\nGenerate a random alphabetical string:")
max_length = 255
random_string = ""
for _ in range(random.randint(1, max_length)):
    random_string += random.choice(string.ascii_letters)
print(random_string)
print("\nGenerate a random alphabetical string of a fixed length:")
fixed_length_string = ""
for _ in range(10):
    fixed_length_string += random.choice(string.ascii_letters)
print(fixed_length_string)
