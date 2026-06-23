import pandas as pd
data=({
    'color':['red', 'blue', 'green']
})

df = pd.DataFrame(data)
encoded = pd.get_dummies(df,dtype= int)
print(encoded)