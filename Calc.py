import math
import decimal
import pandas as pd 
from matplotlib import pyplot as plt 



x = []
y = []

name = input("Enter the name of the graph: ")
yaxis_name = input("Enter the label for the Y-Axis: ")
xaxis_name = input("Enter the label for the X-Axis: ")
n = int(input("How many trials will be ran: "))
p = float(input("What is the probability of a successful event occuring?: "))
q = float(1 - p)



for w in range(0, n+1):
    a = math.factorial(n)/(math.factorial(n-w)*math.factorial(w))
    b = decimal.Decimal(p)**decimal.Decimal(w)
    c = decimal.Decimal(q)**decimal.Decimal(n-w)
    d = (decimal.Decimal(a)*decimal.Decimal(b)*decimal.Decimal(c))*100

    x.append(w)
    y.append(d)
    w = w + 1

plt.axis([0, n, 0, max(y) + (max(y)*decimal.Decimal(0.25))])
plt.title(str(name))
plt.xlabel(str(xaxis_name))
plt.ylabel(str(yaxis_name))
plt.plot(x,y)
plt.show()
