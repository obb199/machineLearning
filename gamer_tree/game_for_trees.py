import pickle
from game_for_humans import *


def show_score(x, y):
    """
    for some reason idk, I needed to make a new show_score function with other score
    variable to work equals the other file. If you discover why this happens tell for me.
    """
    score = font.render("SCORE : " + str(tree_points), True, (255, 255, 255))
    screen.blit(score, (x, y))


if __name__ == '__main__':
    gamer_tree = pickle.load(open("gamer_tree_movement", 'rb'))  # loading trained model
    tree_points = 0

    running = True
    while running:
        pygame.display.set_mode((X_SCREEN, Y_SCREEN))
        # COMMANDS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # to break loop game

        movement = gamer_tree.predict([[point_x_position, base_x_position]])  # Choice of tree
        if movement == 1:
            base_x_position += 50
        elif movement == -1:
            base_x_position -= 50

        # Updates for bar don't pass the scree limit
        if base_x_position < 0:
            base_x_position = 0
        if base_x_position > 800 - 240:
            base_x_position = 800 - 240

        # update images
        show_base(base_x_position)
        show_point(point_x_position, point_y_position)
        show_score(600, 20)
        point_y_position += 1

        # POINT PASS THE BASE
        if point_y_position >= 580:
            point_x_position = random.randint(30, 770)
            point_y_position = 0
            running = False

        # COLLISION
        if 530 <= point_y_position <= 560 and base_x_position-20 <= point_x_position <= base_x_position + 240:
            point_x_position = random.randint(30, 770)
            point_y_position = 0
            tree_points += 1

        pygame.display.update()

    print(score_value)
