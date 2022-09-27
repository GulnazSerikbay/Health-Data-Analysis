from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title("Your step predictor")
root.geometry("400x200")

def plot_stepcounts():
    stepcount = pd.read_csv("GUI/steps_by_dates.csv")
    plt.plot(stepcount["Date"].tail(10), stepcount["StepCount"].tail(10))
    plt.title("Your steps")
    plt.show()

def plot_distance():
    dist = pd.read_csv("GUI/dist_by_dates.csv")
    plt.plot(dist["Date"].tail(10), dist["Distance"].tail(10))
    plt.title("Your distance over 10 days")
    plt.show()
    
def plot_stepcounts():
    stepcount = pd.read_csv("GUI/prepared_by_day.csv")
    plt.plot(stepcount["Date"].tail(10), stepcount["StepCount"].tail(10))
    plt.title("Your steps over 10 days")
    plt.show()
    
def train_all():
    data = pd.read_csv("GUI/prepared_data.csv")
    data.index = data['@_startDate']
    data.pop('@_startDate')
    print(data.iloc[:,0])
    import keras
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Activation, Flatten
    from keras.utils import np_utils
    import time
    from time import process_time
    #Get the model
    MLP_model = Sequential()
    MLP_model.add(Dense(8, input_dim = 15, use_bias = True, activation = 'relu'))
    MLP_model.add(Dense(20, use_bias = True, activation = 'relu'))
    MLP_model.add(Dense(1, use_bias = True, activation = 'sigmoid'))
    
    #dataset split
    n_data_train = int(0.8 * data.iloc[:,1:].shape[0])
    n_data_test = int(0.2 * data['StepCount'].shape[0])

    X_train = data.iloc[:n_data_train, 1:]
    Y_train = data['StepCount'][:n_data_train]
    X_test = data.iloc[n_data_train:, 1:]
    Y_test = data['StepCount'][n_data_train:]
    
    X_train = np.asarray(X_train).astype(np.float32)
    MLP_model.compile(loss = 'mean_absolute_error', optimizer = 'adam', metrics = ['mean_squared_error'])
    training = MLP_model.fit(X_train, Y_train, epochs = 50, batch_size = 1, validation_data = (np.asarray(X_test).astype(np.float32), Y_test), verbose = 2)
    return training

def predict_all():
    estimator = train()
    Y = estimator.predict()
    return Y


step_button = Button(root, text = "Show the last 10 records", command = plot_stepcounts)
step_button.pack()

dist_button = Button(root, text = "Show my distance records", command = plot_distance)
dist_button.pack()

button = Button(root, text = "Show prediction for the next hour", command = train_all)
button.pack()

root.mainloop()
