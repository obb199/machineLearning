import numpy as np
import matplotlib.pyplot as plt

# Values of variables of any group:
group_one_x = np.array([5.78, 4.98, 6.78, 5.95, 5.56, 4.13, 6.76, 7, 8.37, 7.86])
group_one_y = np.array([1.44, 2.66, 0.98, 3.58, 2.07, 1.55, 1.9, 3, 2.64, 3.72])
group_one_z = np.array([2.33, 2.54, 2.23, 2.13, 2.45, 2.19, 2.15, 2.46, 2.25, 2.21])

group_two_x = np.array([3.29, 2.38, 1.57, 1.3, 1.44, 1.55, 0.73, 2.26, 2.69, 2.26])
group_two_y = np.array([9.38, 7.6, 6.74, 8.84, 9.81, 7.89, 9.84, 8.62, 9.88, 6.76])
group_two_z = np.array([1.15, 1.34, 1.78, 1.66, 1.23, 1.28, 1.65, 1.76, 1.71, 1.23])

group_three_x = np.array([10.1, 7.51, 8.16, 6.99, 7.62, 8.55, 9.27, 9.07, 8.24, 7.56])
group_three_y = np.array([8.3, 10.07, 7.43, 7.6, 8.79, 9.84, 9.42, 8.42, 8.52, 7.37])
group_three_z = np.array([3.11, 3.67, 3.33, 3.78, 3.04, 3.98, 3.65, 3.23, 3.67, 3.87])

# point = np.array([5.5, 3, 2.25])  # Green example
# point = np.array([2.34, 8.21, 1.66])  # Blue example
# point = np.array([7.75, 8.23, 3.15])  # Red example
point = np.array([6.21, 5.76, 2.22])  # Other example

#  Calculating the distances
distances = []
for i in range(len(group_one_x)):
    d = (point[0] - group_one_x[i])**2 + (point[1] - group_one_y[i])**2 + (point[2] - group_one_z[i])**2
    distances.append((d, 'one'))

    d = (point[0] - group_two_x[i]) ** 2 + (point[1] - group_two_y)[i] ** 2 + (point[2] - group_two_z[i])**2
    distances.append((d, 'two'))

    d = (point[0] - group_three_x[i]) ** 2 + (point[1] - group_three_x[i]) ** 2 + (point[2] - group_three_z[i])**2
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
fig = plt.figure()
axis = plt.axes(projection="3d")

axis.scatter3D(group_one_x, group_one_y, group_one_z, c='green')
axis.scatter3D(group_two_x, group_two_y, group_two_z, c='blue')
axis.scatter3D(group_three_x, group_three_y, group_three_z, c='red')
axis.scatter3D(point[0], point[1], point[2], c='orange')
plt.show()
