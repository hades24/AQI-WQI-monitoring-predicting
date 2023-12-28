#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np
data = pd.read_csv('bengaluru.csv')
X = data.drop(['AQI', 'City', 'Date', 'AQI_Bucket','Xylene'], axis=1)  # Features
y = data['AQI']  # Target variable
imputer_X = SimpleImputer(strategy='mean')
X = imputer_X.fit_transform(X)
imputer_y = SimpleImputer(strategy='mean')
y = imputer_y.fit_transform(y.values.reshape(-1, 1))
if X.shape[0] != y.shape[0]:
    raise ValueError("Number of samples in X and y are inconsistent.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

print(f'Root Mean Squared Error: {rmse}')

