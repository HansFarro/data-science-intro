import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("PYTHON\countries.csv")
us=data[data.country=="United States"]
china=data[data.country=="China"]
# print(data)
plt.plot(us.year,us.population/ 10**6)
plt.plot(china.year,china.population/10**6)
plt.xlabel("year")
plt.ylabel("population")
plt.legend(["U.S.","China"])
plt.show()