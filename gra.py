import os
import time
import random
import keyboard
import sys


WIDTH = 150
HEIGHT = 10


ball_x = WIDTH // 4
ball_y = HEIGHT // 2
paddle1_y = HEIGHT // 2 - 2
paddle2_y = HEIGHT // 2 - 2


ball_speed_x = -1
ball_speed_y = -1


score1 = 0
score2 = 0

#Płynność gry
def cursor(x,y):
    x = str(x)
    y = str(y)
    LINE_AT = '\033['+x+';'+y+'H'
    print(LINE_AT, end="")
    sys.stdout.flush()
    
#Rysowanie planszy oraz piłki
def draw_board():
    cursor(1,0)
    print(" " * (WIDTH - 5) + "PING PONG" )
    cursor(2, 0)
    print( " " * (WIDTH - 5) + "Score" )
    cursor(3, 0)
    print( " " * (WIDTH - 5) + f"Player 1: {score1}" )
    cursor(4, 0)
    print( " " * (WIDTH - 5) + f"Player 2: {score2}")
    cursor(5, 0)
    print( "+" + "-" * WIDTH + "+" )

    for row in range(HEIGHT):
        cursor(row+6,0)
        print("|",  end="")
        for col in range(WIDTH):
            if row in range(paddle1_y, paddle1_y + 2) and col == 1:
                print("##", end="")
            elif row in range(paddle2_y, paddle2_y + 2) and col == WIDTH - 2:
                cursor(row+6,WIDTH-2)
                print("##", end="")
            elif row == ball_y and col == ball_x:
                print("()", end="")
            else:
                print("  ", end="")
        cursor(row+6, WIDTH+2)
        print("|")
    print("+" + "-" * WIDTH + "+")

#Ruch paletek
def move_paddles():
    global paddle1_y, paddle2_y
    if keyboard.is_pressed('w') and paddle1_y > 0:
        paddle1_y -= 1
    if keyboard.is_pressed('s') and paddle1_y + 2 < HEIGHT:
        paddle1_y += 1
    if keyboard.is_pressed('i') and paddle2_y > 0:
        paddle2_y -= 1
    if keyboard.is_pressed('k') and paddle2_y + 2 < HEIGHT:
        paddle2_y += 1

#Główna funkcja gry
def play_pong():
    global ball_x, ball_y, paddle1_y, paddle2_y, ball_speed_x, ball_speed_y, score1, score2

    while True:
        
        move_paddles()
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        
        if ball_x <= 2 and paddle1_y <= ball_y < paddle1_y + 2: #Odbijanie lewej paletki
                ball_speed_x = 1
                
        elif ball_x >= WIDTH//2-5 and paddle2_y <= ball_y < paddle2_y + 2: #Odbijanie prawej paletki
                ball_speed_x = -1
                

        
        elif ball_y == 0 or ball_y == HEIGHT - 1: #Odbijanie od góry planszy
            ball_speed_y *= -1

        
        elif ball_x < 0: #Przejście piłki z lewej strony
            score2 += 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x = -1
            ball_speed_y = random.choice([-1, 1])
        elif ball_x >= WIDTH: #Przejście piłki z prawej strony
            score1 += 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x = -1
            ball_speed_y = random.choice([-1, 1])

        
        draw_board()

        
        if score1 == 10 or score2 == 10: #Ekran końcowy
            winner = "Player 1" if score1 == 10 else "Player 2"
            print("\n\033[1m" + "GAME OVER" + "\033[0m")
            print(f"\033[1m{winner} wins!\033[0m")
            break

        
        time.sleep(0.03)

 
play_pong()
