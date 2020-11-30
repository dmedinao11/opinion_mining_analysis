import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def delOutliers(df, column:str, percentil: int):
    y=df[column]

    qy_above = y.quantile(1 - percentil)
    qy_below = y.quantile(0 + percentil)

    return df[(df[column] > qy_below) & (df[column] < qy_above)]


df = pd.read_csv("data.csv")
df = df.drop(df.columns[0], axis=1)
df = df.set_index("date")
df.rename(columns={"Positive": "pos_feq", "Negative": "neg_feq", "pos_percentage %": "pos_rel_feq", "neg_percentage %": "neg_rel_feq"}, inplace=True)

xName = "Deaths"
yName = "neg_rel_feq"
deleteOutliers = True

if deleteOutliers:
  df = delOutliers(df, yName, 0.1)


x = df[xName]
y = df[yName]


X=x[:,np.newaxis]

regr = LinearRegression()
regr = regr.fit(X, y)

m=regr.coef_[0]
b=regr.intercept_
y_p=m*X+b

print("Coeficiente de correlación", np.corrcoef(x, y))
print("Modelo: Y = {} * X + {}".format(m, b))


plt.scatter(x,y, color="blue")
plt.plot(x,y_p, color="red")

plt.xlabel('Recuperados')
plt.ylabel('F_q de tweets negativos (%)')
plt.title("Tweets negativos y personas recuperadas")

plt.show()