# Importing required libraries
 
import numpy as np
import scipy.stats
import math
from scipy.stats import multivariate_normal


def normal_dist(x , mean , var):

    """
    Calculates a normal distribution in a variate x,
    with mean mu (mean) and variance sigma^2 (sd)
    as a statistic distribution with probability density function.
    source: https://mathworld.wolfram.com/NormalDistribution.html

    note that variance is std^2, e.g. a distribution with variance equal to 36, has a std dev of 6 (36 = 6^2).

    sigma^2 = sd, standard deviation
    sigma = variance
    """
    
    prob_density = (1/((2*np.pi*var)**(1/2))) * (np.exp(-0.5*((x-mean)**2/var)))

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


def scipy_norm_pdf(x, mean, sd):

    #Using scipy library for calculating the normal probability distribution
    # loc being the mean, varies for probability of 'yes' vs 'no'
    # scale being the sd (not variance), varies for probability of 'yes' vs 'no'
    # use cdf to indicate the value at which we would like to calculate the probability; e.g. x = 4 in this particular scenario

    prob = scipy.stats.norm(mean, sd).pdf(x)
    prob_dist = scipy.stats.norm(mean, sd)

    return prob, prob_dist
 

x = 4
mean_yes = 10
mean_no = 0
var = 36
sd = var**(1/2)


#using the function we have created

our_prob_dist_yes = normal_dist(x, mean_yes, var)
our_prob_dist_no = normal_dist(x, mean_no, var)

print(f"Using the function we have created, for \n X = {x} \n mean_yes = {mean_yes} \n mean_no= {mean_no} n var = {var} \n the probability for Yes is {our_prob_dist_yes} \n and the probability for No is {our_prob_dist_no}")


#using the alternative method from stackoverflow and wikipedia formulation; note you are passing on here sd and not variance (e.g. passing on sd and not var = sd^(2)
alt_prob_dist_yes = stackoverflow_normpdf(x, mean_yes, sd)
alt_prob_dist_no = stackoverflow_normpdf(x, mean_no, sd)

print(f"Using the alternative method from stackoverflow and wikipedia formulation, for \n X = {x} \n mean_yes = {mean_yes} \n mean_no = {mean_no} \n var = {var} the probability for Yes is {alt_prob_dist_yes} \n and the probability for No is {alt_prob_dist_no}")


#using scipy library to compare/validate above function
scipy_prob_yes, scipy_prob_dist_yes = scipy_norm_pdf(x, mean_yes, sd)
scipy_prob_no, scipy_prob_dist_no = scipy_norm_pdf(x, mean_no, sd)

print(f"Using scipy library to compare/validate above function, for \n X = {x} \n mean_yes = {mean_yes} \n mean_no = {mean_no} \n var = {var} the probability for Yes is {scipy_prob_yes} \n and the probability for No is {scipy_prob_no}")