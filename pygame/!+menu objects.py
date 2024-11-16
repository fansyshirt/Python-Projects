import pygame
import string


def box_hollow(win, coord_x, coord_y, width, height, thickness, colour1, colour2=None):
    line = pygame.Rect(coord_x, coord_y, thickness, height)
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coord_x+thickness, coord_y, width-thickness, thickness)
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coord_x+thickness, coord_y+height-thickness, width-2*thickness, thickness)
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coord_x+width-thickness, coord_y+thickness, thickness, height-thickness)
    pygame.draw.rect(win, colour1, line)
    if colour2:
        line = pygame.Rect(coord_x+thickness, coord_y+thickness, width-2*thickness, height-2*thickness)
        pygame.draw.rect(win, colour2, line)


def text_header(win, coords_x, coords_y, width, height, thickness, \
                margin1=0, margin2=0, margin3=0, margin4=0, margin5=0, \
                font=None, text="Text123", colour1=(0, 0, 0), colour2=(0, 0, 0), colour3=None):
    """
    :param margin1: gap between right text and right line
    :param margin2: gap between text and surrounding lines at top
    :param margin3: gap between bottom of text and internal box
    :param margin4: gap between internal box and surrounding lines
    :param margin5: vertical displacement of text box
    :param colour1: colour of border
    :param colour2: colour of text
    :param colour3: colour of internal box
    """
    if not font:
        pygame.font.init()
        font1 = pygame.font.SysFont("Arial", 12)

    text = font.render(text, 1, colour2)  # text
    if colour3:
        box = pygame.Rect(coords_x+thickness+margin4, coords_y+margin3+margin4+(text.get_height()-thickness)//2+margin5, width-2*thickness-2*margin4, height-thickness-2*margin4-margin3-(text.get_height()-thickness)//2-margin5)  # box
        pygame.draw.rect(win, colour3, box)
    win.blit(text, (coords_x+thickness+margin1+margin2, coords_y-text.get_height()//2+thickness//2+margin5))  # text

    line = pygame.Rect(coords_x+thickness, coords_y, margin1, thickness)  # margin 1 top
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coords_x+text.get_width()+thickness+margin1+2*margin2, coords_y, width-text.get_width()-margin1-2*margin2-thickness, thickness)  # top
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coords_x, coords_y, thickness, height)  # left
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coords_x+thickness, coords_y+height-thickness, width-thickness, thickness)  # bottom
    pygame.draw.rect(win, colour1, line)
    line = pygame.Rect(coords_x+width-thickness, coords_y+thickness, thickness, height-2*thickness)  # right
    pygame.draw.rect(win, colour1, line)


