from tkinter import *
import pandas as pd


def save_lesson_func(title,content,window_new):

	window_new.destroy()

	df = pd.read_csv('lessons.csv')
	df.loc[len(df.index)] = [title, content] 
	df.to_csv('lessons.csv')

	main()

def new_lesson_func(window_main):
	window_main.destroy()
	window_new = Tk()
	window_new.geometry("1000x500")
	window_new.title("Super memorizer helper")
	window_new.config(background="#347deb")

	title_text = Label(window_new,
		text="Title:",
		bg="#347deb",
		fg= "white",
		font=("VIMH.otf",15,'bold'),
		pady=3)

	title_entry = Entry(window_new,
		font=("Mothanna.ttf",15),
		relief=RAISED,
		bd=7)

	content_text = Label(window_new,
		text="Content:",
		bg="#347deb",
		fg= "white",
		font=("VIMH.otf",15,'bold'),
		pady=3)

	content_entry = Text(window_new,
		font=("Mothanna.ttf",15),
		relief=RAISED,
		bd=7,)

	save_button = Button(text="Save lesson",
		bg="#345beb",
		activebackground="#345beb",
		fg= "white",
		activeforeground="white",
		font=("VIMH.otf",12,'bold'),
		padx=15,
		pady=10,
		command=lambda: save_lesson_func(title_entry,content_entry,window_new))

	save_button.pack(fill="x",padx=10,pady=5)
	title_text.pack()
	title_entry.pack(fill="x",padx=10,pady=5)
	content_text.pack()
	content_entry.pack(fill="x",padx=10,pady=5)
	window_new.mainloop()


def read_lesson_func():
	pass

def main():
	window_main = Tk()
	window_main.geometry("450x600")
	window_main.title("Super memorizer helper")
	icon = PhotoImage(file="logo.png")
	window_main.iconphoto(True,icon)
	window_main.config(background="#347deb")
	
	label = Label(window_main,
		text="Super Memorizer Helper!",
		bg="#347deb",
		fg= "white",
		font=("VIMH.otf",20,'bold'),
		pady=30)
	
	new_lesson_button = Button(text="Create New Lesson",
		bg="#345beb",
		activebackground="#345beb",
		fg= "white",
		activeforeground="white",
		font=("VIMH.otf",12,'bold'),
		padx=50,
		relief=RAISED,
		bd=3,
		command=lambda: new_lesson_func(window_main))
	
	to_pack_list= [label,new_lesson_button]

	label.pack()
	new_lesson_button.pack(fill="x",padx=10,pady=5)
	
	
	window_main.mainloop()

if __name__ == '__main__':
	main()