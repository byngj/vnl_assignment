import numpy as np
import csv
import matplotlib.pyplot as plt

class C100Dataset:
    """
    X is a feature vector
    Y is the predictor variable
    """
    tr_x = None  # X (data) of training set.
    tr_y = None  # Y (label) of training set.
    ts_x = None # X (data) of test set.
    ts_y = None # Y (label) of test set.

    def __init__(self, filename):
        ## read the csv for dataset (cifar100.csv, cifar100_lt.csv or cifar100_nl.csv), 
        # 
        # Format:
        #   image file path,classname
        
        ### TODO: Read the csv file and make the training and testing set
        ## YOUR CODE HERE
        self.tr_x = []
        self.tr_y = []
        self.ts_x = []
        self.ts_y = []
        class_name=[]
        csvfile = open(filename, 'r', newline='')
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if len(row) == 2:
                tr_x = plt.imread('dataset/' + row[0])
                tr_x = np.transpose(tr_x, (2, 0, 1))
                self.tr_x.append(tr_x)
                if row[1] not in class_name :
                    class_name.append(row[1])
                self.tr_y.append(class_name.index(row[1]))
            else :
                ts_x = plt.imread('dataset/' + row[0])
                self.ts_x.append(ts_x)
                    

        ### TODO: assign each dataset
        tr_x = None  ### TODO: YOUR CODE HERE
        tr_y = None  ### TODO: YOUR CODE HERE
        ts_x = None ### TODO: YOUR CODE HERE
        ts_y = None ### TODO: YOUR CODE HERE
        self.tr_x = np.array(self.tr_x)
        self.tr_y = np.array(self.tr_y)
        self.ts_x = np.array(self.ts_x)
        self.ts_y = np.array(self.ts_y)

    def getDataset(self):
        return [self.tr_x, self.tr_y, self.ts_x, self.ts_y]