from sklearn.linear_model import LogisticRegression
"""
If reslt is 0 - false
If result is 1 - true
"""
X=[[1], [2], [3], [4], [5], [6]] #studie hour input
y=[0, 0, 0, 1, 1, 1] # result 0-fail, 1-pass
 
model = LogisticRegression()
model.fit(X,y)
hour = 3
result = model.predict([[hour]])
if result == 1:
    print(f"Based on hour {hour}, result is pass")
else:
    print(f"Based on hour {hour}, result is fail")

