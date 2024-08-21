from matplotlib import pyplot as plt
import seaborn as sns
from palmerpenguins import load_penguins                           
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go
penguins= load_penguins()
import pandas as pd

df

plt.rcParams.update({'font.family': 'Malgun Gothic'})
sns.scatterplot(data=df,
                x='bill_length_mm',
                y="bill_depth_mm",
                hue="species")
plt.xlabel("부리길이")
plt.ylabel("부리깊이")


입력값: 펭귄종, 부리 길이 
결과값: 부리깊이
선형회귀 모델 적합

model = LinearRegression()
penguins = penguins.dropna()

x=penguins[["bill_length_mm"]]
y=penguins["bill_depth_mm"]

model.fit(x, y)
linear_fit=model.predict(x)
model.coef_
model.intercept_

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        mode="lines",
        x=penguins["bill_length_mm"], y=linear_fit,
        name="선형회귀직선",
        line=dict(dash="dot", color="blue")
    )
)

penguins_dummies = pd.get_dummies(penguins, 
                                  columns=['species'],
                                  drop_first=False)
penguins_dummies.columns

# x와 y 설정 범주형(문자열) 변수를 숫자형으로 바꾸니 modelfit  가능
x = penguins_dummies[["bill_length_mm", "species_Chinstrap", "species_Gentoo"]]
y = penguins_dummies["bill_depth_mm"]

model.coef_
model.intercept_
# 모델 학습
model = LinearRegression()
model.fit(x, y)