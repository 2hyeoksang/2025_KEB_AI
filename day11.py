#from sklearn.linear_model import LinearRegression
from tglearn import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
x = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values

ls.plot(kind = 'scatter', grid =True, x= 'GDP per capita (USD)', y= 'Life satisfaction')
plt.axis([23_500,62_500,4,9])
#plt.show()

model = LinearRegression()
model.fit(x,y)

x_new = [[31721.3]]
print(model.predict(x_new))
# LinearRegression 5.90
# KNeighbootRegressor 5.70