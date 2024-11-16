import pygame

pygame.font.init()
hp_font = pygame.font.SysFont("comicsans", 20)
win_font = pygame.font.SysFont("Arial Black", 40)

X, Y = 900, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("2 player game")

border = pygame.Rect(X//2 - 5, 0, 10, Y)

ship_w, ship_h = 55, 40
player1_char = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/2 player game/player1.png")
p1 = pygame.transform.scale(player1_char, (ship_w, ship_h))
player2_char = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/2 player game/player2.png")
p2 = pygame.transform.rotate(pygame.transform.scale(player2_char, (ship_w, ship_h)), 180)

ship_movement_speed = 3

p1_hit = pygame.USEREVENT + 1
p2_hit = pygame.USEREVENT + 2

max_bullet = 5

bullet_movement_speed = 7

score = [0, 0]

bg = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/2 player game/download1.jfif"), (X, Y))


def draw_win(yellow, red, p1_bul, p2_bul, p1_hp, p2_hp, score):
    win.blit(bg, (0, 0))

    pygame.draw.rect(win, (0, 0, 0), border)

    win.blit(p1, (yellow.x, yellow.y))
    win.blit(p2, (red.x, red.y))

    p1_hp_text = hp_font.render("Health: " + str(p1_hp), 1, (255, 255, 255))
    p2_hp_text = hp_font.render("Health: " + str(p2_hp), 1, (255, 255, 255))
    p1_score_text = hp_font.render("Score: " + str(score[0]), 1, (255, 255, 255))
    p2_score_text = hp_font.render("Score: " + str(score[1]), 1, (255, 255, 255))
    win.blit(p1_hp_text, (10, 10))
    win.blit(p2_hp_text, (X - p2_hp_text.get_width() - 10, 10))
    win.blit(p1_score_text, (10, 20 + p1_score_text.get_height()))
    win.blit(p2_score_text, (X - p2_hp_text.get_width() - 10, 20 + p2_score_text.get_height()))


    for bullet in p1_bul:
        pygame.draw.rect(win, (255, 255, 0), bullet)

    for bullet in p2_bul:
        pygame.draw.rect(win, (255, 0, 0), bullet)
    pygame.display.update()


def p1_move(keys, yellow):
    if keys[pygame.K_w] and yellow.y - ship_movement_speed > 0:
        yellow.y -= ship_movement_speed
    if keys[pygame.K_a] and yellow.x - ship_movement_speed > 0:
        yellow.x -= ship_movement_speed
    if keys[pygame.K_s] and yellow.y + ship_movement_speed < Y - yellow.height:
        yellow.y += ship_movement_speed
    if keys[pygame.K_d] and yellow.x + ship_movement_speed < border.x - yellow.width:
        yellow.x += ship_movement_speed


def p2_move(keys, red):
    if keys[pygame.K_UP] and red.y - ship_movement_speed > 0:
        red.y -= ship_movement_speed
    if keys[pygame.K_LEFT] and red.x - ship_movement_speed > border.x + border.width:
        red.x -= ship_movement_speed
    if keys[pygame.K_DOWN] and red.y + ship_movement_speed < Y - red.height:
        red.y += ship_movement_speed
    if keys[pygame.K_RIGHT] and red.x + ship_movement_speed < X - red.width:
        red.x += ship_movement_speed


def bullet_handle(p1_bul, p2_bul, yellow, red):
    for bullet in p1_bul:
        bullet.x += bullet_movement_speed
        if red.colliderect(bullet):
            p1_bul.remove(bullet)
            pygame.event.post(pygame.event.Event(p2_hit))
        elif bullet.x > X:
            p1_bul.remove(bullet)
    for bullet in p2_bul:
        bullet.x -= bullet_movement_speed
        if yellow.colliderect(bullet):
            p2_bul.remove(bullet)
            pygame.event.post(pygame.event.Event(p1_hit))
        elif bullet.x < 0:
            p2_bul.remove(bullet)


def show_win(winner, score):
    change = 1
    if winner == "PLAYER 1 WON":
        win_text = win_font.render(str(winner), 1, (255, 255, 0))
        win.blit(win_text, (X / 2 - win_text.get_width() // 2, Y / 2 - win_text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(5000)
        score[0] += 1
        change = 0
    if winner == "PLAYER 2 WON":
        win_text = win_font.render(str(winner), 1, (255, 0, 0))
        win.blit(win_text, (X / 2 - win_text.get_width() // 2, Y / 2 - win_text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(5000)
        score[1] += 1
        change = 0
    return score, change


def main(score):

    max_hp = 10
    p1_hp = max_hp
    p2_hp = max_hp
    p1_bul = []
    p2_bul = []
    win_text = ""

    yellow = pygame.Rect(100, Y//2 - ship_h//2, ship_w, ship_h)
    red = pygame.Rect(X - 100 - ship_w, Y//2 - ship_h//2, ship_w, ship_h)

    clock = pygame.time.Clock()
    run = 1

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and len(p1_bul) < max_bullet:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 1, 8, 6)
                    p1_bul.append(bullet)
                if event.key == pygame.K_SPACE and len(p2_bul) < max_bullet:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 1, 8, 6)
                    p2_bul.append(bullet)
            if event.type == p1_hit:
                p1_hp -= 1
            if event.type == p2_hit:
                p2_hp -= 1

        if p1_hp <= 0:
            win_text = "PLAYER 2 WON"
        if p2_hp <= 0:
            win_text = "PLAYER 1 WON"


        keys = pygame.key.get_pressed()
        p1_move(keys, yellow)
        p2_move(keys, red)
        bullet_handle(p1_bul, p2_bul, yellow, red)
        score, run = show_win(win_text, score)
        draw_win(yellow, red, p1_bul, p2_bul, p1_hp, p2_hp, score)
    main(score)


if __name__ == "__main__":
    main(score)
