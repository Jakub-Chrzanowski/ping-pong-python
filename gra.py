import os
import keyboard
WIDTH = 80
HEIGHT = 20

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
paddle1_y = HEIGHT // 2 - 2
paddle2_y = HEIGHT // 2 - 2

score1 = 0
score2 = 0
def draw_board():
    os.system("clear" if os.name == "posix" else "cls")
    print("\033[1m" + " " * (WIDTH + 6) + "PING PONG" + "\033[0m")
    print("\033[1m" + " " * (WIDTH + 2) + "Score" + "\033[0m")
    print("\033[1m" + " " * (WIDTH + 2) + f"Player 1: {score1}" + "\033[0m")
    print("\033[1m" + " " * (WIDTH + 2) + f"Player 2: {score2}" + "\033[0m")
    print("\033[1m" + "+" + "-" * WIDTH + "+" + "\033[0m")
    for row in range(HEIGHT):
        print("\033[1m" + "|" + "\033[0m", end="")
        for col in range(WIDTH):
            if row in range(paddle1_y, paddle1_y + 2) and col == 1:
                print("\033[1m" + "##" + "\033[0m", end="")
            elif row in range(paddle2_y, paddle2_y + 2) and col == WIDTH - 2:
                print("\033[1m" + "##" + "\033[0m", end="")
            elif row == ball_y and col == ball_x:
                print("\033[1m" + "()" + "\033[0m", end="")
            else:
                print("  ", end="")
        print("\033[1m" + "|" + "\033[0m")

    print("\033[1m" + "+" + "-" * WIDTH + "+" + "\033[0m")

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

def play_pong():
        
        move_paddles()
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        draw_board()
