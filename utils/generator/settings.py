from numpy.random.mtrand import randint

locales = ('pl', 'en', 'cs')
genres = ['kryminał', 'komedia', 'biografia', 'fantastyka', 'popularno-naukowe']
author_count = 5
publisher_count = 20
multi_author_count = 5
multi_author_chance = 50


def books_of_author_fixed():
    return 5


def books_of_author_random():
    return randint(1, 10)


books_of_author = books_of_author_fixed
card_count = 90