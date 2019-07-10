# Ridge regression / Lasso regression 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import *
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.datasets import load_boston

# sample data gotten from sklearn.dataset
dataset = load_boston()


# sample data
data_x = pd.DataFrame(dataset.data,columns=dataset.feature_names)

#target data
data_y = pd.DataFrame(dataset.target,columns=['target'])


#compact the data set 
size = len(data_x) - 10
for i in range(size):
    data_x = data_x.drop(i)
    data_y = data_y.drop(i)

data_y = data_y.as_matrix().ravel()


lr = LinearRegression()
lasso = Lasso()
ridge = Ridge()


#create regression linear / lasso / ridge
lr.fit(data_x, data_y)
lasso.fit(data_x, data_y)
ridge.fit(data_x, data_y)


plt.plot(lr.predict(data_x), linestyle="solid", 
         color="black",label="lr")
plt.plot(lasso.predict(data_x), linestyle="solid", 
         color="red", label="lasso")
plt.plot(ridge.predict(data_x), linestyle="solid", 
         color="blue", label='ridge')
plt.title("Linear, Lasso, Ridge")
plt.legend(loc="lower right")
plt.show()


print('coefficients of lasso and aridge')

reg_coef=[]
reg_coef.append([lasso.coef_])
reg_coef.append([ridge.coef_])
print(reg_coef)