class TextBox():
    """
    ### ADD ALIGNMENT ###
    """
    keys = {
        8: "delete",
        13: "enter",
        32: " ",
        44: ",",
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
    cursor = (-1, -1)
    instances = []
    selected = None
    def __init__(self, coords_x, coords_y, width, height, text="", font=None, valid_chars=3, colour=(0, 0, 0), \
                 margin1=0, margin2=0, margin3=0, margin4=2, margin5=0, \
                 cursor_width=3, \
                 box_draw=True, box_colour=(255, 255, 255), \
                 multiline=False, \
                 align_horizontal=0, align_vertical=1):
        """
        :param margin1: gap between left border and text
        :param margin2: gap between top border and text
        :param margin3: gap between text and cursor
        :param margin4: gap between top border and cursor
        :param margin5: gap between newlines
        :param align_horizontal: 0-left 1-center 2-right
        :param align_vertical:   0-top  1-center 2-bottom
        """

        self.font = font
        self.x = coords_x
        self.y = coords_y
        self.width = width
        self.height = height
        self.text = text
        if not font:
            font = pygame.font.SysFont("Arial", 12)
        if isinstance(valid_chars, int):
            other_chars = " ,."
            if valid_chars == 0:  # lower
                valid_chars = list(string.ascii_lowercase+other_chars)
            elif valid_chars == 1:  # upper
                valid_chars = list(string.ascii_uppercase+other_chars)
            elif valid_chars == 2:  # digits
                valid_chars = list(string.digits+other_chars)
            elif valid_chars == 3:  # lower+upper+digits
                valid_chars = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+other_chars)
            else:
                valid_chars = []
        self.valid_chars = valid_chars
        self.colour = colour

        self.margin1 = margin1
        self.margin2 = margin2
        self.margin3 = margin3
        self.margin4 = margin4
        self.margin5 = margin5

        self.cursor_width = cursor_width

        self.box_draw = box_draw
        self.box_colour = box_colour

        self.multiline = multiline

        self.align_horizontal = align_horizontal
        self.align_vertical = align_vertical
        TextBox.instances.append(self)

    @staticmethod
    def handle_text(event):
        if event.key in TextBox.keys.keys() and TextBox.selected is not None:
            if TextBox.keys[event.key] == "delete":
                TextBox.selected.text = TextBox.selected.text[:-1]
            elif TextBox.keys[event.key] == "enter" and TextBox.selected.multiline:
                TextBox.selected.text += '\n'
            elif pygame.key.get_pressed()[pygame.K_LSHIFT]:
                if TextBox.keys[event.key].upper() in TextBox.selected.valid_chars:
                    TextBox.selected.text += TextBox.keys[event.key].upper()
                elif TextBox.keys[event.key].lower() in TextBox.selected.valid_chars:
                    TextBox.selected.text += TextBox.keys[event.key].lower()
            elif not pygame.key.get_pressed()[pygame.K_LSHIFT]:
                if TextBox.keys[event.key].lower() in TextBox.selected.valid_chars:
                    TextBox.selected.text += TextBox.keys[event.key].lower()
                elif TextBox.keys[event.key].upper() in TextBox.selected.valid_chars:
                    TextBox.selected.text += TextBox.keys[event.key].upper()

        elif event.key not in TextBox.keys.keys():
            print(event.key)


    @staticmethod
    def draw(win):
        select = None
        for item in TextBox.instances:
            if item.box_draw:
                line = pygame.Rect(item.x, item.y, item.width, item.height)
                pygame.draw.rect(win, item.box_colour, line)
            for iter, sentence in enumerate(item.text.split('\n')):
                text = item.font.render(sentence, 1, item.colour)
                win.blit(text, (item.x + item.margin1, item.y+item.margin2+(text.get_height()+item.margin5)*iter))
            if item.x < TextBox.cursor[0] < item.x + item.width and item.y < TextBox.cursor[1] < item.y + item.height:
                select = item
                line = pygame.Rect(item.x+item.margin1+item.margin3+text.get_width(), item.y+item.margin4+(text.get_height()+item.margin5)*iter, item.cursor_width, text.get_height()-2*item.margin4)
                pygame.draw.rect(win, item.colour, line)
        TextBox.selected = select


class Button():
    """
    ### ADD GLOBAL STATE LIST ###
    """
    instances = []
    selected = None
    cursor = (0, 0)
    def __init__(self, coords_x, coords_y, width, height, thickness=2, \
                 colour_box=[(230, 230, 230), (50, 50, 50)], colour_border=[(120, 120, 120), (120, 120, 120)], \
                 text='', colour_text=[(0, 0, 0), (0, 0, 0)], \
                 state=0):
        """
        :param colour_box:    [state 0, state 1]
        :param colour_border: [state 0, state 1]
        :param colour_text:   [state 0, state 1]
        """
        self.x = coords_x
        self.y = coords_y
        self.width = width
        self.height = height
        self.thickness = thickness

        self.colour_box = colour_box
        self.colour_border = colour_border

        self.text = text
        self.colour_text = colour_text

        self.state = state

        Button.instances.append(self)


    @staticmethod
    def handle_press():
        Button.cursor = pygame.mouse.get_pos()
        for item in Button.instances:
            if item.x < Button.cursor[0] < item.x + item.width and item.y < Button.cursor[1] < item.y + item.height:
                item.state ^= 1  # 0->1 1->0

    @staticmethod
    def draw(win):
        for item in Button.instances:
            if item.thickness != 0:
                box_hollow(win, item.x, item.y, item.width, item.height, item.thickness, item.colour_border[item.state], item.colour_box[item.state])


