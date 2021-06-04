import random, math


def generate_data(size):
    n = 5
    m = 0.5
    mu, sigma = n ** 2, m/3
    return [random.gauss(mu, sigma) for _ in range(size)]


def variance(ls):
    avg = sum(ls) / len(ls)
    variance = sum(map(lambda x: (x-avg) ** 2, ls)) / len(ls)

    return variance


def Gaussian_distritubion(mean, cov):

    w = np.random.multivariate_normal(mean, cov)

    return w


mean:list=[1,2,3]
cov:list=np.diag([1,1,2])

wG = Gaussian_distritubion(mean, cov)

res = np.mean(np.dot(mean, wG))

x = wG[0]+ 2 * wG[2]


print(math.sqrt(variance(x)))
