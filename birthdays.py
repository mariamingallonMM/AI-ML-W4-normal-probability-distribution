import numpy as np


def prob_not(n:int = 20, days:int = 365):

    """
    probability of the birth dates not coinciding
    n : number of students in class
    days : days in the year (default 365)
    formulation:
        d! / ((d**n) * (365 - n)!)

    source : https://en.wikipedia.org/wiki/Birthday_problem

    """

    prob_no = np.math.factorial(days) / ((days**n) * np.math.factorial(days - n))


    return print("Probability of not coinciding: ", "{:.2%}".format(prob_no), "\n", "Probability of coinciding: ", "{:.2%}".format(1 - prob_no), "\n")


prob_not(20, 365)
    