import matplotlib.pyplot as plt
import random
from math import factorial as fact

def pmf(list_):
    x_range = range(1, 11)
    n_x = [0]*len(x_range)
    for i in x_range:
        for j in list_:
            if i == j:
                n_x[i-1]+=1/len(list_)
    return n_x

u_suc = []

total_try = 5000
for _ in range(total_try):
    i = random.randint(0,2) 
    n = 1
    while i != 1 :
        n+=1
        i = random.randint(0,1)
    u_suc.append(n)

pmf_s = pmf(u_suc)


pmf_a = []
for k in range(1, 6):
    prob = (fact(5)/(fact(k)*fact(5-k)))*(2/5)**(k)*(3/5)**(5-k)
    pmf_a.append(prob)

print(pmf_a)
plt.plot(range(1, 6), pmf_a, 'r.')
plt.legend(['sim', 'analy'])
plt.show()
