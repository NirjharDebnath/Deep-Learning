import numpy as np 
import tensorflow as tf 

from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential

def model_relu():
    model = Sequential([
        Input((1,)),
        Dense(16, activation="relu"),
        Dense(16, activation="relu"),
        Dense(8, activation="relu"),
        Dense(4, activation="linear"),
        Dense(1, activation="linear")
    ])
    
    model_summary = model.summary()
    return model, model_summary

def model_exp():
    model = Sequential([
        Input((1,)),
        Dense(16, activation="exp"),
        Dense(16, activation="relu"),
        Dense(8, activation="exp"),
        Dense(4, activation="linear"),
        Dense(1, activation="linear")
    ])
    
    model_summary = model.summary()
    return model, model_summary

def model_wavy():
    model = Sequential([
        Input((1,)),
        Dense(16, activation="tanh"),
        Dense(16, activation="sigmoid"),
        Dense(8, activation="relu"),
        Dense(4, activation="leaky_relu"),
        Dense(1, activation="linear")
    ])
    
    model_summary = model.summary()
    return model, model_summary

model_relu_exp, model_summary = model_wavy()

print(model_relu_exp)