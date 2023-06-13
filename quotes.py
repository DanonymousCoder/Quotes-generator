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
# Generate and print a random quote
quote = get_random_quote()
