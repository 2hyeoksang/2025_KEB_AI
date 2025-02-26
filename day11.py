# Assignment
# v0.7)v0.6의 최근접이웃모델과 같이 동작하는 커스텀 클래스를 설계하시오.

#from sklearn.linear_model import LinearRegression
from tglearn import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.neighbors import KNeighborsRegressor
from tglearn import KNeighborsRegressor

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
x = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
#print(np.sort(y, axis = 0))

ls.plot(kind = 'scatter', grid =True, x= 'GDP per capita (USD)', y= 'Life satisfaction')
plt.axis([23_500,62_500,4,9])
#plt.show()

# model = LinearRegression()
model = KNeighborsRegressor()
model.fit(x,y)

x_new = [[31721.3]]
print(model.predict(x_new))
# LinearRegression 5.90
# KNeighbootRegressor 5.70