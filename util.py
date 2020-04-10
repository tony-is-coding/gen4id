import random


def get_random_str(seq: str) -> str:
    """shuffle a string"""
    seq = list(seq)
    random.shuffle(seq)
    return "".join(seq)
