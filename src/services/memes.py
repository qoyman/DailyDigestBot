import random

MEMES = [
    '<b>Random Meme</b> — https://i.imgur.com/31aD4Xy.jpeg',
    '<b>Random Meme</b> — https://i.imgur.com/6Xj2b9a.png',
    '<b>Random Meme</b> — https://i.imgur.com/4AiXzf8.jpeg',
]

def random_meme() -> str:
    return random.choice(MEMES)