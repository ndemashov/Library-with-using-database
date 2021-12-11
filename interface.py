import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_create_db = tk.Button(toolbar, text='Create databse', command=self.create_db, bg='#d7d8e0', bd=0,
                                  compound=tk.TOP)
        btn_create_db.pack(side=tk.LEFT)

        btn_delete_db = tk.Button(toolbar, text='Delete databse', command=self.delete_db, bg='#d7d8e0', bd=0,
                                  compound=tk.TOP)
        btn_delete_db.pack(side=tk.LEFT)

        btn_ct = tk.Button(toolbar, text='Create table', command=self.create_table, bg='#d7d8e0', bd=0,
                                  compound=tk.TOP)
        btn_ct.pack(side=tk.LEFT)

        btn_connect = tk.Button(toolbar, text='Connect', command=self.connect, bg='#d7d8e0', bd=0,
                           compound=tk.TOP)
        btn_connect.pack(side=tk.LEFT)
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

    def add_db(self, name):
        self.db.create_db(name)

    def del_db(self, name):
        self.db.delete_db(name)

    def cr_tb(self, name, structure):
        self.db.create_table(name, structure)

    def conn(self, name):
        self.db.connect(name)

    def create_db(self):
        Create_db()

    def delete_db(self):
        Delete_db()

    def create_table(self):
        Create_table()

    def connect(self):
        Connect()


class Template(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_template()

    def init_template(self):
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        btn_close = ttk.Button(self, text='Close', command=self.destroy)
        btn_close.place(x=300, y=170)

        self.grab_set()
        self.focus_set()


class Create_db(Template):
    def __init__(self):
        super().__init__()
        self.init_create_db()
        self.view = app

    def init_create_db(self):
        self.title('Create database')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=50)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        btn_create = ttk.Button(self, text='Create')
        btn_create.place(x=220, y=170)
        btn_create.bind('<Button-1>', lambda event: self.view.add_db(
            self.entry_name.get()))


class Delete_db(Template):
    def __init__(self):
        super().__init__()
        self.init_delete_db()
        self.view = app

    def init_delete_db(self):
        self.title('Delete database')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=50)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        btn_delete = ttk.Button(self, text='Delete')
        btn_delete.place(x=220, y=170)
        btn_delete.bind('<Button-1>', lambda event: self.view.del_db(
            self.entry_name.get()))

class Create_table(Template):
    def __init__(self):
        super().__init__()
        self.init_create_table()
        self.view = app

    def init_create_table(self):
        self.title('Create table')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=20)
        label_structure = tk.Label(self, text='Structure:')
        label_structure.place(x=50, y=70)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=20)

        self.entry_structure = ttk.Entry(self)
        self.entry_structure.place(x=200, y=70)

        btn_ct = ttk.Button(self, text='Create button')
        btn_ct.place(x=220, y=170)
        btn_ct.bind('<Button-1>', lambda event: self.view.cr_tb(
            self.entry_name.get(), self.entry_structure.get(),))

class Connect(Template):
    def __init__(self):
        super().__init__()
        self.init_create_table()
        self.view = app

    def init_create_table(self):
        self.title('Create table')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=20)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=20)

        btn_connect = ttk.Button(self, text='Connect with db')
        btn_connect.place(x=220, y=170)
        btn_connect.bind('<Button-1>', lambda event: self.view.conn(
            self.entry_name.get()))

class DB:
    def __init__(self):
        self.con = psycopg2.connect(
            user="postgres",
            password="22001",
            host="127.0.0.1",
            port="5432"
        )
        self.cur = self.con.cursor()

    def create_db(self, name):
        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        query = "create database " + name + ";"
        self.cur.execute(query)
        print("Created")
        self.con.commit()

    def delete_db(self, name):
        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        query = "drop database " + name + ";"
        self.cur.execute(query)
        print("Deleted")
        self.con.commit()

    def connect(self, name):
        self.con = psycopg2.connect(
            user="postgres",
            database=name,
            password="22001",
            host="127.0.0.1",
            port="5432"
        )
        print("Connected")
        self.cur = self.con.cursor()

    def close(self):
        self.con.close()

    def create_table(self, name, structure):
        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        query = "create table " + name + "(" + str(structure) + ");"
        self.cur.execute(query)
        print("Table created")
        self.con.commit()

    def insert_data(self, description, costs, total):
        self.c.execute('''INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)''',
                       (description, costs, total))
        self.conn.commit()


if __name__ == "__main__":
    '''con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    sqlCreateDatabase = "create database Library;"
    cur.execute(sqlCreateDatabase)
    con.commit() '''
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Library")
    root.geometry("650x150+300+200")
    root.resizable(False, False)
    root.mainloop()
