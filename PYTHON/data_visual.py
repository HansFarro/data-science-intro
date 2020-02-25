import pandas as pd
from matplotlib import pyplot as plt
sample_data=pd.read_csv("PYTHON\sample_data.csv")
# print(sample_data)
# print(sample_data.column_c)
plt.plot(sample_data.column_a,sample_data.column_b,'o')
plt.plot(sample_data.column_a,sample_data.column_c)
plt.show()