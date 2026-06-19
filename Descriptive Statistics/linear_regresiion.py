# bassic code of linear regression to find linear regrassion and predict the given data.

def linear_prediction(x, y, X):
    n = len(x)
    mean_X = sum(x) / n # mean of x column
    mean_Y = sum(y) / n # mean of y column
    d_X = []
    d_Y = []
    sum_of_sqr_of_dev_X = 0
    sum_of_pd = 0
    for i in range(n):
        d_X.append(x[i] - mean_X) # deviation of x
        d_Y.append(y[i] - mean_Y) # deviation of y
        sum_of_pd += d_X[i] * d_Y[i]  # sum of product deviation
        sum_of_sqr_of_dev_X += d_X[i] * d_X[i] # sum of square of deviation of x
    # linear regression: Y = mX + b
    m = sum_of_pd / sum_of_sqr_of_dev_X
    b = mean_Y - (m * mean_X)
    prediction = m * X + b
    return prediction

""""
Predict the price of pizza according to pizza size (in inches)
"""
x = [8, 10, 12] # pizza size column
y = [10, 13, 16] # pizza price column
ans = linear_prediction(x, y, 20)
print("Prediction =", ans)


    
