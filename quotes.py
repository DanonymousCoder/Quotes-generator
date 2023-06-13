import random


def get_random_quote():
 quotes = [
     "The only way to do great work is to love what you do. - Steve Jobs",
     "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
     "Believe you can and you're halfway there. - Theodore Roosevelt",
     "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
     "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
     "In the middle of every difficulty lies opportunity. - Albert Einstein"
    ]
return random.choice(quotes)
quote = get_random_quote()
print(quotes)
# Generate and print a random quote#

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a random password of length 10
password = generate_password(10)
print("Random Password:", password)
