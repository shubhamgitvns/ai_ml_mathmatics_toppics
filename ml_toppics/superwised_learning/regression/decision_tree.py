import pandas as pd
from sklearn.tree import DecisionTreeRegressor
data = {
    "Area": [500, 700, 1000, 1500, 2000],
    "Price": [20000, 25000, 35000, 50000, 70000]
}

df = pd.DataFrame(data)
print(df)

X=df[['Area']]
y=df['Price']

model = DecisionTreeRegressor()
model.fit(X,y)
traing_data = pd.DataFrame({
    'Area':[1200,1800, 1600,700]
})
result = model.predict(traing_data)

print("Predicted result =", result)