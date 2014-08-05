#!/usr/bin/python


"""
ConfidenceIntervals.py
"""


from numpy import mean, std
from scipy import stats

from FlippingCoins import flip_some_coins_lots_of_times


def get_confidence_intervals_using_the_three_sigma_rule(a_list_of_values, number_of_standard_deviations=2):
    """
    Gets the confidence interval using the three sigma rule.
        1 standard deviation approx 0.6827
        2 standard deviation approx 0.9545
        3 standard deviation approx 0.9973
        5 standard deviation approx 1-(1/(3.5*10**6)) - Higgs boson \o/
    """

    sample_standard_deviation = std(a_list_of_values)
    sample_mean = mean(a_list_of_values)

    lower_bound = sample_mean - (number_of_standard_deviations * sample_standard_deviation)
    upper_bound = sample_mean + (number_of_standard_deviations * sample_standard_deviation)
    return lower_bound, upper_bound


def get_confidence_intervals_using_the_normal_distribution(a_list_of_values, significance_level=0.95):
    """ Gets the confidence interval using the normal distribution"""

    sample_standard_deviation = std(a_list_of_values)
    sample_mean = mean(a_list_of_values)

    lower_bound, upper_bound =  stats.norm.interval(significance_level,
                                                sample_mean, sample_standard_deviation)
    return lower_bound, upper_bound


def get_confidence_intervals_using_the_quantiles(a_list_of_values, significance_level=0.95):
    """ Gets the confidence interval using the quantiles"""

    alpha = 1 - significance_level
    lower_bound = stats.scoreatpercentile(a_list_of_values, 100*alpha/2)
    upper_bound = stats.scoreatpercentile(a_list_of_values, 100*(1-alpha/2))
    return lower_bound, upper_bound


def main():
    """ ConfidenceIntervals.py """

    results = flip_some_coins_lots_of_times(number_of_times=100000,
                                            number_of_flips=1000,
                                            fairness=0.5)
    print 'Three-sigma:', get_confidence_intervals_using_the_three_sigma_rule(results)
    print 'Normal dist.:', get_confidence_intervals_using_the_normal_distribution(results)
    print 'Quantiles:', get_confidence_intervals_using_the_quantiles(results)


if __name__ == '__main__':

    main()

