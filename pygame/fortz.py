import pygame

X, Y = 960, 640
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("name")


# sprites needed: robot, dog, airstriker, gun_1, gun_2, gun_3, ammo_b, dog_b, airstriker_b, floor, bg
p_height, p_width = 20, 28.5
b_height, b_width = 32, 32
p1 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/fortz/player_1.png")
p1 = pygame.transform.scale(p1, (p_height, p_width))
p2 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/fortz/player_2.png")
p2 = pygame.transform.scale(p2, (p_height, p_width))
block_list = []
for item in range(4):
    block = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/fortz/block_{0}hp.png".format(str(item+1)))
    block = pygame.transform.scale(block, (b_height, b_width))
    block_list.append(block)
floor_height = 512
floor = pygame.Rect(0, floor_height, 960, 140)

movement_speed = 3


def draw_win(p_1_box, p_2_box, box_coords, test_list):
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (0, 0, 0), bg)
    pygame.draw.rect(win, (220, 140, 50), floor)

    win.blit(p1, (p_1_box.x, p_1_box.y))
    win.blit(p2, (p_2_box.x, p_2_box.y))

    for item in box_coords:
        win.blit(block_list[item[2]-1], (item[0]*32, item[1]*32))

    for item in test_list:
        a = pygame.Rect(item[0], item[1], 1, 1)
        pygame.draw.rect(win, (255, 0, 0), a)

    pygame.display.update()


def p1_move(keys, box, accel, box_coords, jump, place, on_ground, test_list):

    move_r = -1
    move_l = -1

    for item in box_coords:
        if box.y + box.height >= item[1]*32 and box.x < item[0]*32 + 32 and box.x > item[0]*32 - box.width and box.y < item[1]*32:

            on_ground = 1
            accel = 0
            box.y = item[1]*32 - box.height

    if box.y + box.height >= floor_height:
        on_ground = 1
        accel = 0
        box.y = floor_height - box.height
    if jump and on_ground == 1:
        accel = 15
        on_ground = 0

    for item in box_coords:

        if box.y > item[1]*32 + 32 and box.x < item[0]*32 + 32 and box.x > item[0]*32 - box.width and box.y - accel < item[1]*32+32:
            accel = 0
            box.y = item[1] * 32 + 32

        if box.x <= item[0] * 32 - box.width and box.y + box.height > item[1]*32 and box.y <= item[1]*32 + 33 and box.x + movement_speed > item[0] * 32 - box.width:
            box.x -= box.x - (item[0] * 32 - box.width)
            move_r = 1
        if box.x >= item[0] * 32 + 32 and box.y + box.height > item[1]*32 and box.y <= item[1]*32 + 33 and box.x - movement_speed < item[0] * 32 + 32:
            box.x += (item[0] * 32 + 32) - box.x
            move_l = 1

    if keys[pygame.K_a] and box.x - movement_speed > 0 and move_l == -1:
        box.x -= movement_speed
    if keys[pygame.K_d] and box.x + movement_speed + box.width < X and move_r == -1:
        box.x += movement_speed

    if place:
        if [(box.x + box.width/2)//32, box.y//32-1, 4] not in box_coords:
            box_coords.append([(box.x + box.width/2)//32, box.y//32-1, 4])
    box.y -= accel
    accel -= 1

    test_list.append([box.x, box.y])

    return accel, box_coords, on_ground, test_list


def p2_move(keys, box, accel, box_coords, jump, place, on_ground):
    for item in box_coords:
        if box.y + box.height >= item[1] * 32 and box.x <= item[0] * 32 + 32 and box.x >= item[0] * 32 - box.width and box.y <= item[1] * 32:
            accel = 0
            box.y = item[1] * 32 - 30

        if keys[pygame.K_LEFT] and box.x - movement_speed > 0 and box.x <= item[0] * 32 - box.width and box.x >= item[0] * 32 + 32:
            box.x -= movement_speed
        if keys[pygame.K_RIGHT] and box.x + movement_speed + box.width < X:
            box.x += movement_speed

    if box.y + box.height >= floor_height:
        accel = 0
        box.y = floor_height - box.height

    if keys[pygame.K_UP]:
        accel = 8
    box.y -= accel
    accel -= 1
    return accel, box_coords, on_ground


def main():
    #
    test_list = [[0, 0]]
    #
    p_1_box = pygame.Rect(100, 400, p_height, p_width)
    p_2_box = pygame.Rect(800, 400, p_height, p_width)
    p_1_accel = 0
    p_2_accel = 0
    box_coords = [[2, 15, 3]]
    on_ground = 1

    clock = pygame.time.Clock()
    run = 1
    while run:
        jump_1 = 0
        jump_2 = 0
        place_1 = 0
        place_2 = 0

        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    jump_1 = 1
                if event.key == pygame.K_w:
                    jump_2 = 1
                if event.key == pygame.K_s:
                    place_1 = 1
                if event.key == pygame.K_DOWN:
                    place_2 = 1


        keys = pygame.key.get_pressed()
        p_1_accel, box_coords, on_ground, test_list = p1_move(keys, p_1_box, p_1_accel, box_coords, jump_1, place_1, on_ground, test_list)
        p_2_accel, box_coords, on_ground = p2_move(keys, p_2_box, p_2_accel, box_coords, jump_2, place_2, on_ground)
        draw_win(p_1_box, p_2_box, box_coords, test_list)


if __name__ == "__main__":
    main()