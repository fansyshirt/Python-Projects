# things to improve:
#
# idiot proof the program
# pressing keys that are not in keys{} throws error
# allow only nums or only char in var name and values
# fix floating point rounding using :.2f form
#

import pygame

pygame.font.init()
font1 = pygame.font.SysFont("Arial", 16)
font2 = pygame.font.SysFont("Arial", 14)
font3 = pygame.font.SysFont("Arial", 10)

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 10

pygame.display.set_caption("IB Physics Error Calculator")

keys = {
    8: "delete",
    46: ".",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    97: "A",
    98: "B",
    99: "C",
    100: "D",
    101: "E",
    102: "F",
    103: "G",
    104: "H",
    105: "I",
    106: "J",
    107: "K",
    108: "L",
    109: "M",
    110: "N",
    111: "O",
    112: "P",
    113: "Q",
    114: "R",
    115: "S",
    116: "T",
    117: "U",
    118: "V",
    119: "W",
    120: "X",
    121: "Y",
    122: "Z"
}


def draw_win(vars, equation, prop_error, cur_pos, symbols):

    if True:  # allows pycharm to minimise block
        bg = pygame.Rect(0, 0, X, Y)
        colour_bg = (238, 238, 238)
        pygame.draw.rect(win, colour_bg, bg)

        colour_line = (200, 200, 200)

        line = pygame.Rect(20, 20, 10, 2)  # Variable box
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(20, 20, 2, 220)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(20, 240, 460, 2)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(90, 20, 390, 2)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(478, 20, 2, 222)
        pygame.draw.rect(win, colour_line, line)
        text = font1.render("Variables", 1, (0, 0, 0))
        win.blit(text, (35, 12))
        line = pygame.Rect(35, 53, 428, 176)
        pygame.draw.rect(win, (252, 252, 252), line)

        for item in range(3):
            line = pygame.Rect(140 + item*112, 44, 5, 185)
            pygame.draw.rect(win, colour_bg, line)

        for item in range(4):
            line = pygame.Rect(35, 84 + item*36, 428, 5)
            pygame.draw.rect(win, colour_bg, line)

        text = font2.render("Name", 1, (0, 0, 0))
        win.blit(text, (40, 33))
        text = font2.render("Measurement", 1, (0, 0, 0))
        win.blit(text, (152, 33))
        text = font2.render("Equipment Error", 1, (0, 0, 0))
        win.blit(text, (264, 33))
        text = font2.render("Percent Error", 1, (0, 0, 0))
        win.blit(text, (376, 33))

        line = pygame.Rect(20, 265, 10, 2)  # Equation box
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(20, 265, 2, 60)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(20, 325, 460, 2)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(90, 265, 390, 2)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(478, 265, 2, 60)
        pygame.draw.rect(win, colour_line, line)
        text = font1.render("Equation", 1, (0, 0, 0))
        win.blit(text, (35, 258))
        line = pygame.Rect(35, 280, 428, 35)
        pygame.draw.rect(win, (252, 252, 252), line)

        colour_button1 = (150, 150, 150)
        colour_button2 = (100, 100, 100)
        for item in range(8):  #                   Button symbols
            line = pygame.Rect(35 + 55*item, 338, 35, 35)
            pygame.draw.rect(win, colour_button1, line)
            line = pygame.Rect(35 + 55*item, 338, 35, 2)
            pygame.draw.rect(win, colour_button2, line)
            line = pygame.Rect(35 + 55*item, 338, 2, 35)
            pygame.draw.rect(win, colour_button2, line)
            line = pygame.Rect(70 + 55*item, 338, 2, 36)
            pygame.draw.rect(win, colour_button2, line)
            line = pygame.Rect(35 + 55*item, 372, 35, 2)
            pygame.draw.rect(win, colour_button2, line)
            text = font1.render(symbols[item], 1, (0, 0, 0))
            win.blit(text, (35 + 55*item + 18 - text.get_width()/2, 336 + text.get_height()/2))

        line = pygame.Rect(20, 400, 10, 2)  # Prop. error
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(20, 400, 2, 60)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(20, 460, 460, 2)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(140, 400, 340, 2)
        pygame.draw.rect(win, colour_line, line)
        line = pygame.Rect(478, 400, 2, 60)
        pygame.draw.rect(win, colour_line, line)
        text = font1.render("Propogation Error", 1, (0, 0, 0))
        win.blit(text, (35, 390))
        line = pygame.Rect(35, 413, 428, 35)
        pygame.draw.rect(win, (252, 252, 252), line)

        text = font1.render("E = ", 1, (0, 0, 0))
        win.blit(text, (46, 287))

    for col in range(5):
        for row in range(4):
            text = font1.render((vars[col][row] + (row//3)*"%"), 1, (0, 0, 0))
            win.blit(text, (45 + row*112, 58 + col*36))
            if cur_pos[1] == col and cur_pos[0] == row and cur_pos[2] == 0:
                line = pygame.Rect(45 + row*112 + text.get_width(), 58 + col*36, 2, 20)
                pygame.draw.rect(win, (0, 0, 0), line)
    text = font1.render(equation, 1, (0, 0, 0))
    win.blit(text, (75, 287))
    if cur_pos[0] == -1:
        line = pygame.Rect(75 + text.get_width(), 287, 2, 20)
        pygame.draw.rect(win, (0, 0, 0), line)
    text = font1.render(prop_error, 1, (0, 0, 0))
    win.blit(text, (35, 413))
    # (35, 413, 428, 35)

    pygame.display.update()


def main():
    coords = (0, 0, -1)
    vars = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    equation = ""
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    chars = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    sym_list = ["+", "-", "×", "÷", "(", ")", "^", "π"]
    key_press = ""
    clock = pygame.time.Clock()
    run = 1
    while run:
        vars_dict = {}
        button_press = 0
        mouse_pos = (0, 0)
        prop_error = ""
        pressed = 0
        clicked = 0
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #key_press = keys[event.key]
                try:
                    key_press = keys[event.key]
                    pressed = 1
                except:
                    print("error")
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = 1
                print("click")

        if True: #  minimise mouse typing and mouse
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                mouse_pos = pygame.mouse.get_pos()
            if 35 < mouse_pos[0] < 355 and 53 < mouse_pos[1] < 228:
                coords = (mouse_pos[0] - 35)//112, (mouse_pos[1] - 53)//36, 0
            if 35 < mouse_pos[0] < 463 and 280 < mouse_pos[1] < 315:
                coords = (-1, -1, -1)
            if 35 < mouse_pos[0] < 455 and 335 < mouse_pos[1] < 370:
                if 35 < mouse_pos[0] < 70:
                    button_press = 1
                if 90 < mouse_pos[0] < 125:
                    button_press = 2
                if 145 < mouse_pos[0] < 180:
                    button_press = 3
                if 200 < mouse_pos[0] < 235:
                    button_press = 4
                if 255 < mouse_pos[0] < 290:
                    button_press = 5
                if 310 < mouse_pos[0] < 345:
                    button_press = 6
                if 365 < mouse_pos[0] < 400:
                    button_press = 7
                if 420 < mouse_pos[0] < 455:
                    button_press = 8

            if coords[0] == 0 and pressed == 1:
                if key_press != "delete" and key_press in chars:
                    vars[coords[1]][0] = key_press
                if key_press == "delete":
                    vars[coords[1]][0] = vars[coords[1]][0][:-1]
            if coords[0] == 1 and pressed == 1:
                if key_press != "delete" and key_press in nums:
                    vars[coords[1]][1] += key_press
                if key_press == "delete":
                    vars[coords[1]][1] = vars[coords[1]][1][:-1]
            if coords[0] == 2 and pressed == 1:
                if key_press != "delete" and key_press in nums:
                    vars[coords[1]][2] += key_press
                if key_press == "delete":
                    vars[coords[1]][2] = vars[coords[1]][2][:-1]
            if coords[0] == -1 and pressed == 1:
                if key_press != "delete" and key_press:
                    equation += key_press
                if key_press == "delete":
                    equation = equation[:-1]
        if button_press > 0 and clicked == 1:
            equation += sym_list[button_press-1]
            coords = (-1, -1, -1)
        for item in range(5):
            try:
                vars[item][3] = str((float(vars[item][2])/float(vars[item][1])*10000000//1)/10000000*100)
            except:
                pass
        for item in range(5):
            if vars[item][0] != "" and vars[item][3] != "":
                vars_dict[vars[item][0]] = vars[item][3]
        #print(vars_dict)

        val_location = []
        i = 0
        for item in equation:
            if item in vars_dict:
                #print(vars_dict[item])
                val_location.append(i)
            i += 1

        val_exponent = []
        for item in val_location:
            try:
                if equation[item+1] == "^":
                    if equation[item+2] in number:
                        val_exponent.append(equation[item+2])
                    else:
                        val_exponent.append("1")
                else:
                    val_exponent.append("1")
            except:
                val_exponent.append("1")
        i = 0
        sum_error = 0
        for item in val_location:
            try:
                sum_error += float(vars_dict[equation[int(item)]]) * float(val_exponent[i])
            except:
                pass
            i += 1
        prop_error = str(sum_error)
        draw_win(vars, equation, prop_error, coords, sym_list)


if __name__ == "__main__":
    main()
