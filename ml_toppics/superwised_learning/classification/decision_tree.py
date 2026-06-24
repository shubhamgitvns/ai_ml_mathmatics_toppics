import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = {
    "Area": [500, 700, 1000, 1500, 2000, 2500],
    "Price": ['low', 'low', 'mid', 'high', 'high', 'v-high']
}

df = pd.DataFrame(data)

X=df[['Area']]
y=df['Price']

model = DecisionTreeClassifier()
model.fit(X,y)
traing_data = pd.DataFrame({
    'Area':[1200,1800, 1600,700,2600]
})
result = model.predict(traing_data)
print(traing_data)
print("Predicted result =", result)