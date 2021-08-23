import matplotlib.pyplot as plt
import numpy as np

# Values of variables of any group:
group_one_X = np.array([2, 3, 2, 1, 1.5, 2.8, 2.82, 3.46, 3.18, 2.24])
group_one_Y = np.array([3, 3, 2, 1, 1.49, 1.51, 2.41, 1.93, 1.05, 1.03])

group_two_X = np.array([3.86, 4.38, 4.16, 2.9, 3.14, 3.32, 4, 3.24, 4.48, 5.44])
group_two_Y = np.array([7.07, 6.69, 6.25, 6.81, 7.51, 6.11, 5, 5.35, 5.67, 6.61])

group_three_X = np.array([5, 6, 5.5, 6.24, 5.64, 7.9, 6.94, 7.32, 6.62, 6.8, 4.82])
group_three_Y = np.array([3, 4, 3.47, 2.79, 2.25, 3.33, 3.67, 2.53, 2.39, 4.25, 3.89])

# point = (6.2, 4)  # Green example
# point = (2.2, 3)  # Blue example
# point = (2.2, 7)  # Red example
point = (3.89, 3.5)  # other example

#  Calculating the distances
distances = []
for i in range(len(group_one_X)):
    d = (point[0] - group_one_X[i])**2 + (point[1] - group_one_Y[i])**2
    distances.append((d, 'one'))

    d = (point[0] - group_two_X[i]) ** 2 + (point[1] - group_two_Y)[i] ** 2
    distances.append((d, 'two'))

    d = (point[0] - group_three_X[i]) ** 2 + (point[1] - group_three_Y[i]) ** 2
    distances.append((d, 'three'))

distances.sort()

#  Finding group of nearest neighbors
k = 10  # Using the ten nearest neighbors
while True:
    one = 0
    two = 0
    three = 0
    for i in range(k):
        if distances[i][1] == 'one':
            one += 1
        elif distances[i][1] == 'two':
            two += 1
        elif distances[i][1] == 'three':
            three += 1

    if (one > two and one > three) or (two > one and two > three) or (three > one and three > two):
        if one > two >= three:
            print('This point is from green group!')
        elif two > one >= three:
            print('This point is from blue group!')
        elif three > one >= two:
            print('This point is from red group!')

        break
    else:  # In the case of equality of neighbors
        k += 1

# plotting the values
plt.scatter(group_one_X, group_one_Y, color='blue')
plt.scatter(group_two_X, group_two_Y, color='red')
plt.scatter(group_three_X, group_three_Y, color='green')
plt.scatter(point[0], point[1], color='orange')
plt.show()
