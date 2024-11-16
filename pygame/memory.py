import random
import pygame

pygame.font.init()
text_font = pygame.font.SysFont("Arial Black", 20)

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("memory")

TIME = 30
WORDS = 3
text = open("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/memory/text.txt", "r")
text = text.read()
text = text.split("\n")
word_list = []

def draw_win(word):
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (0, 0, 0), bg)

    item_list = []
    item_text = ""
    i = 0
    for item in word:
        i += 1
        text_text = text_font.render(item_text + item, True, (255, 255, 255))
        if text_text.get_width() > (X - 50):
            item_list.append(item_text)
            item_text = ""
        if i == len(word):
            item_list.append(item_text + item)
        item_text += item


    i = 0
    for item in item_list:
        i += 1
        text_text = text_font.render(item, True, (255, 255, 255))
        win.blit(text_text, (250 - text_text.get_width()//2, 250 - (text_text.get_height()//2)*(len(item_list)+1) + text_text.get_height()*i))

    dot = pygame.Rect(250, 250, 1, 1)
    pygame.draw.rect(win, (255, 0, 0), dot)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = 1
    pressed = 1
    count = 0
    while run:
        clock.tick(fps)
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressed = 1
                if event.key == pygame.K_SPACE:
                    command = ""
                    for item in word_list:
                        words = ""
                        for word in item:
                            words += word
                        command += words + "\n"
                    print(command)
                    word_list.clear()
        if pressed == 1:
            word = []
            for item in range(WORDS):
                word.append(text[random.randint(0, len(text)-1)] + " ")
                count = 0
            word_list.append(word)
        if count >= TIME:
            word = ""
        pressed = 0
        draw_win(word)


if __name__ == "__main__":
    main()