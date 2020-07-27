import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import datetime
import time
import sqlite3


class School():

    db_name = 'database\\students.db'

    def __init__(self, root):
        # title
        self.root = root
        self.root.title('Students data')

        #image
        self.image = tk.PhotoImage(file='images\\icon.png')
        self.label = tk.Label(image=self.image)
        self.label.grid()

        #title font
        self.label_title = tk.Label(text='School Management System',
                                    font=('Arial', 15, 'bold'),
                                    fg='blue')
        self.label_title.grid()


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('500x500')

    app = School(root)
    root.mainloop()
