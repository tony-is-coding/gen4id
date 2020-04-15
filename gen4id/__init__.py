import random

from .increase_gen import IncreaseGen


def random_str(seq: str) -> str:
    """shuffle a string"""
    seq = list(seq)
    random.shuffle(seq)
    return "".join(seq)


__all__ = ['IncreaseGen', 'random_str']
