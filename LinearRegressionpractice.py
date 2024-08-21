from palmerpenguins import load_penguins
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

df = load_penguins()

    # 입력값: 펭귄 종, 부리 길이
    # 결과값: 부리 깊이
    # 선형회귀 모델 적합하기 문제

model=LinearRegression()

model.fit(x, y)

model.coef_
model.intercept_