class Slider():
    instances = []
    cursor = (0, 0)
    selected = None
    def __init__(self, coords_x, coords_y, width, height, slider_width, \
                 continuous=True, span=[0, 5], marks_state=0, display_text=False, font=None, mark_width=2, mark_height=5, \
                 colour_1=(140, 140, 140), colour_2=(90, 90, 90), colour_3=(170, 170, 170), colour_text = (0, 0, 0), \
                 margin1=0, margin2=0):
        """
        :param colour_1: colour bar
        :param colour_2: colour slider
        :param colour_3: colour marks
        :param span: [min, max]
        :param marks_state: 0->no marks 1->bottom 2->top 3->top&bottom
        :param margin_1: gap between left border and min value
        :param margin_2: gap between top border and top of slider
        """
        self.x = coords_x
        self.y = coords_y
        self.width = width
        self.height = height
        self.slider_width = slider_width

        self.continuous = continuous
        self.span = span
        self.marks_state = marks_state
        self.display_text = display_text
        if display_text == True and not font:
            font = pygame.font.SysFont("Arial", 12)
        self.font = font
        self.mark_width = mark_width
        self.mark_height = mark_height

        self.colour_1 = colour_1
        self.colour_2 = colour_2
        self.colour_3 = colour_3
        self.colour_text = colour_text

        self.margin1 = margin1
        self.margin2 = margin2
        #self.margin3 = margin3
        #self.margin4 = margin4
        #self.margin5 = margin5

        self.index = 0
        self.value = 0
        self.slider_x = 0

        Slider.instances.append(self)


    @staticmethod
    def handle_press():
        Slider.selected = None
        Slider.cursor = pygame.mouse.get_pos()
        for item in Slider.instances:
            if item.x + item.slider_x < Slider.cursor[0] < item.x + item.slider_x + item.slider_width and item.y + item.margin2 < Slider.cursor[1] < item.y + item.height - item.margin2:
                # if slider
                Slider.selected = item
                #print("selected")

            if item.x < Slider.cursor[0] < item.x + item.width and item.y < Slider.cursor[1] < item.y + item.height:
                # if slider bar
                item.slider_x = Slider.cursor[0] - item.x - item.slider_width//2
                Slider.selected = item
                #print("selected")




    @staticmethod
    def handle_held():
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and Slider.selected is not None:
            Slider.selected.slider_x = pygame.mouse.get_pos()[0] - Slider.selected.x - (Slider.selected.slider_width) // 2
            #print(Slider.selected.slider_x)
            if Slider.selected.slider_x < 0:
                Slider.selected.slider_x = 0
            if Slider.selected.slider_x > Slider.selected.width - Slider.selected.slider_width:
                Slider.selected.slider_x = Slider.selected.width - Slider.selected.slider_width
            if not Slider.selected.continuous:
                val = (pygame.mouse.get_pos()[0]-Slider.selected.x)/Slider.selected.width
                Slider.selected.index = (val - (1 / (2 * (Slider.selected.span[1] - Slider.selected.span[0])))) // (
                            1 / (Slider.selected.span[1] - Slider.selected.span[0]))+1
                if Slider.selected.index < 0:
                    Slider.selected.index = 0
                if Slider.selected.index > Slider.selected.span[1]-Slider.selected.span[0]:
                    Slider.selected.index = Slider.selected.span[1]-Slider.selected.span[0]
                #print(Slider.selected.x + index*Slider.selected.width/(Slider.selected.span[1]-Slider.selected.span[0]))
                #print(index)
                Slider.selected.slider_x = Slider.selected.index*(Slider.selected.width-Slider.selected.slider_width)/(Slider.selected.span[1]-Slider.selected.span[0])
                #print(index)
        for item in Slider.instances:
            percent = (item.slider_x) / (item.width-item.slider_width)
            item.value = item.span[0] + percent * (item.span[1] - item.span[0])

            #print(pygame.mouse.get_pos())
            #print(Slider.cursor)


    @staticmethod
    def draw(win):
        for item in Slider.instances:
            if item.marks_state != 0:
                for i in range(item.continuous*2+(item.continuous^1)*(item.span[1]-item.span[0]+1)):
                    if item.continuous:
                        mark = pygame.Rect(item.x + (item.width-item.mark_width)*(i), item.y+item.height-(item.marks_state//2)*(item.height+item.mark_height), item.mark_width, item.mark_height+(item.mark_height+item.height)*(item.marks_state//3))
                    if not item.continuous:
                        mark = pygame.Rect(item.x + (item.width-item.mark_width)*(i/(item.span[1]-item.span[0]))//1, item.y+item.height-(item.marks_state//2)*(item.height+item.mark_height), item.mark_width, item.mark_height+(item.mark_height+item.height)*(item.marks_state//3))
                    pygame.draw.rect(win, item.colour_3, mark)
            line = pygame.Rect(item.x-item.margin1, item.y, item.width+2*item.margin1, item.height)
            pygame.draw.rect(win, item.colour_1, line)
            slider = pygame.Rect(item.x + item.slider_x, item.y + item.margin2, item.slider_width, item.height - 2 * item.margin2)
            pygame.draw.rect(win, item.colour_2, slider)

