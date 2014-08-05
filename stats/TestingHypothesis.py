#!/usr/bin/python


"""
TestingHypothesis.py
"""


from scipy import stats

from FlippingCoins import flip_a_coin


def example_test_coin_fairness(number_of_flips, fairness=0.5, significance_level=0.95):
    """ Two-sided test for the null hypothesis that the coin is fair """

    results = [flip_a_coin(fairness) for flip in range(number_of_flips)]

    # Test if mean of random sample is equal to true mean (here 0.5 - fair coin)
    t_statistic, prob = stats.ttest_1samp(results, 0.5)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'The coin is fair'
    else:
        return 'The coin is unfair'


def example_compare_two_coins(number_of_flips, fairness_1=0.5, fairness_2=0.5, significance_level=0.95):
    """ Two-sided test for the null hypothesis that 2 coins are equal """

    results_1, results_2 = [], []
    for _ in range(number_of_flips):
        results_1.append(flip_a_coin(fairness_1))
        results_2.append(flip_a_coin(fairness_2))

    # If equal_var=True: assumes equal population variances.
    # If equal_var=False, perform Welch t-test
    t_statistic, prob = stats.ttest_ind(results_1, results_2, equal_var=False)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Coins are equal'
    else:
        return 'Coins are not equal'


def compare_two_means(list_of_values_1, list_of_values_2, significance_level=0.95):
    """ Two-sided test for the null hypothesis that 2 means are equal """

    # If equal_var=True: assumes equal population variances.
    # If equal_var=False, perform Welch t-test
    t_statistic, prob = stats.ttest_ind(list_of_values_1, list_of_values_2, equal_var=False)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Means are equal'
    else:
        return 'Means are not equal'


def example_test_single_proportion(number_of_flips, fairness=0.5, significance_level=0.95):
    """ Two-sided test for the null hypothesis that a proportion is equal to 0.5 """

    results = [flip_a_coin(fairness) for flip in range(number_of_flips)]
    success = sum(results)
    failure = len(results) - success

    # Exact two-sided test of the null hypothesis that the probability of success
    # in a Bernoulli experiment is 0.5 (here, fair coin)
    prob = stats.binom_test([success, failure], p=0.5)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'The proportion is equal to target'
    else:
        return 'The proportion is not equal to target'


def example_compare_two_proportions(number_of_flips, fairness_1=0.5, fairness_2=0.5,
                                    significance_level=0.95):
    """ Two-sided test for the null hypothesis that 2 proportions are equal """

    results_1, results_2 = [], []
    for _ in range(number_of_flips):
        results_1.append(flip_a_coin(fairness_1))
        results_2.append(flip_a_coin(fairness_2))

    # Two-sided test of whether 2 samples are drawn from the same distribution and parameters or not.
    ks_statistic, prob = stats.ks_2samp(results_1, results_2)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportions are equal'
    else:
        return 'Proportions are not equal'


def main():
    """ TestingHypothesis.py """

    print 'Testing the fairness of a fair coin:', example_test_coin_fairness(
                                                    number_of_flips=1000,
                                                    fairness=0.5)
    print 'Testing the fairness of an unfair coin:', example_test_coin_fairness(
                                                    number_of_flips=1000,
                                                    fairness=0.3)
    print 'Comparing equal coins:', example_compare_two_coins(
                                                    number_of_flips=1000,
                                                    fairness_1=0.5,
                                                    fairness_2=0.5)
    print 'Comparing unequal coins:', example_compare_two_coins(
                                                    number_of_flips=1000,
                                                    fairness_1=0.5,
                                                    fairness_2=0.3)

    print 'Testing single proportion:', example_test_single_proportion(
                                                    number_of_flips=1000,
                                                    fairness=0.5)
    print 'Comparing two equal proportions:', example_compare_two_proportions(
                                                    number_of_flips=1000,
                                                    fairness_1=0.5,
                                                    fairness_2=0.5)
    print 'Comparing two unequal proportions:', example_compare_two_proportions(
                                                    number_of_flips=1000,
                                                    fairness_1=0.5,
                                                    fairness_2=0.3)


if __name__ == '__main__':

    main()

