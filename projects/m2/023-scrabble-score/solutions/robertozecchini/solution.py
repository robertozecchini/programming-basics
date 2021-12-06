#!/usr/bin/env python3

# solution for Scrabble-Score project

import sys

points = {
    'A':1,
    'B':3,
    'C':3,
    'D':2,
    'E':1,
    'F':4,
    'G':2,
    'H':4,
    'I':1,
    'J':8,
    'K':5,
    'L':1,
    'M':3,
    'N':1,
    'O':1,
    'P':3,
    'Q':10,
    'R':1,
    'S':1,
    'T':1,
    'U':1,
    'V':4,
    'W':4,
    'X':8,
    'Y':4,
    'Z':10
    }

def ScrabbleScore(word):
    score = 0
    for letter in word:
        score += points.get(letter.upper(), 0)
    return score

def main():
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input("Type a word: ")
    score = ScrabbleScore(word)
    print(f"The scrabble score for word \"{word}\" is {score}.")

if __name__ == "__main__":
    main()