import random
import pygame

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("name")


def collision(s1, s2, m):
    # if no collision return -1 if collision return (dx, dy)
    # s1[0] -> s1[0]+m[0]
    # s1[1] -> s1[1]+m[1]
    col_x = 0
    col_y = 0
    collide = [0, 0]
    if s2[0] < s1[0]+m[0] < s2[0] + s2[2] and s1[1]+m[1] < s2[1] + s2[3] and s1[1]+m[1] + s1[3] > s2[1]:
        collide[0] = ((s2[0]+s2[2]) - s1[0]+m[0])
        col_x = 1
        print("right")
    if s2[1] < s1[1]+m[1] < s2[1] + s2[3] and s1[0]+m[0] < s2[0] + s2[2] and s1[0]+m[0] + s1[2] > s2[0]:
        collide[1] = ((s2[1] + s2[3]) - s1[1]+m[1])
        col_y = 1
        print("bottom")
    if s1[0]+m[0] < s2[0] < s1[0]+m[0] + s1[2] and s2[1] < s1[1]+m[1] + s1[3] and s2[1] + s2[3] > s1[1]:
        collide[0] = (s2[0] - (s1[0]+m[0] + s1[2]))
        col_x = 1
        print("left")
    if s1[1]+m[1] < s2[1] < s1[1]+m[1] + s1[3] and s2[0] < s1[0]+m[0] + s1[2] and s2[0] + s2[2] > s1[0]:
        collide[1] = (s2[1] - (s1[1]+m[1] + s1[3]))
        col_y = 1
        print("top")
    return collide, col_x, col_y


def player_move(s1, s2, move):
    coll, x, y = collision(s1, s2, move)
    if coll == -1:
        s1[0] += move[0]
        s1[1] += move[1]
    else:
        pass
    return s1


def draw_win(s1, s2):
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (0, 0, 0), bg)

    rec1 = pygame.Rect(s1[0], s1[1], s1[2], s1[3])
    rec2 = pygame.Rect(s2[0], s2[1], s2[2], s2[3])
    pygame.draw.rect(win, (200, 50, 50), rec1)
    pygame.draw.rect(win, (50, 200, 50), rec2)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = 1
    pressed = 1
    square_1 = [100, 120, 50, 80]
    square_2 = [90, 78, 12, 103]
    movement = []
    while run:
        movement = [0, 0]
        clock.tick(fps)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            movement[1] = -5
        if keys[pygame.K_a]:
            movement[0] = -5
        if keys[pygame.K_s]:
            movement[1] = 5
        if keys[pygame.K_d]:
            movement[0] = 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressed = 1
                #if event.key == pygame.K_SPACE:
                #    print(collision(square_1, square_2, movement))

        if pressed == 1:
            pressed = 0
            rand1 = random.randint(50, 350)
            rand2 = random.randint(50, 350)
            rand3 = 150
            rand4 = 150
            square_1 = [rand1, rand2, rand3, rand4]
            rand1 = 170
            rand2 = 170
            rand3 = 150
            rand4 = 150
            square_2 = [rand1, rand2, rand3, rand4]
        square_1 = player_move(square_1, square_2, movement)
        draw_win(square_1, square_2)


if __name__ == "__main__":
    main()
