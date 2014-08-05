#!/usr/bin/python


"""
ThompsonSampling.py
"""


import operator
from random import random
from scipy import stats
from matplotlib.pyplot import plot, legend, xlabel, show


def simulate_bandit(number_of_requests=1000):
    """
    This function simulates a flow of requests, the bandit procedure called
    Thompson Sampling for choosing alternatives, and the conversion rate of
    a hypothetical website
    """

    # First let's build the alternatives (Bandit's arms)

    # Note that we have to define the expected conversion
    # rate of each alternative, quantity that is unknown
    # in actual test applications
    alternatives = {
        'A': {
            'success': 1,
            'failure': 1,
            'simulated_conversion': 0.1,
            'requests_so_far': 0.,
            'tmp_random_beta': 0
        },
        'B': {
            'success': 1,
            'failure': 1,
            'simulated_conversion': 0.1,
            'requests_so_far': 0.,
            'tmp_random_beta': 0
        },
        'C': {
            'success': 1,
            'failure': 1,
            'simulated_conversion': 0.1,
            'requests_so_far': 0.,
            'tmp_random_beta': 0
        }
    }

    # After the simulation, we'll plot the proportions of requests
    # received by each alternative during time
    proportions_in_time = []

    # For each simulated alternative
    for _ in range(1, number_of_requests):

        # Let's choose one according to the Thompson Sampling procedure
        for alternative in alternatives:
            # Get history so far
            success = alternatives[alternative]['success']
            failure = alternatives[alternative]['failure']
            # Store alternative's own number from Beta
            alternatives[alternative]['tmp_random_beta'] = stats.beta.rvs(success, failure)

        # Sort by random number from Beta
        chosen_alternative = sorted(alternatives.iteritems(), 
                                key=lambda (x, y): y['tmp_random_beta'],
                                reverse=True)[0][0]

        # Feedback is necessary, so we update success and failure
        alternatives[chosen_alternative]['requests_so_far'] += 1

        # Store for plotting
        list_of_alternatives_requests = [alternatives[alternative]['requests_so_far']
                                            for alternative in alternatives]
        requests_so_far = sum(list_of_alternatives_requests)
        if requests_so_far == 1000:
            # Store
            proportions_to_plot = [x/requests_so_far for x in list_of_alternatives_requests]
            proportions_in_time.append(proportions_to_plot)
            # Clear
            for alternative in alternatives:
                alternatives[alternative]['requests_so_far'] = .0

        # Fake (simulated) conversion
        if random() < alternatives[chosen_alternative]['simulated_conversion']:
            alternatives[chosen_alternative]['success'] += 1
        else:
            alternatives[chosen_alternative]['failure'] += 1

    plot(proportions_in_time); legend(alternatives.keys()); xlabel('thousands'); show()


def main():
    """ ThompsonSampling.py """

    simulate_bandit(number_of_requests=100000)


if __name__ == '__main__':

    main()

