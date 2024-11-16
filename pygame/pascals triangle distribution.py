import pygame
import math


n = 160
height = []

for k in range(0, n+1):
    height.append(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))

max = 0
for item in height:
    if item > max:
        max = item

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("binomial probability")


def draw_win():
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (90, 90, 90), bg)
    trim = 0
    for item in range(0, n+1):
        if (height[item]/max)*480 < 1:
            trim += 1

    for item in range((trim//2), n+1-(trim//2)):
        square = pygame.Rect(10+((X-20)//(n+1-trim))*(1+item-(trim//2)), 490-(height[item]/max)*480, ((X-20)//(n+1-trim)), (height[item]/max)*480)
        pygame.draw.rect(win, (200, 50, 200), square)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = 1
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_win()


if __name__ == "__main__":
    main()