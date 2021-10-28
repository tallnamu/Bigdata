import matplotlib.pyplot as plt
import random

fre=[]
prob=[]
num=[]
n=0
total_try=3000
i=0
switch='False'
for j in range(1,total_try+1):
    i = random.randint(1,6)
    if (i ==3):
        switch='True'
        n+=1
        num.append(i)   
    fre.append((n/j))
    prob.append(1/6)
print(num)
plt.plot(range(1,total_try+1),fre,'b',range(1,total_try+1),prob,'r')
plt.legend(['Relative Frequency','Probablity'])
plt.show()



