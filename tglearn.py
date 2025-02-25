import numpy as np

class KNeighborsRegressor:
    def __init__(self, n_neighbors = 5):
        self.n = n_neighbors


    def fit(self,X,y):
        """
        learning function
        :param X:
        :param y:
        :return:
        """
        self.X_train = X
        self.y_train = y


    def predict(self, X):
        distance = abs(self.X_train - X)
        idx_arr = np.argsort(distance, axis = 0)
        sum_val = np.sum(self.y_train[idx_arr[:self.n]])
        return sum_val / self.n

        # sum_val = 0
        # for i in range(self.n):
        #     sum_val += self.y_train[idx_arr[i][0]][0]
        # return sum_val / self.n


class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None


    def fit(self, X, y):
        """
        learning function
        :param X: independant variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: void
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        denominator = np.sum(pow(X-X_mean, 2))
        numerator = np.sum((X-X_mean) * (y-y_mean))

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)


    def predict(self, X) -> list:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array fromat)
        """
        return self.slope * np.array(X) + self.intercept