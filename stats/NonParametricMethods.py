#!/usr/bin/python


"""
NonParametricMethods.py
"""


from random import random
from numpy import mean
from scipy import stats
from matplotlib.pyplot import hist, show

from FlippingCoins import flip_some_coins_lots_of_times
from ConfidenceIntervals import get_confidence_intervals_using_the_normal_distribution, \
                                get_confidence_intervals_using_the_quantiles
from TestingHypothesis import compare_two_means


def create_random_non_normal_data(sample_size=1000, a=11.3, c=0.4, plot=False):
    """ Create non normal random data from the Generalized Gamma distribution """

    data = stats.gengamma.rvs(a, c, size=sample_size)
    if plot: hist(data, 100); show()
    return data


def test_for_normality(a_list_of_values, significance_level=0.95):
    """ Normality test """

    # Tests the null hypothesis that a sample comes from a normal distribution.
    # It is based on D'Agostino and Pearson's test
    chi2_statistic, prob = stats.normaltest(a_list_of_values)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Data is normal'
    else:
        return 'Data is not normal'


def bootstrap_confidence_intervals(a_list_of_values, bootstrapping_resamples=1000):
    """ Bootstrapping confidence intervals """

    def sample_wr(population, k):
        """ Chooses k random elements (with replacement) from a population """
        n = len(population)
        _random, _int = random, int
        result = [None] * k
        for i in xrange(k):
            j = _int(_random() * n)
            result[i] = population[j]
        return result

    # Bootstrapping
    lower_bounds, upper_bounds = [], []
    for _ in range(bootstrapping_resamples):
        # create resample with the same size as the original
        resample = sample_wr(a_list_of_values, len(a_list_of_values))
        # get confidence interval
        resample_lower_bound, resample_upper_bound = get_confidence_intervals_using_the_quantiles(resample)
        # append to results
        lower_bounds.append(resample_lower_bound)
        upper_bounds.append(resample_upper_bound)

    mean_lower_bound, mean_upper_bound = mean(lower_bounds), mean(upper_bounds)
    return mean_lower_bound, mean_upper_bound


def non_parametric_test_for_difference_of_means(list_of_values_1, list_of_values_2,
                                                    significance_level=0.95):
    """ Mann-Whitney U (non parametric) test for the difference of proportions """

    # Mann-Whitney U test (also called the Mann-Whitney-Wilcoxon (MWW),
    # Wilcoxon rank-sum test, or Wilcoxon-Mann-Whitney test
    z_statistic, prob = stats.mannwhitneyu(list_of_values_1, list_of_values_2)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Means are equal'
    else:
        return 'Means are not equal'


def main():
    """ NonParametricMethods.py """

    print '---------- Normal data ---------------'
    normal_data = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5, plot=True)
    normal_lower_bound, normal_upper_bound = get_confidence_intervals_using_the_normal_distribution(
                                                                                        normal_data)
    print 'normal: len', len(normal_data), 'mean', mean(normal_data)
    print 'Normality test for normal data:', test_for_normality(normal_data)
    print 'Confidence intervals for normal data:', normal_lower_bound, normal_upper_bound
    normal_lower_bound, normal_upper_bound = bootstrap_confidence_intervals(normal_data)
    print 'Bootstrapping confidence intervals for normal data:', normal_lower_bound, normal_upper_bound
    print

    print '---------- Powerlaw data -------------'
    powerlaw_data = create_random_non_normal_data(sample_size=10000, plot=True)
    print 'powerlaw: len', len(powerlaw_data), 'mean', mean(powerlaw_data)
    powerlaw_lower_bound, powerlaw_upper_bound = get_confidence_intervals_using_the_normal_distribution(
                                                                                        powerlaw_data)
    print 'Normality test for powerlaw data:', test_for_normality(powerlaw_data)
    print 'Confidence intervals for powerlaw data:', powerlaw_lower_bound, powerlaw_upper_bound
    powerlaw_lower_bound, powerlaw_upper_bound = bootstrap_confidence_intervals(powerlaw_data)
    print 'Bootstrapping confidence intervals for powerlaw data:', powerlaw_lower_bound, powerlaw_upper_bound
    print

    print '---------- Two equal normal means -----------------'
    data_1 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5)
    data_2 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5)
    print 'Normality based test:', compare_two_means(data_2, data_1)
    print 'Ranksum test        :', non_parametric_test_for_difference_of_means(data_2, data_1)
    print
    print '---------- Two unequal normal means ---------------'
    data_1 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5)
    data_2 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.45)
    print 'Normality based test:', compare_two_means(data_2, data_1)
    print 'Ranksum test        :', non_parametric_test_for_difference_of_means(data_2, data_1)
    print
    print '---------- Two equal non-normal means -------------'
    data_1 = create_random_non_normal_data(sample_size=100000)
    data_2 = create_random_non_normal_data(sample_size=100000)
    print 'Normality based test:', compare_two_means(data_2, data_1)
    print 'Ranksum test        :', non_parametric_test_for_difference_of_means(data_2, data_1)

    print
    print '---------- Two unequal non-normal means -------------'
    data_1 = create_random_non_normal_data(sample_size=100000, a=11.3)
    data_2 = create_random_non_normal_data(sample_size=100000, a=12)
    print 'Normality based test:', compare_two_means(data_2, data_1)
    print 'Ranksum test        :', non_parametric_test_for_difference_of_means(data_2, data_1)


if __name__ == '__main__':

    main()

