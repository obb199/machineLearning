import matplotlib.pyplot as plt
import numpy as np

points_1 = np.array([(1, 1), (3, 2), (5, 3), (7, 3), (7, 4.25), (4.86, 3.87),
                     (8.46, 4.81), (8.2, 5.83), (10.84, 5.97), (10.46, 7.85),
                     (12.66, 8.35), (10.02, 6.35), (12.04, 8.41), (11.32, 8.25),
                     (9.36, 5.91), (6.42, 4.71), (4.72, 1.95), (2.76, 0.73),
                     (4.3, 2.87), (5.78, 2.55), (1.96, 1.77), (4, 1), (6.02, 3.33),
                     (5.76, 3.99), (7.98, 4.27), (9.02, 6.73), (11.62, 6.79),
                     (9.82, 7.27), (3.66, 1.77), (7.96, 3.35), (12, 9), (12.16, 7.61),
                     (9.08, 4.55), (10, 5), (10.54, 6.93), (7.2, 5.37), (7.2, 5.37),
                     (3.5, 2.65), (1.66, 0.51), (1, 0), (2.58, 1.41), (9.96, 5.61)],
                    dtype=np.float32)

points_2 = np.array([(1.6, 1.03), (3.82, 6.83), (8.62, 9.67), (14.64, 8.87), (18.18, 6.65),
                     (21.02, 3.67), (22.28, 0.53), (6.78, 8.07), (8, 9), (5.72, 9.27), (4.98, 7.77),
                     (2.72, 4.43), (2.18, 2.31), (3.04, 1.43), (1.34, 0.11), (3.76, 3.29), (3.5, 4.81),
                     (3.02, 5.45), (9.52, 8.83), (10.8, 9.99), (10.14, 10.93), (12.68, 11.21), (13.96, 10.59),
                     (13.9, 9.67), (12.5, 9.73), (11.68, 10.53), (14.16, 8.25), (16.5, 8.49), (15.56, 9.43),
                     (16.4, 7.29), (15.56, 7.89), (18.12, 7.81), (17.64, 6.35), (19.18, 5.31), (20.22, 6.17),
                     (20.62, 4.99), (20.2, 4.15), (20.78, 2.69), (21.36, 1.99), (22.26, 2.27), (22.66, 1.11),
                     (23.14, 0), (21.7, 0.75), (22.16, 1.63), (10.5, 9.17), (12.42, 8.89), (11.36, 9.41),
                     (9.1, 10.49), (9.72, 10.03), (7.44, 10.33), (6.68, 9.55), (6.02, 8.65), (7.92, 9.49),
                     (6.14, 8.17), (5.34, 6.73), (4.76, 6.11), (4.16, 4.99), (2.78, 3.77), (3.7, 2.53),
                     (2.4, 1.73), (2.52, 0.83), (2.04, 0.41), (4.42, 4.25), (3.06, 3.35), (2.34, 3.05),
                     (8.44, 10.97), (13.24, 9.13), (12.92, 10.53), (17.38, 7.75), (19.26, 6.59), (4.28, 6.07),
                     (22.34, 3.83), (11.14, 11.45), (22, 3), (21.46, 4.59), (6.12, 7.33), (15, 10)],
                    dtype=np.float32)

points_3 = np.array([(2, 3), (3, 3), (3, 4), (2.38, 4.39), (3, 4.61), (22.18, 8.25),
                     (4, 4.71), (4, 4), (4.62, 4.57), (5.46, 5.11), (19.9, 7.79),
                     (5.02, 5.51), (6.16, 4.35), (5.78, 5.73), (6.82, 5.91),
                     (7.14, 5.15), (8.02, 6.19), (7.62, 6.67), (8.8, 5.45),
                     (8.08, 5.37), (10, 6), (10.74, 5.21), (11.56, 4.61),
                     (12.24, 3.93), (11, 4), (11.6, 5.19), (11.18, 5.99), (2, 1),
                     (12.58, 5.97), (13.22, 5.43), (13.16, 4.99), (12.8, 4.59),
                     (14.4, 3.71), (14.4, 4.49), (13.44, 3.75), (15, 3), (14.94, 2.53),
                     (14.58, 2.51), (15.76, 2.69), (16.1, 3.37), (16.84, 3.25),
                     (16.76, 2.69), (16.78, 2.21), (17.68, 2.45), (17.28, 1.85),
                     (17.58, 1.73), (9.38, 6.97), (10.24, 7.19), (10.68, 6.83),
                     (10, 6.73), (8.76, 7.51), (8.62, 7.19), (8.96, 6.51), (8.58, 6.69),
                     (7.52, 7.51), (3.72, 3.01), (2.88, 2.53), (1.92, 2.49), (1.42, 2.71),
                     (1.74, 1.89), (2.14, 1.75), (0.86, 1.17), (1.48, 1.03), (20.34, 6.59),
                     (17.26, 4.13), (17.6, 3.61), (18.18, 3.41), (18.18, 4.15), (17.86, 4.55),
                     (17.44, 5.21), (18.26, 5.21), (18.56, 4.91), (18.26, 5.87), (18.88, 6.15),
                     (18.88, 5.73), (19.48, 6.51), (18.98, 6.87), (19.4, 6.19), (20, 6),
                     (20.36, 7.13), (20.38, 7.73), (17.82, 6.97), (18.82, 7.45), (19.26, 8.13),
                     (20.46, 8.65), (21.14, 8.03), (21.2, 7.41), (21.54, 6.87), (21.8, 7.43)],
                    dtype=np.float32)


