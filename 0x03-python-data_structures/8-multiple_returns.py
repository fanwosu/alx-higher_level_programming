#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n < 1:
        return (None)
    return (n, sentence[0])
