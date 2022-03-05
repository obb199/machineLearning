import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
import pickle


def reading_data(file):
    with open(file, 'r') as f:
        csv = f.read().split('\n')
        x = [-1]
        y_movement = []
        for i in range(1, len(csv)):
            play = csv[i].split(',')
            if (float(play[0]), float(play[1])) != x[-1]:
                x.append((float(play[0]), float(play[1])))
        x.pop(0)
        for i in range(1, len(x)):
            if x[i-1][0] == x[i][0]:
                if x[i-1][1] > x[i][1]:
                    y_movement.append(-1)
                elif x[i-1][1] < x[i][1]:
                    y_movement.append(1)
            else:
                y_movement.append(0)

    return np.array(x), np.array(y_movement)


def test_tree(real_y, predict_y):
    accuracy = 0
    for i in range(len(real_y)):
        if real_y[i] == predict_y[i]:
            accuracy += 1

    return accuracy * 100 / len(real_y)


if __name__ == '__main__':
    X, y_mov = reading_data('data.csv')

    # Data for predict how side the bar needs to go
    X_train_mov, X_test_mov, y_train_mov, y_test_mov = train_test_split(X, y_mov, train_size=0.3, random_state=0)

    movement_tree = tree.DecisionTreeClassifier(max_depth=8, min_samples_leaf=2)
    movement_tree.fit(X_train_mov, y_train_mov)

    predict_movement = movement_tree.predict(X_test_mov)

    print('ACCURACY MOVEMENT TREE: %.2f%%' % test_tree(y_test_mov, predict_movement))

    # Saving the model
    with open('gamer_tree_movement', 'wb') as f:
        pickle.dump(movement_tree, f)
