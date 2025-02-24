from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
print(ls)
# print(type(ls))
x = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
#print(y)

# ls.plot(kind = 'scatter', grid =True, x= 'GDP per capita (USD)', y= 'Life satisfaction')
# plt.axis([23_500,62_500,4,9])
# plt.show()

# model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)
model.fit(x,y)
x_new = [[37_655.2]]
print(model.predict(x_new))
# LinearRegression 6.30
# KNeighbootRegressor 6.33