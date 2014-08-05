#!/usr/bin/python


"""
TheBasics.py
"""


from random import random


def flip_a_fair_coin():
    """ Flips a fair coin """

    # The default behaviour of the random function is to
    # generate float random numbers between 0 and 1 with
    # equal probability, that is uniformely distributed
    # among the possible values
    random_number_from_uniform = random()

    if random_number_from_uniform < 0.5:
        return 'Head'
    else:
        return 'Tail'


def guess_a_baby():
    """ Guess whether it's a boy or a girl """

    # Then we can model whatever we want
    random_number_from_uniform = random()

    if random_number_from_uniform < 0.5:
        return 'It\'s a Boy'
    else:
        return 'It\'s a Girl'


def example_flip_a_coin(fairness=0.5):
    """ Flips a coin in an informative way"""

    if fairness < 0 or fairness > 1:
        return 'fairness must be inside [0, 1]'

    # Including unfair coins
    random_number_from_uniform = random()

    if random_number_from_uniform < fairness:
        return 'Head'
    else:
        return 'Tail'


def main():
    """ TheBasics.py """

    print 'The flip of a fair coin:', flip_a_fair_coin()
    print 'Guessing babies:', guess_a_baby()
    print 'The flip of a another fair coin:', example_flip_a_coin(fairness=0.5)
    print 'The flip of a unfair coin:', example_flip_a_coin(fairness=0.2)


if __name__ == '__main__':

    main()

