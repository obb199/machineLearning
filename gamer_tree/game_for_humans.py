import pygame
import random


def show_base(x):
    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(x, 550, 240, 30))  # (pos em x, pos y, tam. horizontal, tam. vertical)


def show_point(x, y):
    pygame.draw.rect(screen, (0, 255, 0),
                     pygame.Rect(x, y, 20, 20))  # (pos em x, pos y, tam. horizontal, tam. vertical)


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def save_plays(point_x, base_x, file):
    data = str(point_x) + ',' + str(base_x) + '\n'

    with open(file, 'a') as f:
        f.write(data)


pygame.init()
X_SCREEN = 800
Y_SCREEN = 600

screen = pygame.display.set_mode((X_SCREEN, Y_SCREEN))
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

base_x_position = random.randint(30, 770)
point_x_position = 50
point_y_position = 100

if __name__ == '__main__':
    running = True
    # Game loop
    while running:
        save_plays(point_x_position, base_x_position, 'data.csv')  # Function to save information of current frame
        pygame.display.set_mode((X_SCREEN, Y_SCREEN))

        # COMMANDS OF PLAYER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # to break the loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    base_x_position -= 50
                elif event.key == pygame.K_RIGHT:
                    base_x_position += 50

                if base_x_position < 0:
                    base_x_position = 0
                if base_x_position > 800 - 240:
                    base_x_position = 800 - 240

        # update images
        show_base(base_x_position)
        show_point(point_x_position, point_y_position)
        show_score(600, 20)
        point_y_position += 0.5

        # IF POINT PASS THE BASE
        if point_y_position >= 580:
            running = False

        # COLLISION
        if 530 <= point_y_position <= 560 and base_x_position-20 <= point_x_position <= base_x_position + 240:
            point_x_position = random.randint(30, 770)
            point_y_position = 0
            score_value += 1

        pygame.display.update()
