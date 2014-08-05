#!/usr/bin/python


"""
FlippingCoins.py
"""


from numpy.random import binomial
from matplotlib.pyplot import hist, show


def flip_a_coin(fairness=0.5):
    """ Flips a coin and returns 1 for heads and 0 for tails """

    # binomial function is a nice way of working with the binomial distribution
    return binomial(1, fairness)


def flip_some_coins(number_of_flips, fairness=0.5):
    """ Flips some coins and prints the numbers of heads and tails """

    number_of_heads = binomial(number_of_flips, fairness)
    number_of_tails = number_of_flips - number_of_heads
    return 'number of heads:', number_of_heads, 'number of tails:', number_of_tails


def flip_some_coins_lots_of_times(number_of_times, number_of_flips=1000, fairness=0.5, plot=False):
    """ Flips some coins lots of times """

    results = binomial(number_of_flips, fairness, number_of_times)
    if plot:
        hist(results, 1000); show()
    return results


def main():
    """ FlippingCoins.py """

    print 'Binary flip of a coin:', flip_a_coin()
    print 'Flipping a thousand coins:'
    print flip_some_coins(1000)
    print 'Flipping a hundred thousand coins:'
    print flip_some_coins(100000)
    print 'Plotting a thousand coins flipped a thousand times'
    flip_some_coins_lots_of_times(1000, plot=True)
    print 'Plotting a thousand coins flipped a hundred thousand times'
    flip_some_coins_lots_of_times(100000, plot=True)


if __name__ == '__main__':

    main()

