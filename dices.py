import numpy as np


def probability_of_sum(total:int, dice1, dice2):

    """
    Brief: 
    Basic probability - Die cast
    Suppose a pair of fair 6-sided dice are thrown. 
    What is the probability that the sum of the rolls is 6? (Answer as a simple fraction of integers)
    reference: https://statweb.stanford.edu/~susan/courses/s60/split/node65.html
    """

    n = dice1.shape[0]
    m = dice2.shape[0]

    comb = n * m
    count = 0

    for i in dice1:
        for j in dice2:
            sum = int(i + j)
            if sum == total:
                count += 1
    
    prob = count / comb
    
    return print("{:.2%}".format(prob))
            
# define the dice as a linear array of 1 to 6, all integers
dice1 = np.linspace(1,6,6,dtype=int)

# call the function above with the total for which we would like to calculate the probability with 2 dices
prob = probability_of_sum(6, dice1, dice1)




