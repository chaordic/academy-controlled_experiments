#!/usr/bin/python


"""
TestingHypothesisMath.py
"""


from numpy import mean, std, sqrt
from scipy import stats

from FlippingCoins import flip_some_coins_lots_of_times


def example_test_a_mean(a_list_of_values, target=0.5, significance_level=0.95):
    """ The math behind testing a single mean """

    # sample size
    n = len(a_list_of_values)
    # sample standard deviation
    sigma = std(a_list_of_values)
    # sample mean
    mu = mean(a_list_of_values)

    # standard error
    se = sigma/sqrt(n)
    # t-statistic
    t = (mu-target)/se
    # degrees of freedom
    df = n-1

    # check in statistical table
    prob = stats.t.sf(t, df)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Mean is equal to target'
    else:
        return 'Mean is not equal to target'


def example_compare_two_means(list_of_values_1, list_of_values_2, significance_level=0.95):
    """ The math behind comparing two means """

    # sample size
    n1 = len(list_of_values_1)
    n2 = len(list_of_values_2)
    # sample standard deviation
    sigma1 = std(list_of_values_1)
    sigma2 = std(list_of_values_2)
    # sample mean
    mu1 = mean(list_of_values_1)
    mu2 = mean(list_of_values_2)
    # sample variance
    s12 = sigma1**2
    s22 = sigma2**2

    # standard error
    se = sqrt((s12/n1)+(s22/n2))
    # t-statistic
    t = (mu1-mu2)/se
    # degrees of freedom
    df = round(min(n1, n2)-1)

    # check in statistical table
    prob = stats.t.sf(abs(t), df)*2

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Means are equal'
    else:
        return 'Means are not equal'


def example_test_a_proportion(p=0.1, n=100, target=0.1, significance_level=0.95):
    """ The math behind testing a single proportion """

    # sample standard deviation
    sigma = sqrt(p*(1-p)/n)

    # z-score
    z = (p-target)/sigma

    # check in statistical table
    prob = stats.zprob(z)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical proportions
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportion is equal to target'
    else:
        return 'Proportion is not equal to target'


def example_compare_two_proportions(p1=0.1, n1=100, p2=0.1, n2=100, significance_level=0.95):
    """ The math behind comparing two proportions """

    # overall sample proportion
    p = ((p1*n1)+(p2*n2))/(n1+n2)
    # standard error
    se = sqrt(p*(1.-p)*((1./n1)+(1./n2)))
    # z-score
    z = (p1-p2)/se

    # check in statistical table
    prob = stats.zprob(z)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical proportions
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportions are equal'
    else:
        return 'Proportions are not equal'


def main():
    """ TestingHypothesisMath.py """

    results = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.5)
    print 'Testing a single mean:', example_test_a_mean(
                                        results,
                                        target=500,
                                        significance_level=0.95)

    results_1 = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.5)
    results_2 = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.5)
    print 'Comparing two equal means:', example_compare_two_means(
                                        results_1,
                                        results_2)

    results_2 = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.3)
    print 'Comparing two unequal means:', example_compare_two_means(
                                        results_1,
                                        results_2)

    print 'Testing a single proportion:', example_test_a_proportion(p=0.1,
                                                                    n=100,
                                                                    target=0.1)

    print 'Comparing two equal proportions:', example_compare_two_proportions(p1=0.1,
                                                                              n1=1000,
                                                                              p2=0.1,
                                                                              n2=1000)

    print 'Comparing two unequal proportions:', example_compare_two_proportions(p1=0.1,
                                                                                n1=1000,
                                                                                p2=0.15,
                                                                                n2=1000)


if __name__ == '__main__':

    main()

