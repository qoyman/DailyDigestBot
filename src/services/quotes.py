import random

QUOTES = [
    "The only way to do great work is to love what you do. — Steve Jobs",
    "It always seems impossible until it’s done. — Nelson Mandela",
    "Whether you think you can or you think you can’t, you’re right. — Henry Ford",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
    "Start where you are. Use what you have. Do what you can. — Arthur Ashe",
]

def random_quote() -> str:
    return random.choice(QUOTES)