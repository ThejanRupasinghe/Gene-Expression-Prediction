import pandas as pd
import numpy as np

# flat everything to x_train - 15485 x 500 , y_train - 15485 , x_test - 3871 x 500
def parseFlat():
    filepath = '../data/'
    x_train = pd.read_csv(filepath + 'train/x_train.csv')
    y_train = pd.read_csv(filepath + 'train/y_train.csv')
    x_test = pd.read_csv(filepath + 'test/x_test.csv')

    x_train = x_train.drop("GeneId",axis=1)
    x_test = x_test.drop("GeneId",axis=1)
    y_train = y_train.drop("GeneId",axis=1)
    
    no_train_genes = x_train.shape[0] / 100
    no_test_genes  = x_test.shape[0] / 100
    
    x_train = np.split(x_train, no_train_genes)
    x_test = np.split(x_test, no_test_genes)
    
    x_train = [gene.values.ravel() for gene in x_train]
    x_test = [gene.values.ravel() for gene in x_test]
    
    x_train = np.array(x_train)
    y_train = np.array(y_train.values.ravel())
    x_test  = np.array(x_test)
    
    return x_train, y_train, x_test