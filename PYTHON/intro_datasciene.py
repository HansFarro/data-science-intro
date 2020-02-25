import pandas as pd
from matplotlib import pyplot as plt
x=[1,2,3]
y=[1,4,9]
z=[10,5,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("TEST PLOT")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["esto es y","esto es z"])
plt.show()