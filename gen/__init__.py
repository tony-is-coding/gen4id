from abc import ABCMeta


class Generator:

    def encode(self, ):
        raise NotImplementedError

    def decode(self):
        raise NotImplementedError


class Digit:

    def add(self):
        raise NotImplementedError

    def check(self):
        raise NotImplementedError
