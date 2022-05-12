from pygame import *
import pygame
import random
from functions import *


init()

window = display.set_mode((300, 300))
screen = Surface((300, 300))

display.set_caption("Крестики-нолики")
display.set_icon(image.load("icon.png"))
screen.fill((255, 255, 255))

table = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
game_over = False
draw_grid(screen)
flag = True

turn = mixer.Sound("sounds/turn.wav")
win = mixer.Sound("sounds/win.wav")
lose = mixer.Sound("sounds/lose.wav")
draw = mixer.Sound("sounds/draw.wav")

while flag:
    for event in pygame.event.get():
        if event.type == QUIT:
            flag = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:

                window = display.set_mode((300, 300))
                screen = Surface((300, 300))

                display.set_caption("Крестики-нолики")
                screen.fill((255, 255, 255))

                table = [["", "", ""],
                         ["", "", ""],
                         ["", "", ""]]
                game_over = False

                draw_grid(screen)

        if event.type == MOUSEBUTTONDOWN and not game_over:
            pos = mouse.get_pos()
            if table[pos[1] // 100][pos[0] // 100] == "":
                table[pos[1] // 100][pos[0] // 100] = "x"
                player_win = get_win_check(table, "x")
                x, y = random.randint(0, 2), random.randint(0, 2)
                turn.play()
                if check_free(table) and not player_win:
                    while table[x][y] != "":
                        x, y = random.randint(0, 2), random.randint(0, 2)
                    table[x][y] = "0"

            ai_win = get_win_check(table, "0")
            if player_win or ai_win:
                game_over = True
                if player_win:
                    display.set_caption("Вы победили")
                    win.play()
                else:
                    display.set_caption("Компьютер победил")
                    lose.play()
            elif table[0].count("x") + table[0].count("0") + table[1].count("x") + \
                    table[1].count("0") + table[2].count("x") + table[2].count("0") == 9:
                game_over = True
                display.set_caption("Ничья")
                draw.play()

    draw_tic_tac_toe(screen, table)
    window.blit(screen, (0, 0))
    display.update()
