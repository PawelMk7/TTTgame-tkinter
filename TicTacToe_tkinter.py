from tkinter import *

root = Tk()
root.geometry("800x600")

def number(num):
	if num==1:
		b1.config(text='X')
	elif num==2:
		b2.config(text='O')

def buttons():
	"""
	Parameters: Function do not take any parameters.
	Returns: List of 9 buttons with grid positions.
	"""
	
	global button_list
	button_list = list()
	for rw in range(3):
		for col in range(3):
			button_list.append(Button(root, text=XO_assignment, height=20, width=20).grid(row=rw, column=col))




#b1 = Button(root, height=20, width=20, command=lambda: number(1))
#b1.grid(row=0, column=0)

#b2 = Button(root, height=20, width=20, command=lambda: number(2))
#b2.grid(row=0, column=1)


root.mainloop()