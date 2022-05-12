from pygame.draw import *

colorX = (255, 0, 0)
color0 = (150, 255, 220)

def check_free(table):
    for i in table:
        for j in i:
            if j == '':
                return True
    return False


def draw_grid(scr):
    line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
    line(scr, (0, 0, 0), (0, 200), (300, 200), 3)


def draw_tic_tac_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "0":
                circle(scr, color0, (j * 100 + 50, i * 100 + 50), 45)
                circle(scr, (255, 255, 255), (j * 100 + 50, i * 100 + 50), 35)
            elif items[i][j] == "x":
                line(scr, colorX, (j * 100 + 10, i * 100 + 10), (j * 100 + 90, i * 100 + 90), 10)
                line(scr, colorX, (j * 100 + 90, i * 100 + 10), (j * 100 + 10, i * 100 + 90), 10)


def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fd[0][i] == fd[1][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True
    return flag_win
