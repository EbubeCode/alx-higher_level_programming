#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght:
        return lenght, sentence[0]
    return 0, None
