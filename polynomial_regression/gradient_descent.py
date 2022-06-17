def grads(X, Y, a, b):
    grad_a = 0
    grad_b = 0

    for x, y in zip(X, Y):
        grad_a += x * (y - (x * a + b))
        grad_b += y - (x * a + b)

    grad_a *= -2/len(X)
    grad_b *= -2/len(X)

    return grad_a, grad_b


def fit(grads, lr, a, b):
    a -= grads[0] * lr
    b -= grads[1] * lr
    return a, b


if __name__ == '__main__':
    X = [i for i in range(150)]
    Y = [i * 3 + 1 for i in range(150)]

    a = 0.3
    b = 0.5
    lr = 0.00005
    
    for _ in range(100000):
        var_grads = grads(X, Y, a, b)
        a, b = fit(var_grads, lr, a, b)


    print(a, b)
