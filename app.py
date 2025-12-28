import streamlit as st
import time
import pandas as np
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.datasets import fetch_california_housing
st.title('House Price prediction using ML')
st.image('https://therealdeal.com/wp-content/uploads/2021/03/CoreLogic-Home-Price-Reports-Highest-Growth-Since-2013.gif')
df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title(' Select House feature')
st.sidebar.image('https://therealdeal.com/wp-content/uploads/2021/03/CoreLogic-Home-Price-Reports-Highest-Growth-Since-2013.gif')
all_value = []
for i in X:
  ans = st.sidebar.slider(f'Select {i} value')
  all_value.append(ans)
st.write(all_value)



