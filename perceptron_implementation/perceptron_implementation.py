from math import e
import random
import matplotlib.pyplot as plt

def dot_product(vec1, vec2):
    dot_result = 0

    for i in range(len(vec1)):
       dot_result += vec1[i]*vec2[i]

    return dot_result


class perceptron:
    def __init__(self, learning_rate=1e-4, actv_func='relu'):
        self.__inputs = None
        self.__output = None
        self.__weights = None
        self.__bias = random.random()
        self.__learning_rate = learning_rate
        self.__actv_func = actv_func

    def set_input(self, inputs):
        self.__inputs = inputs
        self.__weights = [random.random() for _ in range(len(self.__inputs[0]))]

    def set_output(self, outputs):
        self.__outputs = outputs

    def get_weights(self):
        return self.__weights

    def get_bias(self):
        return self.__bias

    def partial_result(self, x):
        return dot_product(self.__weights, x) + self.__bias

    def internal_predict(self):
        #predict de todo o conjunto de entrada
        result = []
        for i in self.__inputs:
            result.append(dot_product(self.__weights, i) + self.__bias)

        return result

    def predict(self, x):
        #predict específica de um vetor
        return dot_product(self.__weights, x) + self.__bias

    def get_sum(self):
        sum_result = 0
        for i in self.__inputs:
            sum_result += dot_product(self.__weights, i) + self.__bias

        return sum_result

        if self.__actv_func == 'relu':
            return self.relu(sum_result)
        elif self.__actv_func == 'sigmoide':
            return self.sigmoide(sum_result)

    def mean_error(self):
        error = 0
        for i in range(len(self.__inputs)):
            error += (self.__outputs[i] - self.predict(self.__inputs[i])) * (self.__outputs[i] - self.predict(self.__inputs[i]))

        return error**(0.5)/len(self.__inputs)

    def fit(self):
        error = self.mean_error()
        for i in range(len(self.__weights)):
            error = self.mean_error()
            if self.__actv_func == 'sigmoide':
                self.__weights[i] += error * self.sigmoide(error) * self.__learning_rate
            elif self.__actv_func == 'relu':
                self.__weights[i] += error * self.derivative_relu(error) * self.__learning_rate

        self.__bias += error * self.__learning_rate

    def relu(self, x):
        if x > 0:
            return x
        return 0

    def derivative_relu(self, x):
        if x > 0:
            return 1
        return 0

    def sigmoide(self, x):
        return 1/(1 + e**(-x))

    def derivative_sigmoide(self, x):
        sig = self.sigmoide(x)
        return self.sigmoide(x) * (1 - self.sigmoide(x))

if __name__ == '__main__':
    # Example f(x) = 3*x + 2:

    x = []
    for i in range(-20, 20):
        x.append([i])

    y = []
    for i in range(len(x)):
        y.append(x[i][0]*3 + 2)

    print(x)
    print(y)

    p = perceptron()
    p.set_input(x)
    p.set_output(y)

    for i in range(25000):
        p.fit()

    res = p.internal_predict()

    for i in range(len(y)):
        print(y[i], res[i])

    plt.plot(x, y)
    plt.plot(x, res)
    plt.show()