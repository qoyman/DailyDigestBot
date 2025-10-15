from src.services.quotes import random_quote, QUOTES

def test_random_quote_returns_known_quote():
    q = random_quote()
    assert q in QUOTES