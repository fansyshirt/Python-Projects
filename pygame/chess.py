import pygame

pygame.font.init()
num_font = pygame.font.SysFont("Courier New", 20)

X, Y = 550, 550
win = pygame.display.set_mode((X, Y))
fps = 60
pygame.display.set_caption("chess")

B_P = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/B_1.png"), (20, 30))
B_N = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/B_2.png"), (25, 30))
B_B = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/B_3.png"), (20, 30))
B_R = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/B_4.png"), (25, 30))
B_Q = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/B_5.png"), (30, 30))
B_K = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/B_6.png"), (30, 30))
W_P = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/W_1.png"), (20, 30))
W_N = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/W_2.png"), (25, 30))
W_B = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/W_3.png"), (20, 30))
W_R = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/W_4.png"), (25, 30))
W_Q = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/W_5.png"), (30, 30))
W_K = pygame.transform.scale(pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/chess/W_6.png"), (30, 30))

board = [["B_R", "B_N", "B_B", "B_K", "B_Q", "B_B", "B_N", "B_R"],
         ["B_P", "B_P", "B_P", "B_P", "B_P", "B_P", "B_P", "B_P"],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["W_P", "W_P", "W_P", "W_P", "W_P", "W_P", "W_P", "W_P"],
         ["W_R", "W_N", "W_B", "W_K", "W_Q", "W_B", "W_N", "W_R"]]

board_list = [[], [], [], [], [], [], [], []]
i = 0
for axis_y in range(8):
    for axis_x in range(8):
        rec = pygame.Rect(75 + axis_x * 50, 75 + axis_y * 50, 50, 50)
        board_list[i].append(rec)
    i += 1
print(board_list)


def show_board(board):
    for row in board:
        text = ""
        for item in row:
            text += item + " "
        print(text)


def draw_win(board_list, board, mouse_pos):
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (90, 90, 90), bg)
    char = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    j = 0
    for row in board_list:
        j += 1
        i = 0
        num_text = num_font.render(char[j-1], True, (25, 25, 25))
        win.blit(num_text, (60, 40 + 50*j))
        for item in row:
            i += 1
            c = ((i + j) % 2) * 255
            pygame.draw.rect(win, (c, c, c), item)
            if board[j-1][i-1] != "":
                if board[j-1][i-1] == "B_P":
                    win.blit(B_P, (40 + 50*i, 35 + 50*j))
                if board[j-1][i-1] == "B_N":
                    win.blit(B_N, (37.5 + 50*i, 35 + 50*j))
                if board[j-1][i-1] == "B_B":
                    win.blit(B_B, (40 + 50*i, 35 + 50*j))
                if board[j-1][i-1] == "B_R":
                    win.blit(B_R, (37.5 + 50*i, 35 + 50*j))
                if board[j-1][i-1] == "B_K":
                    win.blit(B_K, (35 + 50*i, 35 + 50*j))
                if board[j-1][i-1] == "B_Q":
                    win.blit(B_Q, (35 + 50*i, 35 + 50*j))
                if board[j-1][i-1] == "W_P":
                    win.blit(W_P, (40 + 50 * i, 35 + 50 * j))
                if board[j-1][i-1] == "W_N":
                    win.blit(W_N, (37.5 + 50 * i, 35 + 50 * j))
                if board[j-1][i-1] == "W_B":
                    win.blit(W_B, (40 + 50 * i, 35 + 50 * j))
                if board[j-1][i-1] == "W_R":
                    win.blit(W_R, (37.5 + 50 * i, 35 + 50 * j))
                if board[j-1][i-1] == "W_K":
                    win.blit(W_K, (35 + 50 * i, 35 + 50 * j))
                if board[j-1][i-1] == "W_Q":
                    win.blit(W_Q, (35 + 50 * i, 35 + 50 * j))
    for item in range(8):
        num_text = num_font.render(str(item + 1), True, (25, 25, 25))
        win.blit(num_text, (90 + 50 * item, 55))
    pygame.display.update()


def main(board_list, board):
    clock = pygame.time.Clock()
    run = 1
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse_presses = pygame.mouse.get_pressed()
        mouse_pos = (0, 0)
        if mouse_presses[0]:
            mouse_pos = pygame.mouse.get_pos()
        draw_win(board_list, board, mouse_pos)
        #show_board(board)


main(board_list, board)
