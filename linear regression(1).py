#!/usr/bin/env python
# coding: utf-8

# # Simple Linear Regression

# ## Importing the libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ## Importing the dataset

# In[2]:


dataset = pd.read_csv('C:/Users/User/Desktop/Part 2 - Regression/Section 4 - Simple Linear Regression/Python/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

xn = np.reshape(X,len(X))


# # Finding the mean of the data

# In[3]:


import statistics
x_bar = statistics.mean(xn)
print(x_bar)
y_bar = statistics.mean(y)
print(y_bar)


# ## Finding the Standard deviation and slope from the dependent and inpendent variable

# In[4]:



for i in range (0, 30):
    n1 =+ ((X[i]-x_bar)*(y[i]-y_bar));
    d1 =+ ((X[i]-x_bar)*(X[i]-x_bar));
    d2 =+ ((y[i]-y_bar)*(y[i]-y_bar));
    r = n1/np.sqrt(d1*d2);

sx = statistics.stdev(xn)
print(sx)
sy = statistics.stdev(y)
print(sy)
b= r*(sy/sx)
print (b)


# ## Finding the y intercept

# In[5]:


c = y_bar - b*x_bar
print(c)
    


# ## Creating the model

# In[6]:


yp=[]
for j in range (0,30):

    yp=np.append(yp,b*xn[j]+c)
        
    
    


# ## Model accuracy using R square method

# In[7]:


from sklearn.metrics import r2_score
r2_score(y, yp)


# ## Actual vs model output

# In[8]:


plt.scatter(X, y, color = 'red')
plt.plot(X, yp, color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[ ]:




