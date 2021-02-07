# Importing required libraries
 
import numpy as np
import scipy.stats
import math

def normal_dist(x , mean , sd):

    """
    Calculates a normal distribution in a variate x,
    with mean mu (mean) and variance sigma^2 (sd)
    as a statistic distribution with probability density function.
    source: https://mathworld.wolfram.com/NormalDistribution.html
    """
    
    prob_density = (1/((2*np.pi*sd**2)**(1/2))) * (np.exp(-0.5*((x-mean)/sd)**2))

    return prob_density
 

def stackoverflow_normpdf(x, mean, sd):

    """
    Another alternative from: https://stackoverflow.com/a/12413491
    This uses the formula found here: http://en.wikipedia.org/wiki/Normal_distribution#Probability_density_function
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


def scipy_norm_pdf(x, mean, var):

    #Using scipy library for calculating the normal probability distribution
    # loc being the mean, varies for probability of 'yes' vs 'no'
    # scale being the variance, varies for probability of 'yes' vs 'no'
    # use cdf to indicate the value at which we would like to calculate the probability; e.g. x = 4 in this particular scenario

    prob = scipy.stats.norm(mean, var).pdf(x)
    prob_dist = scipy.stats.norm(mean, var)

    return prob, prob_dist
 

#using the function we have created
our_prob_dist_yes = normal_dist(4, 10, 36)
our_prob_dist_no = normal_dist(4, 0, 36)

#using the alternative method from stackoverflow and wikipedia formulation
alt_prob_dist_yes = stackoverflow_normpdf(4, 10, 36)
alt_prob_dist_no = stackoverflow_normpdf(4, 0, 36)

#using scipy library to compare/validate above function
scipy_prob_yes, scipy_prob_dist_yes = scipy_norm_pdf(4, 10, 36)
scipy_prob_no, scipy_prob_dist_no = scipy_norm_pdf(4, 0, 36)
