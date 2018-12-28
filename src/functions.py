import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.model_selection import GridSearchCV

#split data set using train_test_split
def splitData(x_train, y_train):
    X_train, X_test, Y_train, Y_test = train_test_split(x_train, y_train, test_size=0.2)
    return X_train, X_test, Y_train, Y_test

#grid search CV
def grid_search_cross_val(model, X, Y, param_grid, scoring='f1'):
    grid = GridSearchCV(model, param_grid=param_grid, scoring=scoring)
    grid.fit(X, Y)
    print("Best score: {}".format(np.abs(grid.best_score_)))
    print("Best params: {}".format(grid.best_params_))