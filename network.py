import numpy as np
from collections import deque

class Network(object):
    def __init__(self, layers, lr, loss):
        self.layers = layers

    def forward(self, inputs):
        activation = inputs
        for layer in self.layers:
            activation = layer.forward(activation)
        return activation