# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/20/2022
# Description: A function that takes as a parameter a string and returns a dictionary
# that tabulates how many of each letter is in that string.

def count_letters(words):
    """A functon that counts the number of each letter in a string"""
    letter_count = {}

    for letter in words:
        if letter.lower() >= "a" and letter.lower() <= "z":
            letter = letter.upper()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count
