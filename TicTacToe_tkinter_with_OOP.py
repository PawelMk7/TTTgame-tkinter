from tkinter import *


class Window(Frame):

	def __init__(self, master=None, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self['height'] = 600
		self['width'] = 800
		self['bd'] = 10
		self['bg'] = '#ffffff'
		self.pack_propagate(0)
		self.pack()
		self.scores()
		b1 = Btn(self).grid(row=1,columnspan=2)

	def scores(self):

		F = Frame(bg='lightgreen')
		player_x_score = Label(self, text=f'Player X score:', bg='lightgreen').grid(row=0, column=0, padx=100, pady=5)
		player_o_score = Label(self, text=f'Player Y score:', bg='lightblue').grid(row=0, column=1, padx=100, pady=5)



class Btn(Button):
	def __init__(self, master, *args, **kwargs):
		Button.__init__(self, master, *args, **kwargs)
		self['width'] = 10
		self['height'] = 5


root = Tk()

f = Window(root)

root.mainloop()
