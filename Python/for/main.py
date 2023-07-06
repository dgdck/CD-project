from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(countries):
    short_list = []
    length = []
    for country in countries:
        length.append(len(country))
    for country in countries:
        if len(country) == min(length):
            short_list.append(country)
    return short_list


def most_vowels(countries):
    vowels_leaderboard = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_top3 = []

    for country in countries:
        count = 0
        for x in country.lower():
            if x in vowels:
                count += 1
        vowels_leaderboard.append([count, country])
    vowels_leaderboard.sort(reverse=True)
    for x in vowels_leaderboard:
        if len(vowels_top3) < 3:
            vowels_top3.append(x[1])
    return vowels_top3


def alphabet_set(countries):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    alphabet_countries = []
    length = []
    for country in countries:
        length.append([len(country), country])
    length.sort(reverse=True)
    for x in length:
        del x[0]
    countries = length
    for set in countries:
        for country in set:
            for letter in alphabet:
                if letter.lower() in country:
                    if letter.lower() not in alphabet_list:
                        alphabet_list.append(letter)
                        if country not in alphabet_countries:
                            alphabet_countries.append(country)

    return alphabet_countries
# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`


if __name__ == "__main__":
    countries = get_countries()

    """Write the calls to your functions here."""
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)
