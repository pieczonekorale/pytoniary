import random
import math

def gen_random(n):
    data=[]
    for i in range(0,n):
        data.append(random.randint(0,n-1))
    return data

def gen_almost_sorted(n):
    data=[]
    for i in range(0,n):
        ew=int(i)
        data.append(random.randint(int(ew/1.05),ew+1))
    return data


def gen_almost_reverse(n):
    data=[]
    for i in range(0,n):
        ew=n-int(i)
        data.append(random.randint(int(ew/1.7),ew+1))
    return data

def gen_gauss(n):
    mu = n
    sigma = n/2
    data=[]
    for i in range(0,n):
        data.append(random.gauss(mu, sigma))
    return data

def gen_random_copies(n):
    data=[]
    k=int(math.sqrt(n))
    for i in range(0,n):
        data.append(random.randint(0,k))
    return data

