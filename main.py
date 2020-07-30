import tkinter as tk
import tkinter.ttk
import datetime
import time
import sqlite3 as sql


class School():

    db_name = 'database\\students.db'

    def __init__(self, root):

        # -------------------APP TITLE--------------------------------------
        self.root = root
        self.root.title('Students data')

        # -------------------APP ICON--------------------------------------
        self.image = tk.PhotoImage(file='images\\icon.png')
        self.label = tk.Label(image=self.image)
        self.label.grid()

        # -------------------APP TITLE TEXT--------------------------------------
        self.label_title = tk.Label(text='School Management System',
                                    font=('Arial', 15, 'bold'),
                                    fg='blue')
        self.label_title.grid()

        # -------------------BLOC TEXT TITLE--------------------------------------
        frame = tk.LabelFrame(self.root, text='Student record:', pady=10)
        frame.grid(row=0, column=1)

        # -------------------FIRST NAME--------------------------------------
        tk.Label(frame, text='First name:').grid(row=1, column=1, sticky='W')
        self.firstname = tk.Entry(frame, width=20)
        self.firstname.grid(row=1, column=2)

        # -------------------LAST NAME--------------------------------------
        tk.Label(frame, text='Last name:').grid(row=2, column=1, sticky='W')
        self.lastname = tk.Entry(frame, width=20)
        self.lastname.grid(row=2, column=2)

        # -------------------USERNAME--------------------------------------
        tk.Label(frame, text='Username:').grid(row=3, column=1, sticky='W')
        self.username = tk.Entry(frame, width=20)
        self.username.grid(row=3, column=2)

        # -------------------EMAIL--------------------------------------
        tk.Label(frame, text='Email:').grid(row=4, column=1, sticky='W')
        self.email = tk.Entry(frame, width=20)
        self.email.grid(row=4, column=2)

        # -------------------SUBJECT--------------------------------------
        tk.Label(frame, text='Subject:').grid(row=5, column=1, sticky='W')
        self.subject = tk.Entry(frame, width=20)
        self.subject.grid(row=5, column=2)

        # -------------------AGE--------------------------------------
        tk.Label(frame, text='Age:').grid(row=6, column=1, sticky='W')
        self.age = tk.Entry(frame, width=20)
        self.age.grid(row=6, column=2)

        # -------------------SUBMIT BUTTON--------------------------------------
        tk.Button(frame, text='Add Record').grid(row=7, column=2)

        # -------------------DISPLAY MESSAGE--------------------------------------
        self.message = tk.Label(text='')
        self.message.grid(row=8, column=1)

        # -------------------DATA TABLE TREE BLOC DISPLAY--------------------------------------
        self.tree = tk.ttk.Treeview(height=10, column=['', '', '', '', '', ''])
        self.tree.grid(row=9, column=0, columnspan=3)

        self.tree.heading('#0', text='ID')
        self.tree.column('#0', width=50)

        self.tree.heading('#1', text='First name')
        self.tree.column('#1', width=100)

        self.tree.heading('#2', text='Last name')
        self.tree.column('#2', width=100)

        self.tree.heading('#3', text='Username')
        self.tree.column('#3', width=100)

        self.tree.heading('#4', text='Email')
        self.tree.column('#4', width=140)

        self.tree.heading('#5', text='Subject')
        self.tree.column('#5', width=100)

        self.tree.heading('#6', text='Age')
        self.tree.column('#6', width=50)

        # ------------------MENU BAR--------------------------------------
        menu = tk.Menu()
        item_menu = tk.Menu()

        item_menu.add_command(label='Add Record')
        item_menu.add_command(label='Edit Record')
        item_menu.add_command(label='Delete Record')
        item_menu.add_separator()
        item_menu.add_command(label='Help')
        item_menu.add_command(label='Exit')

        menu.add_cascade(label='File', menu=item_menu)
        menu.add_cascade(label='Add')
        menu.add_cascade(label='Edit')
        menu.add_cascade(label='Delete')
        menu.add_cascade(label='Help')
        menu.add_cascade(label='Exit')

        root.config(menu=menu)

        # ------------------VIEW RECORDS--------------------------------------
        self.show_records()

    def show_records(self):
        # show the databse records
        records = self.tree.get_children()

        for record in records:
            self.tree.delete(record)

        command = 'SELECT * FROM students'
        db_rows = self.connect_database(command)

        for db_row in db_rows:
            self.tree.insert('', 1000, text=db_row[0], values=db_row[1:])

    def connect_database(self, command):
        # connect db
        with sql.connect(self.db_name) as db:
            cursor = db.cursor()
            result = cursor.execute(command)
            db.commit()
        return result


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('700x700')

    app = School(root)
    root.mainloop()
