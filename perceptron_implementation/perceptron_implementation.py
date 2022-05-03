from math import e
from random import randint, random
import matplotlib.pyplot as plt

def x_y_sigmoid_test():
    x = [[2.7810836, 2.550537003, 0],
         [1.465489372, 2.362125076, 0],
         [3.396561688, 4.400293529, 0],
         [1.38807019, 1.850220317, 0],
         [3.06407232, 3.005305973, 0],
         [7.627531214, 2.759262235, 1],
         [5.332441248, 2.088626775, 1],
         [6.922596716, 1.77106367, 1],
         [8.675418651, -0.242068655, 1],
         [7.673756466, 3.508563011, 1]]

    y = [[0], [0], [0], [0], [0], [1], [1], [1], [1], [1]]

    return x, y

def dot_product(vec1, vec2):
    dot_result = 0
    for i in range(len(vec1)):
        dot_result += vec1[i]*vec2[i]

    return dot_result

def relu(x):
    if x > 0:
        return x
    return 0

def d_relu(x):
    if x > 0:
        return 1
    return 0

def sigmoid(x):
    return 1/(1 + e**(-x))

def d_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


class perceptron:
    def __init__(self, x, y, activation_function='relu', learning_rate=0.0001):
        self.__input = x
        self.__output = y
        self.__activation_function = activation_function

        self.__weights = [random()*00.1 for _ in range(len(x[0]))]
        self.__bias = random()*00.1
        self.__learning_rate = learning_rate

    def get_weights(self):
        return self.__weights

    def get_bias(self):
        return self.__bias

    def feedforward(self):
        res = []

        if self.__activation_function == 'relu':
            for i in range(len(self.__input)):
                res.append(relu(dot_product(self.__input[i], self.__weights)) + self.__bias)
        elif self.__activation_function == 'sigmoid':
            for i in range(len(self.__input)):
                res.append(sigmoid(dot_product(self.__input[i], self.__weights)) + self.__bias)

        return res

    def error(self):
        error = 0
        res = self.feedforward()

        for i in range(len(self.__input)):
            error += res[i] - self.__output[i][0]

        return error

    def backpropagation(self):
        if self.__activation_function == 'relu':
            sum_actv = sum([d_relu(i) for i in self.feedforward()])
        elif self.__activation_function == 'sigmoid':
            sum_actv = sum([d_sigmoid(i) for i in self.feedforward()])

        error = self.error()
        for i in range(len(self.__weights)):
            self.__weights[i] -= self.__learning_rate*error*self.__weights[i]*sum_actv
        self.__bias -= self.__learning_rate*error*sum_actv
