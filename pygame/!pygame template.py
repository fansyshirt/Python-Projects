import pygame

#pygame.font.init()
#font1 = pygame.font.SysFont("comicsans", 20)

X, Y = 700, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("name")


def draw_win():
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (0, 0, 0), bg)
    
    #line = pygame.Rect(50, 40, 2, 280)
    #pygame.draw.rect(win, (20, 20, 20), line)

    #text = font1.render("text", 1, (255, 255, 255))
    #win.blit(text, (10, 10))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = 1
    while run:
        dt = fps * (clock.tick(fps)/1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_win()


if __name__ == "__main__":
    main()