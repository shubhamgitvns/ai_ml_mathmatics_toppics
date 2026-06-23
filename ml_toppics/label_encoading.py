
"""
Label encoding convert the categorial (text) data to numerical data
"""

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

gender=['male', 'female']

encder= le.fit_transform(gender)
print(gender,"After label encoder",encder)