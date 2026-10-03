import matplotlib.pyplot as plt
import numpy as np

c = np.linspace(0, 4, 50)
u = -1 * (c - 2) ** 2 + 10
plt.plot(c, u)
plt.xlabel('Consumption')
plt.ylabel('Utility')

def util(c, A, B, C):
    u = -A * (c - B)**2 + C
    return u

def find_max_cons(candidates, A, B, C):
    """
    Find the consumption level that maximizes utility 
    form a sequence of candidates

    Parameters
    -----------
    candidates: list or array-like 
        Sequence of candidate consumtion levels to 
        evaluate
    A, B, C: float
        Parameters of the utility function
    
    Returns
    --------
    u_max
        Maximized utility
    cons_max
        Consumtion at which utility is maximized
    """
    u_max = - np.inf

    for i, candidate in enumerate(candidates):
        utility = util(candidate, A, B, C)
        if utility > u_max:
            u_max = utility
            cons_max = candidate
    return u_max, cons_max

cons = np.linspace(0,4,51)
A = 1
B = 2
C = 10

u_max, cons_max = find_max_cons(cons, A, B, C)

print(u_max, cons_max)

def find_max_cons_np(candidates, A, B, C):
    utility = -A * (candidates - B)**2 + C
    u = np.argmax(utility)
    return candidates[u]

print(find_max_cons_np(cons, A, B, C))
