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

#add the indices in an array ex. [1,2,3]
def parseFlatWith(array):
    filepath = '../data/'
    x_train = pd.read_csv(filepath + 'train/x_train.csv')
    y_train = pd.read_csv(filepath + 'train/y_train.csv')
    #useless , but added
    x_test = pd.read_csv(filepath + 'test/x_test.csv')
    
    columnArray = ['GeneId', 'H3K4me3','H3K4me1','H3K36me3', 'H3K9me3','H3K27me3']
    
    for i in array:
        columnArray.remove(columnArray[i])
        
    x_train = x_train.drop(columnArray,axis=1)
    x_test = x_test.drop(columnArray,axis=1)
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
        
def getMeanOfSignals():
    filepath = '../data/'
    x_train = pd.read_csv(filepath + 'train/x_train.csv')
    y_train = pd.read_csv(filepath + 'train/y_train.csv')
    #useless , but added
    x_test = pd.read_csv(filepath + 'test/x_test.csv')
    
    no_train_genes = x_train.shape[0] / 100
    no_test_genes  = x_test.shape[0] / 100
    
    x_train = x_train.drop("GeneId",axis=1)
    x_test = x_test.drop("GeneId",axis=1)
    y_train = y_train.drop("GeneId",axis=1)
    
    x_train = np.split(x_train, no_train_genes)
    x_test = np.split(x_test, no_test_genes)
    
    x_train_mean_list = []
    x_test_mean_list = []

    for gene_id in range(len(x_train)):
        x_train_mean_list.append(np.mean(np.array(x_train[gene_id]), axis=0))
        
    for gene_id in range(len(x_test)):
        x_test_mean_list.append(np.mean(np.array(x_test[gene_id]), axis=0))
    
    y_train = np.array(y_train.values.ravel())
    
    return np.array(x_train_mean_list), y_train, np.array(x_test_mean_list)
    
        
#     print(x_train_mean_list)
#     print("--------")
#     print(x_train_mean_list[0])
    