def delta_calculus(first_line, second_line, third_line, fourth_line):
    """Using Laplace theorem definition here"""

    det_value = 0
    det_value += first_line[0] * (
                second_line[1] * third_line[2] * fourth_line[3] + second_line[2] * third_line[3] * fourth_line[1] +
                second_line[3] * third_line[1] * fourth_line[2] - second_line[2] * third_line[1] * fourth_line[3] -
                second_line[1] * third_line[3] * fourth_line[2] - second_line[3] * third_line[2] * fourth_line[1])
    det_value -= second_line[0] * (
                first_line[1] * third_line[2] * fourth_line[3] + first_line[2] * third_line[3] * fourth_line[1] +
                first_line[3] * third_line[1] * fourth_line[2] - first_line[2] * third_line[1] * fourth_line[3] -
                first_line[1] * third_line[3] * fourth_line[2] - first_line[3] * third_line[2] * fourth_line[1])
    det_value += third_line[0] * (
                first_line[1] * second_line[2] * fourth_line[3] + first_line[2] * second_line[3] * fourth_line[1] +
                first_line[3] * second_line[1] * fourth_line[2] - first_line[2] * second_line[1] * fourth_line[3] -
                first_line[1] * second_line[3] * fourth_line[2] - first_line[3] * second_line[2] * fourth_line[1])
    det_value -= fourth_line[0] * (
                first_line[1] * second_line[2] * third_line[3] + first_line[2] * second_line[3] * third_line[1] +
                first_line[3] * second_line[1] * third_line[2] - first_line[2] * second_line[1] * third_line[3] -
                first_line[1] * second_line[3] * third_line[2] - first_line[3] * second_line[2] * third_line[1])

    return det_value


def function_construct(list_of_points):
    #  Values to use in delta construction

    l = 0  # length of ponits
    x1 = 0  # sum of x
    x2 = 0  # sum of x**2
    x3 = 0  # sum of x**3
    x4 = 0  # sum of x**4
    x5 = 0  # sum of x**5
    x6 = 0  # sum of x**6
    y = 0  # sum of y
    yx = 0  # sum of x*y
    yx2 = 0  # sum of x²*y
    yx3 = 0  # sum of x³*y

    max_x = 0
    min_x = 0
    for point in list_of_points:
        #  definition of limits to the fuction in graphic
        if point[0] > max_x:
            max_x = int(point[0])
        if point[0] < min_x:
            min_x = int(point[0])

        #  Sums:
        l += 1
        x1 += point[0]
        x2 += point[0] ** 2
        x3 += point[0] ** 3
        x4 += point[0] ** 4
        x5 += point[0] ** 5
        x6 += point[0] ** 6
        y += point[1]
        yx += point[0] * point[1]
        yx2 += point[0] * point[0] * point[1]
        yx3 += point[0] * point[0] * point[0] * point[1]

    stand_first_line = (x6, x5, x4, x3)
    stand_second_line = (x5, x4, x3, x2)
    stand_third_line = (x4, x3, x2, x1)
    stand_fourth_line = (x3, x2, x1, l)
    constant_values = (yx3, yx2, yx, y)

    det = delta_calculus(stand_first_line, stand_second_line, stand_third_line, stand_fourth_line)

    det_a = delta_calculus(constant_values, stand_second_line, stand_third_line, stand_fourth_line)

    det_b = delta_calculus(stand_first_line, constant_values, stand_third_line, stand_fourth_line)

    det_c = delta_calculus(stand_first_line, stand_second_line, constant_values, stand_fourth_line)

    det_d = delta_calculus(stand_first_line, stand_second_line, stand_third_line, constant_values)

    a = det_a / det

    b = det_b / det

    c = det_c / det

    d = det_d / det

    function_x = []
    function_y = []

    for x in range(min_x, max_x + 5):
        for _ in range(9):
            function_y.append(a * x ** 3 + b * x ** 2 + c * x + d)
            function_x.append(x)
            x += 0.1

    points_x = []
    points_y = []
    for point in list_of_points:
        points_x.append(point[0])
        points_y.append(point[1])

    fig = plt.figure()
    axis = fig.add_subplot()
    axis.plot(function_x, function_y)
    axis.scatter(points_x, points_y)

    print(f'f(x) = {a}.x³ + {b}.x² + {c}.x + {d}')

    return plt.show()


if __name__ == '__main__':
    function_construct(points_2)
