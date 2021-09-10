import matplotlib.pyplot as plt

points = [(1, 1), (3, 2), (5, 3), (7, 3), (7, 4.25), (4.86, 3.87),
          (8.46, 4.81), (8.2, 5.83), (10.84, 5.97), (10.46, 7.85),
          (12.66, 8.35), (10.02, 6.35), (12.04, 8.41), (11.32, 8.25),
          (9.36, 5.91), (6.42, 4.71), (4.72, 1.95), (2.76, 0.73),
          (4.3, 2.87), (5.78, 2.55), (1.96, 1.77), (4, 1), (6.02, 3.33),
          (5.76, 3.99), (7.98, 4.27), (9.02, 6.73), (11.62, 6.79),
          (9.82, 7.27), (3.66, 1.77), (7.96, 3.35), (12, 9), (12.16, 7.61),
          (9.08, 4.55), (10, 5), (10.54, 6.93), (7.2, 5.37), (7.2, 5.37),
          (3.5, 2.65), (1.66, 0.51), (1, 0), (2.58, 1.41), (9.96, 5.61)]

x = [i[0] for i in points]
y = [i[1] for i in points]


def error_tax(a, b, points):
    error = 0

    for point in points:
        error += (point[1] - a*point[0] - b)**2

    return error*0.5


def gradient_descent(a_now, b_now, points, L):
    a_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in points:

        a_gradient += -(2/n) * i[0] * (i[1] - i[0] * a_now - b_now)
        b_gradient += -(2/n) * (i[1] - i[0] * a_now - b_now)

    a = a_now - a_gradient * L
    b = b_now - b_gradient * L

    return a, b


m = 0
n = 0
L = 0.01
epochs = 1000

for i in range(epochs):
    m, n = gradient_descent(m, n, points, L)

print(m, n)
print(error_tax(m, n, points))

plt.scatter(x, y, c='blue')
plt.plot([0, 15], [n, m*15 + n], c='red')
plt.show()
