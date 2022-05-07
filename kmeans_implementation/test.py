from kmeans import *
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def points_generator(dimension, n_groups, elements_per_group, distance_groups):
    points = []
    k = 0

    for _ in range(n_groups):
        for n in range(elements_per_group):
            points.append([randint(k, 100+k) for _ in range(dimension)])
        k += distance_groups

    return points


if __name__ == '__main__':
    #Example for 3D points
    points = points_generator(3, 3, 50, 100)
    x = []
    y = []
    z = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
        z.append(p[2])

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(x, y, z, c=z, cmap='cividis');

    teste = k_means(n_clusters=3, max_iterations=100, distance_type='euclidian')
    teste.fit(points)

    x = []
    y = []
    z = []
    for centroid in teste.get_centroids():
        x.append(centroid[0])
        y.append(centroid[1])
        z.append(centroid[2])

    ax.scatter3D(x, y, z, c='red')
    plt.show()

    points = points_generator(2, 3, 50, 100)
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])

    plt.scatter(x, y, alpha=0.35)

    #example for 2D points
    teste2 = k_means(n_clusters=3, max_iterations=100, distance_type='euclidian')
    teste2.fit(points)

    x = []
    y = []
    for centroid in teste2.get_centroids():
        x.append(centroid[0])
        y.append(centroid[1])

    plt.scatter(x, y, c='#ff0000')
    plt.show()