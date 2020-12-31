from tkinter import *

class TkinterSetUp():

	def __init__(self):
		# basic Tkinter window setup
		self.root = Tk()
		self.root.title("Welcome to 3 Man Chess!")
		image = PhotoImage(file="images/bg1.png")
		w = image.width()
		h = image.height()
		self.root.geometry('%dx%d+0+0' % (w,h))
		self.frame = Frame(self.root)
		self.frame.pack()
		image_label = Label(self.frame, image=image)
		image_label.pack()
		image_label.image = image

		

		self.center_frame = Frame(self.frame)
		self.center_frame.place(in_=image_label)

		# instructions label creation and gridding
		self.instructions = Label(self.center_frame, text="Please Fill in the Game Options Below", font='Helvetica 18 bold')
		self.instructions.grid(row=0, column=1)

		# name and type labels
		Label(self.center_frame, text="Name", font='Helvetica 18 bold').grid(row=2,column=1)
		Label(self.center_frame, text="Type", font='Helvetica 18 bold').grid(row=2,column=2)
		
		# Player 1 info
		Label(self.center_frame, text="Player 1 (white)").grid(row=3,column=0)
		self.enter_player_one_name = Entry(self.center_frame)
		self.enter_player_one_name.grid(row=3,column=1)

		self.tk_player_one_type = StringVar()
		Radiobutton(self.center_frame, text="Human",variable=self.tk_player_one_type, value="human").grid(row=3,column=2)
		self.tk_player_one_type.set("human")

		# Player 2 info
		Label(self.center_frame, text="Player 2 (gray)").grid(row=4,column=0)
		self.enter_player_two_name = Entry(self.center_frame)
		self.enter_player_two_name.grid(row=4,column=1)

		self.tk_player_two_type = StringVar()
		Radiobutton(self.center_frame, text="Human",variable=self.tk_player_two_type, value="human").grid(row=4,column=2)
		self.tk_player_one_type.set("human")

		# Player 3 info
		Label(self.center_frame, text="Player 3 (black)").grid(row=5,column=0)
		self.enter_player_three_name = Entry(self.center_frame)
		self.enter_player_three_name.grid(row=5,column=1)

		self.tk_player_three_type = StringVar()
		Radiobutton(self.center_frame, text="Human",variable=self.tk_player_three_type, value="human").grid(row=5,column=2)
		self.tk_player_three_type.set("human")

		b = Button(self.center_frame, text="Start Game!", command=self.yuh)
		b.grid(row=6,column=1)
		

	def yuh(self):
		self.player_one_name = self.enter_player_one_name.get()
		self.player_one_color = 'w'

		self.player_two_name = self.enter_player_two_name.get()
		self.player_two_color = 'g'

		self.player_three_name = self.enter_player_three_name.get()
		self.player_three_color = 'b'

		self.frame.destroy()	
			
	def send_data(self):
		# wait for self.frame to be destroyed
		self.root.wait_window(self.frame)
		self.root.destroy()

		return [self.player_one_name, self.player_one_color, self.player_two_name, self.player_two_color, self.player_three_name, self.player_three_color]




if __name__ == "__main__":
	root = Tk()
	x = TkinterSetUp(root)
	root.mainloop()


