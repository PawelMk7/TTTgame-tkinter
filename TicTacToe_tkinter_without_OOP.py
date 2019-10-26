from tkinter import *
from tkinter import messagebox

winning_options = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
x_positions = list()
o_positions = list()
assign = 0
no_of_x_wins = 0
no_of_o_wins = 0
xo_assignment = ""


def field(num):
	'''
	Function takes one parametr: num. It is field's place on the gameboard.
	Function assigns X or O to the field and disables field for the current round. Selected field is added to the list
	of player's choices and checked against winning options.
	'''
	global assign, x_positions, o_positions

	if assign%2 == 0:
		x_positions.append(num)
		xo_assignment = 'X'
	else:
		o_positions.append(num)
		xo_assignment = 'O'

	assign += 1

	if num == 1:
		b1.config(text=xo_assignment, state=DISABLED)
	elif num == 2:
		b2.config(text=xo_assignment, state=DISABLED)
	elif num == 3:
		b3.config(text=xo_assignment, state=DISABLED)
	elif num == 4:
		b4.config(text=xo_assignment, state=DISABLED)
	elif num == 5:
		b5.config(text=xo_assignment, state=DISABLED)
	elif num == 6:
		b6.config(text=xo_assignment, state=DISABLED)
	elif num == 7:
		b7.config(text=xo_assignment, state=DISABLED)
	elif num == 8:
		b8.config(text=xo_assignment, state=DISABLED)
	elif num == 9:
		b9.config(text=xo_assignment, state=DISABLED)	

	winner_check()

def winner_check():
	'''
	Function is checking for the winner of the round. Assigns score for player X and Y after each round and resets
	gameboard after each round.
	'''
	global no_of_x_wins, no_of_o_wins, x_positions, o_positions

	if len(x_positions) >= 3 or len(o_positions) >= 3:
		for i in winning_options:
			if i[0] in x_positions and i[1] in x_positions and i[2] in x_positions:
				no_of_x_wins += 1
				players_score.config(text=f'Player X score: {no_of_x_wins}  VS  Player O score: {no_of_o_wins}')
				x_positions = []
				o_positions = []
				messagebox.showinfo('Result', "Player X has won!")
				b1.config(text="", state=NORMAL)
				b2.config(text="", state=NORMAL)
				b3.config(text="", state=NORMAL)
				b4.config(text="", state=NORMAL)
				b5.config(text="", state=NORMAL)
				b6.config(text="", state=NORMAL)
				b7.config(text="", state=NORMAL)
				b8.config(text="", state=NORMAL)
				b9.config(text="", state=NORMAL)			
			
			elif i[0] in o_positions and i[1] in o_positions and i[2] in o_positions:
				no_of_o_wins += 1
				players_score.config(text=f'Player X score: {no_of_x_wins}  VS  Player O score: {no_of_o_wins}')
				x_positions = []
				o_positions = []
				messagebox.showinfo('Result', "Player O has won!")
				b1.config(text="", state=NORMAL)
				b2.config(text="", state=NORMAL)
				b3.config(text="", state=NORMAL)
				b4.config(text="", state=NORMAL)
				b5.config(text="", state=NORMAL)
				b6.config(text="", state=NORMAL)
				b7.config(text="", state=NORMAL)
				b8.config(text="", state=NORMAL)
				b9.config(text="", state=NORMAL)				

			elif (len(x_positions) + len(o_positions)) == 9:
				x_positions = []
				o_positions = []
				messagebox.showinfo('Result', "Draw!")
				b1.config(text="", state=NORMAL)
				b2.config(text="", state=NORMAL)
				b3.config(text="", state=NORMAL)
				b4.config(text="", state=NORMAL)
				b5.config(text="", state=NORMAL)
				b6.config(text="", state=NORMAL)
				b7.config(text="", state=NORMAL)
				b8.config(text="", state=NORMAL)
				b9.config(text="", state=NORMAL)				


root = Tk()
root.geometry('445x500')
root.resizable(0,0)
root.title('PawelMk X/O game')

players_score = Label(root, text=f'Player X score: {no_of_x_wins}  VS  Player O score: {no_of_o_wins}', font='bold', bg='lightgreen')
players_score.grid(row=0, columnspan=3, sticky='EWNS')

b1 = Button(root, height=10, width=20, bd=1, command=lambda: field(1))
b2 = Button(root, height=10, width=20, bd=1, command=lambda: field(2))
b3 = Button(root, height=10, width=20, bd=1, command=lambda: field(3))
b4 = Button(root, height=10, width=20, bd=1, command=lambda: field(4))
b5 = Button(root, height=10, width=20, bd=1, command=lambda: field(5))
b6 = Button(root, height=10, width=20, bd=1, command=lambda: field(6))
b7 = Button(root, height=10, width=20, bd=1, command=lambda: field(7))
b8 = Button(root, height=10, width=20, bd=1, command=lambda: field(8))
b9 = Button(root, height=10, width=20, bd=1, command=lambda: field(9))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

root.mainloop()