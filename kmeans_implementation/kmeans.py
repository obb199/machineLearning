from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class k_means:
    def __init__(self, n_clusters=2, max_iterations=100, distance_type='euclidian'):
        self.__n_clusters=n_clusters
        self.__max_iterations = max_iterations
        self.__distance_type = distance_type
        self.__centroids_positions = []

    def get_centroids(self):
        return self.__centroids_positions

    def fit(self, points):
        # inicializando aleatoriamente os centróides
        self.__centroids_positions = [[randint(0, 100) for _ in range(len(points[0]))] for _ in range(self.__n_clusters)]

        iters = -1
        while iters < self.__max_iterations:
            iters += 1
            distance_points = []

            # calculando a distância de cada ponto até cada um dos centróides
            for i in range(len(points)):
                dist = []
                for j in range(len(self.__centroids_positions)):
                    if self.__distance_type == 'euclidian':
                        dist.append(sum([(points[i][k] - self.__centroids_positions[j][k]) ** 2 for k in range(len(points[0]))]) ** 0.5)
                    elif self.__distance_type == 'manhattan':
                        #For the future (or not)
                        pass

                distance_points.append(dist)

            elements_per_centroid = [0 for _ in range(self.__n_clusters)]
            sum_of_distances = [[0 for _ in points[0]] for _ in range(self.__n_clusters)]

            # calculando em qual centróide cada ponto está mais próximo
            partial_result = [index_smaller_element(p) for p in distance_points]

            # evitando a divisão por zero
            for i in range(len(elements_per_centroid)):
                if elements_per_centroid[i] == 0:
                    elements_per_centroid[i] += 1

            # calculando a soma das distâncias do centróide mais perto para cada ponto
            for idx in range(len(partial_result)):
                elements_per_centroid[partial_result[idx]] += 1
                for dim in range(len(points[0])):
                    sum_of_distances[partial_result[idx]][dim] += points[idx][dim]

            # calculando a nova posição dos centróides
            new_centroids_positions = [
                [sum_of_distances[i][k] / elements_per_centroid[i] for k in range(len(points[0]))] for i in
                range(self.__n_clusters)]

            # verificando se o conjunto convergiu
            if new_centroids_positions == self.__centroids_positions:
                return self.__centroids_positions

            self.__centroids_positions = new_centroids_positions

    def predict(self, points):
        res = []

        for i in range(len(points)):
            dist = []
            for j in range(len(self.__centroids_positions)):
                if self.__distance_type == 'euclidian':
                    dist.append(sum([(points[i][k] - self.centroids_positions[j][k]) ** 2 for k in range(len(points[0]))]) ** 0.5)
            res.append(dist)

        res = [index_smaller_element(r) for r in res]

        return res

def index_smaller_element(vec):
    smaller_idx = 0
    smaller_value = vec[0]

    for i in range(len(vec)):
        if vec[i] < smaller_value:
            smaller_value = vec[i]
            smaller_idx = i

    return smaller_idx
