from tkinter import *
import pandas as pd
import os

def save_lesson_func(title, content, window_new):
    title_text = title.get()
    content_text = content.get("1.0", "end-1c")

    window_new.destroy()

    csv_file = 'lessons.csv'

    file_exists = os.path.isfile(csv_file)
    if file_exists:
        if os.stat(csv_file).st_size == 0:
            df = pd.DataFrame(columns=['Title', 'Content'])
            df.to_csv(csv_file, index=False, sep=';')
    else:
        df = pd.DataFrame(columns=['Title', 'Content'])
        df.to_csv(csv_file, index=False, sep=';')

    try:
        df = pd.read_csv(csv_file, sep=';')
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=['Title', 'Content'])

    df.loc[len(df.index)] = [title_text, content_text]
    df.to_csv(csv_file, index=False, sep=';')
    
    main()

def Memorize_lesson(window_main,content,title):
    window_main.destroy()
    window_new = Tk()
    window_new.geometry("1000x500")
    window_new.title("Super memorizer helper")
    window_new.config(background="#347deb")

    title_text = Label(window_new, text="Title:", bg="#347deb", fg="white", font=("VIMH.otf", 15, 'bold'), pady=3)
    title_entry = Entry(window_new, font=("Mothanna.ttf", 15), relief=RAISED, bd=7)

    content_text = Label(window_new, text="Content:", bg="#347deb", fg="white", font=("VIMH.otf", 15, 'bold'), pady=3)
    content_entry = Text(window_new, font=("Mothanna.ttf", 15), relief=RAISED, bd=7)

    save_button = Button(text="Save lesson", bg="#345beb", activebackground="#345beb", fg="white", 
                         activeforeground="white", font=("VIMH.otf", 12, 'bold'), padx=15, pady=10,
                         command=lambda: save_lesson_func(title_entry, content_entry, window_new))

    title_text.pack()
    title_entry.pack(fill="x", padx=10, pady=5)
    content_text.pack()
    content_entry.pack(fill="x", padx=10, pady=5)
    save_button.pack(fill="x", padx=10, pady=5)
    window_new.mainloop()


def new_lesson_func(window_main):
    window_main.destroy()
    window_new = Tk()
    window_new.geometry("1000x500")
    window_new.title("Super memorizer helper")
    window_new.config(background="#347deb")

    title_text = Label(window_new, text="Title:", bg="#347deb", fg="white", font=("VIMH.otf", 15, 'bold'), pady=3)
    title_entry = Entry(window_new, font=("Mothanna.ttf", 15), relief=RAISED, bd=7)

    content_text = Label(window_new, text="Content:", bg="#347deb", fg="white", font=("VIMH.otf", 15, 'bold'), pady=3)
    content_entry = Text(window_new, font=("Mothanna.ttf", 15), relief=RAISED, bd=7)

    save_button = Button(text="Save lesson", bg="#345beb", activebackground="#345beb", fg="white", 
                         activeforeground="white", font=("VIMH.otf", 12, 'bold'), padx=15, pady=10,
                         command=lambda: save_lesson_func(title_entry, content_entry, window_new))

    title_text.pack()
    title_entry.pack(fill="x", padx=10, pady=5)
    content_text.pack()
    content_entry.pack(fill="x", padx=10, pady=5)
    save_button.pack(fill="x", padx=10, pady=5)
    window_new.mainloop()

def display_titles(window):
    """Read all titles from the CSV file and display them as buttons."""
    csv_file = 'lessons.csv'
    if os.path.isfile(csv_file) and os.stat(csv_file).st_size > 0:
        try:
            df = pd.read_csv(csv_file, sep=';')
            for title in df['Title']:
                title_button = Button(window, text=title, bg="#4a90e2", fg="white", font=("Mothanna.ttf", 12, 'bold'),
                                      command=lambda t=title: read_lesson(df, t,window))
                title_button.pack(fill="x", padx=10, pady=2)
        except Exception as e:
            error_label = Label(window, text="Error reading titles.", bg="red", fg="white")
            error_label.pack(fill="x", padx=10, pady=2)
            print(f"Error: {e}")

def read_lesson(df, title, window):
    window.destroy()
    # Locate the row where the 'Title' column matches the specified title
    content = df.loc[df['Title'] == title, 'Content'].values
    # Check if content exists for that title
    if content.size > 0:
        lesson_content = content[0]  # Get the content for the title
        
        # Create a new window to display the lesson
        lesson_window = Tk()  # Create a new Tk instance
        lesson_window.geometry("700x450")  # Set the size of the window
        lesson_window.title(title)  # Set the title of the window
        lesson_window.config(background="#347deb")

        # Display the title
        title_label = Label(lesson_window, text=title, bg="#347deb", fg="white", 
                  font=("VIMH.otf", 20, 'bold'))
        title_label.pack()

        # Display the content
        content_label = Label(lesson_window, text=lesson_content, bg="#347deb", fg="white", 
                  font=("VIMH.otf", 20))
        content_label.pack()

        # Add a "Memorize" button
        memorize_button = Button(lesson_window, text="Memorize", bg="#4a90e2", fg="white", font=("Mothanna.ttf", 12, 'bold'),
                                 command=lambda: Memorize_lesson(lesson_window,content,title))  # Placeholder for memorize action
        memorize_button.pack(side="bottom", fill="x", padx=10, pady=10)

        # Start the new window's main loop
        lesson_window.mainloop()
    else:
        # Handle the case where the title is not found
        print(f"Title '{title}' not found.")




def main():
    window_main = Tk()
    window_main.geometry("450x600")
    window_main.title("Super memorizer helper")
    icon = PhotoImage(file="logo.png")
    window_main.iconphoto(True, icon)
    window_main.config(background="#347deb")

    label = Label(window_main, text="Super Memorizer Helper!", bg="#347deb", fg="white", 
                  font=("VIMH.otf", 20, 'bold'), pady=30)
    new_lesson_button = Button(text="Create New Lesson", bg="#345beb", activebackground="#345beb", fg="white", 
                               activeforeground="white", font=("VIMH.otf", 12, 'bold'), padx=50, relief=RAISED, 
                               bd=3, command=lambda: new_lesson_func(window_main))

    label.pack()
    new_lesson_button.pack(fill="x", padx=10, pady=5)

    # Call display_titles to show all titles from the CSV
    display_titles(window_main)

    window_main.mainloop()

if __name__ == '__main__':
    main()
