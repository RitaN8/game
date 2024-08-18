# welcome to the game tic tac toe -> the aim: take 4 cells in a row (or horizontal, or vertical, or diagonal) 
from time import sleep
from tkinter import *
from tkinter import font

# set megure of playing feald and other constants
MATRIX_WIDTH = 6
MATRIX_HEIGHT = 6
FIRST_PLAYER_COLOR = "red"
SECOND_PLAYER_COLOR = "green"
EMPTY_FIELD = "   "
game_buttons = []
current_player = FIRST_PLAYER_COLOR

# function reset all buttons
def reset_all_buttons():
    for next_row_buttons in game_buttons:
        for btn_reset in next_row_buttons:
            btn_reset.config(bg="SystemButtonFace")
            pass
    pass

# function checking game button
def check_game_out(smb):
    for r in range(MATRIX_HEIGHT):
        for c in range(MATRIX_WIDTH):
            if (game_buttons[r][c].config()['text'][4] == game_buttons[r][abs(c-1)].config()['text'][4] == game_buttons[r][abs(c-2)].config()['text'][4] == game_buttons[r][abs(c-3)].config()['text'][4] == EMPTY_FIELD
                and game_buttons[r][c].config()['background'][4] == game_buttons[r][(abs(c-1))].config()['background'][4] == game_buttons[r][(abs(c-2))].config()['background'][4] == game_buttons[r][(abs(c-4))].config()['background'][4] == smb)\
                or (game_buttons[r][c].config()['text'][4] == game_buttons[abs(r-1)][c].config()['text'][4] == game_buttons[abs(r-2)][c].config()['text'][4] == game_buttons[abs(r-3)][c].config()['text'][4] == EMPTY_FIELD
                    and game_buttons[r][c].config()['background'][4] == game_buttons[abs(r-1)][(c)].config()['background'][4] == game_buttons[abs(r-2)][(c)].config()['background'][4] == game_buttons[abs(r-3)][(c)].config()['background'][4] == smb)\
                or (game_buttons[r][c].config()['text'][4] == game_buttons[abs(r-1)][abs(c-1)].config()['text'][4] == game_buttons[abs(r-2)][abs(c-2)].config()['text'][4] == game_buttons[abs(r-3)][abs(c-3)].config()['text'][4] == EMPTY_FIELD
                    and game_buttons[r][c].config()['background'][4] == game_buttons[abs(r-1)][(abs(c-1))].config()['background'][4] == game_buttons[abs(r-2)][(abs(c-2))].config()['background'][4] == game_buttons[abs(r-3)][(abs(c-3))].config()['background'][4] == smb):
                print(f"Winner {current_player}")
                create_lbl()
                sleep(3)
                print("Game over")
                reset_all_buttons()
    pass

#function to change player
def next_game_moove(event):
    global current_player, current_button
    current_button = event.widget
    current_button.config(bg=current_player)
    if current_player == FIRST_PLAYER_COLOR:
        current_player = SECOND_PLAYER_COLOR
        check_game_out(current_player)

    else:
        current_player = FIRST_PLAYER_COLOR
        check_game_out(current_player)
    pass

# create tkinter window 
my_game = Tk()
for row in range(MATRIX_HEIGHT):
    next_row = []
    for col in range(MATRIX_WIDTH):
        init_text = EMPTY_FIELD
        btn = Button(text=init_text)
        btn.bind("<Button>", next_game_moove)
        next_row.append(btn)
        btn.grid(row=row, column=col, ipadx=30, ipady=30, padx=5, pady=5)
        pass
    game_buttons.append(next_row)
    pass
font1 = font.Font(family="Helvetica", size=14, weight="bold", slant="roman")
btn_reset = Button(text="Next game", bg="grey",
                   font=font1, command=reset_all_buttons)
btn_reset.grid(columnspan=MATRIX_WIDTH, padx=10, pady=10, sticky=(W, E))

# function to print result in Label
def create_lbl():
    lbl_reset = Label(
        text=f"Winner {current_player}", font=font1, bg=current_player)
    lbl_reset.grid(row=MATRIX_HEIGHT+2, columnspan=MATRIX_WIDTH,
                   padx=10, pady=10, sticky=(W, E))
    pass


my_game.mainloop()
