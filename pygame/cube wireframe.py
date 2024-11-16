import pygame
import math
import numpy

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 60


pygame.display.set_caption("CUBE!!!11!1!!1!!1!!!!")
face_list = [[5, 6, 7], [4, 5, 6], [0, 1, 2], [1, 2, 3], [0, 4, 1], [1, 4, 5], [0, 2, 4], [2, 4, 6], [1, 3, 5], [3, 5, 7], [2, 3, 6], [3, 6, 7]]
point_list = numpy.array([[-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1], [-1, -1, 1], [1, -1, 1], [-1, 1, 1], [1, 1, 1]])
line_list = [[0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 3], [2, 6], [3, 7], [4, 5], [4, 6], [5, 7], [6, 7]]
angle = 1
rot_x_pos = numpy.array([[1, 0, 0], [0, 0.999847695, 0.0174524064], [0, -0.0174524064, 0.999847695]])
rot_x_neg = numpy.array([[1, 0, 0], [0, 0.999847695, -0.0174524064], [0, 0.0174524064, 0.999847695]])
rot_y_pos = numpy.array([[0.999847695, 0, 0.0174524064], [0, 1, 0], [-0.0174524064, 0, 0.999847695]])
rot_y_neg = numpy.array([[0.999847695, 0, -0.0174524064], [0, 1, 0], [0.0174524064, 0, 0.999847695]])
#  rot_z = numpy.array([[0.999847695, -0.0174524064, 0], [0.0174524064, 0.999847695, 0], [0, 0, 1]])
curr_rot = numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def draw_face(face_list, point_list):
    for face in face_list:
        pygame.draw.polygon(win, (100, 100, 100),
                            [(X / 2 + 100 * point_list[face[0]][0], Y / 2 + 100 * point_list[face[0]][1]),
                             (X / 2 + 100 * point_list[face[1]][0], Y / 2 + 100 * point_list[face[1]][1]),
                             (X / 2 + 100 * point_list[face[2]][0], Y / 2 + 100 * point_list[face[2]][1])])


def draw_points(point_list):
    for point in point_list:
        point = pygame.Rect(X / 2 + (point[0] * 100), Y / 2 + (point[1] * 100), 5, 5)
        pygame.draw.rect(win, (0, 0, 0), point)


def draw_line(line_list, point_list):
    for line in line_list:
        edge = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject1/otherfiles/rec.png")
        coords = (math.sqrt(math.pow((point_list[line[0]][0] - point_list[line[1]][0]), 2) + math.pow(
            (point_list[line[0]][1] - point_list[line[1]][1]), 2)) * 100, 5)
        edge = pygame.transform.scale(edge, coords)
        if (point_list[line[0]][0] - point_list[line[1]][0]) == 0:
            a = 90
        else:
            a = math.atan((point_list[line[0]][1] - point_list[line[1]][1]) / (
                        point_list[line[0]][0] - point_list[line[1]][0])) * 57.2957795
        edge = pygame.transform.rotate(edge, -a)
        if point_list[line[0]][1] > point_list[line[1]][1] and point_list[line[0]][0] > point_list[line[1]][0]:
            win.blit(edge, (X / 2 + point_list[line[0]][0] * 100 - edge.get_width() + 5,
                            Y / 2 + point_list[line[0]][1] * 100 - edge.get_height() + 5))
        if point_list[line[0]][1] > point_list[line[1]][1] and point_list[line[0]][0] <= point_list[line[1]][0]:
            win.blit(edge, (
            X / 2 + point_list[line[0]][0] * 100, Y / 2 + point_list[line[0]][1] * 100 - edge.get_height() + 5))
        if point_list[line[0]][1] <= point_list[line[1]][1] and point_list[line[0]][0] > point_list[line[1]][0]:
            win.blit(edge, (
            X / 2 + point_list[line[0]][0] * 100 - edge.get_width() + 5, Y / 2 + point_list[line[0]][1] * 100))
        if point_list[line[0]][1] <= point_list[line[1]][1] and point_list[line[0]][0] <= point_list[line[1]][0]:
            win.blit(edge, (X / 2 + point_list[line[0]][0] * 100, Y / 2 + point_list[line[0]][1] * 100))


def draw_win(point_list, line_list, face_list):
    win.fill((255, 255, 255))
    draw_face(face_list, point_list)
    #draw_line(line_list, point_list)
    draw_points(point_list)
    pygame.display.update()


def main(point_list, line_list, face_list, rot_x_pos, rot_x_neg, rot_y_pos, rot_y_neg, curr_rot):
    clock = pygame.time.Clock()
    while True:
        left = False
        right = False
        up = False
        down = False
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
        if pygame.key.get_pressed()[pygame.K_UP]:
            up = True
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            down = True
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            left = True
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            right = True

        if up:
            curr_rot = curr_rot.dot(rot_x_pos)
            point_list = point_list.dot(rot_x_pos)
        if down:
            curr_rot = curr_rot.dot(rot_x_neg)
            point_list = point_list.dot(rot_x_neg)
        if left:
            curr_rot = curr_rot.dot(rot_y_pos)
            point_list = point_list.dot(rot_y_pos)
        if right:
            curr_rot = curr_rot.dot(rot_y_neg)
            point_list = point_list.dot(rot_y_neg)

        draw_win(point_list, line_list, face_list)


main(point_list, line_list, face_list, rot_x_pos, rot_x_neg, rot_y_pos, rot_y_neg, curr_rot)
