import numpy as np



class NeuralNetwork:

    def __init__(self, layer_sizes):
        # layer_sizes example: [4, 10, 2]
        self.neuron_number_1 = layer_sizes[0]
        self.neuron_number_2 = layer_sizes[1]
        self.neuron_number_3 = layer_sizes[2]
        self.w1 = np.random.normal(size=(self.neuron_number_2, self.neuron_number_1))
        self.w2 = np.random.normal(size=(self.neuron_number_3, self.neuron_number_2))
        self.b2 = np.zeros((self.neuron_number_2, 1))
        self.b3 = np.zeros((self.neuron_number_3, 1))


    def activation(self, x):
        x = x.astype(float)
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        # x example: np.array([[0.1], [0.2], [0.3]])
        a1 = x
        a2 = self.activation(self.w1 @ a1 + self.b2)
        a3 = self.activation(self.w2 @ a2 + self.b3)
        return a3
