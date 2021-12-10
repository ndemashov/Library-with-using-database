import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_create_db = tk.Button(toolbar, text='Create databse', command=self.create_db, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_create_db.pack(side=tk.LEFT)

        btn_delete_db = tk.Button(toolbar, text='Delete databse', command=self.delete_db, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_delete_db.pack(side=tk.LEFT)

        '''
        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'),
                                 height=15, show='headings')
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("description", width=365, anchor=tk.CENTER)
        self.tree.column("costs", width=150, anchor=tk.CENTER)
        self.tree.column("total", width=100, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("description", text='Наименование')
        self.tree.heading("costs", text='Статья дохода/расхода')
        self.tree.heading("total", text='Сумма')

        self.tree.pack()
        '''

    def create_db(self):
        Create_db()

    def delete_db(self):
        Delete_db()

class Create_db(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_create_db()

    def init_create_db(self):
        self.title('Create database')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=50)
        label_structure = tk.Label(self, text='Structure:')
        label_structure.place(x=50, y=110)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        self.structure = ttk.Entry(self)
        self.structure.place(x=200, y=110)

        btn_close = ttk.Button(self, text='Close', command=self.destroy)
        btn_close.place(x=300, y=170)

        btn_create = ttk.Button(self, text='Create')
        btn_create.place(x=220, y=170)
        btn_create.bind('<Button-1>')

        self.grab_set()
        self.focus_set()

class Delete_db(Create_db):
    def __init__(self):
        super().__init__()
        self.init_delete_db()

    def init_delete_db(self):
        self.title('Delete database')

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        btn_delete = ttk.Button(self, text='Delete')
        btn_delete.place(x=220, y=170)
        btn_delete.bind('<Button-1>')

if __name__ == "__main__":

    con = psycopg2.connect( 
    user="postgres", 
    password="123", 
    host="127.0.0.1", 
    port="5432"
    )
    '''con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    sqlCreateDatabase = "create database Library;"
    cur.execute(sqlCreateDatabase)
    con.commit() '''

    
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Library")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
    
