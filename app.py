import streamlit as st
import time
import pandas as np
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.datasets import fetch_california_housing
st.title('House Price prediction using ML')
st.image('https://therealdeal.com/wp-content/uploads/2021/03/CoreLogic-Home-Price-Reports-Highest-Growth-Since-2013.gif')

