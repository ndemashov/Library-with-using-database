import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd
import pandas.io.sql as psql


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_create_db = tk.Button(toolbar, text='Create databse', command=self.create_db, bg='#d7d8e0', bd=3,
                                  compound=tk.TOP)
        btn_create_db.pack(side=tk.LEFT)

        btn_delete_db = tk.Button(toolbar, text='Delete databse', command=self.delete_db, bg='#d7d8e0', bd=3,
                                  compound=tk.TOP)
        btn_delete_db.pack(side=tk.LEFT)

        btn_connect = tk.Button(toolbar, text='Connect', command=self.connect, bg='#d7d8e0', bd=3,
                                compound=tk.TOP)
        btn_connect.pack(side=tk.LEFT)

        btn_clt = tk.Button(toolbar, text='Create library tables', command=self.create_tables, bg='#d7d8e0', bd=3,
                                  compound=tk.TOP)
        btn_clt.pack(side=tk.LEFT)

        btn_at = tk.Button(toolbar, text='Add table', command=self.add_table, bg='#d7d8e0',
                           bd=3,
                           compound=tk.TOP)
        btn_at.pack(side=tk.LEFT)

        btn_add_book = tk.Button(toolbar, text='Add book', command=self.add_book, bg='#d7d8e0', bd=3,
                                  compound=tk.TOP)
        btn_add_book.pack(side=tk.LEFT)

        btn_add_reader = tk.Button(toolbar, text='Add reader', command=self.add_reader, bg='#d7d8e0', bd=3,
                                 compound=tk.TOP)
        btn_add_reader.pack(side=tk.LEFT)

        btn_add_export = tk.Button(toolbar, text='Add export', command=self.add_export, bg='#d7d8e0', bd=3,
                                   compound=tk.TOP)
        btn_add_export.pack(side=tk.LEFT)

        btn_print_tb = tk.Button(toolbar, text='Print table', command=self.print_table, bg='#d7d8e0', bd=3,
                           compound=tk.TOP)
        btn_print_tb.pack(side=tk.LEFT)


    def create_tables(self):
        self.db.create_table()
        
    def create_db(self):
        Create_db()

    def delete_db(self):
        Delete_db()

    def add_table(self):
        Add_table()

    def connect(self):
        Connect()

    def add_book(self):
        Add_book()

    def add_reader(self):
        Add_reader()

    def add_export(self):
        Add_export()

    def print_table(self):
        Print_table()

class Template(tk.Toplevel):
     def __init__(self):
        super().__init__(root)
        self.init_template()
        self.db = db
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
        
    def init_create_db(self):
        self.title('Create database')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=50)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        btn_create = ttk.Button(self, text='Create')
        btn_create.place(x=220, y=170)
        btn_create.bind('<Button-1>', lambda event: self.add_db(
            self.entry_name.get()))
        
    def add_db(self, name):
        self.db.create_db(name)

class Delete_db(Template):
    def __init__(self):
        super().__init__()
        self.init_delete_db()

    def init_delete_db(self):
        self.title('Delete database')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=50)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        btn_delete = ttk.Button(self, text='Delete')
        btn_delete.place(x=220, y=170)
        btn_delete.bind('<Button-1>', lambda event: self.del_db(
            self.entry_name.get()))
    def del_db(self, name):
        self.db.delete_db(name)

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

        btn_connect = ttk.Button(self, text='Connect')
        btn_connect.place(x=220, y=170)
        btn_connect.bind('<Button-1>', lambda event: self.connect(
            self.entry_name.get()))
        
    def connect(self, name):
        self.db.connect(name)

class Add_table(Template):
    def __init__(self):
        super().__init__()
        self.init_add_table()

    def init_add_table(self):
        self.title('Add table')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=20)
        label_structure = tk.Label(self, text='Structure')
        label_structure.place(x=50, y=70)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=20)

        self.entry_structure = ttk.Entry(self)
        self.entry_structure.place(x=200, y=70)

        btn_ct = ttk.Button(self, text='Add')
        btn_ct.place(x=220, y=170)
        btn_ct.bind('<Button-1>', lambda event: self.add_tb(
            self.entry_name.get(), self.entry_structure.get(), ))

    def add_tb(self, name, structure):
        self.db.add_table(name, structure)

class Add_book(Template):
    def __init__(self):
        super().__init__()
        self.init_add_book()
        self.view = app

    def init_add_book(self):
        self.title('Add book')
        label_title = tk.Label(self, text='Title:')
        label_title.place(x=50, y=20)

        label_writing_year = tk.Label(self, text='Writing year:')
        label_writing_year.place(x=50, y=45)

        label_author_name = tk.Label(self, text='Author Surname:')
        label_author_name.place(x=50, y=70)

        label_author_surname = tk.Label(self, text='Author name:')
        label_author_surname.place(x=50, y=95)

        label_num_book = tk.Label(self, text='Author patronymic')
        label_num_book.place(x=50, y=120)


        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=200, y=20)

        self.entry_writing_year = ttk.Entry(self)
        self.entry_writing_year.place(x=200, y=45)

        self.entry_author_surname = ttk.Entry(self)
        self.entry_author_surname.place(x=200, y=70)

        self.entry_author_name = ttk.Entry(self)
        self.entry_author_name.place(x=200, y=95)

        self.entry_author_patronymic = ttk.Entry(self)
        self.entry_author_patronymic.place(x=200, y=120)

        btn_ct = ttk.Button(self, text='Add book')
        btn_ct.place(x=220, y=170)
        btn_ct.bind('<Button-1>', lambda event: self.add_b(
        self.entry_title.get(), self.entry_writing_year.get(),
        self.entry_author_name.get(), self.entry_author_surname.get(),
        self.entry_author_patronymic.get(), ))

    def add_b(self, title, writing_year, author_name, author_surname, author_patronymic):
        self.db.query_add_book(title, writing_year, author_name, author_surname, author_patronymic)

class Add_reader(Template):
    def __init__(self):
        super().__init__()
        self.init_add_reader()
        self.view = app

    def init_add_reader(self):
        self.title('Add reader')
        label_title = tk.Label(self, text='Surname:')
        label_title.place(x=50, y=20)

        label_writing_year = tk.Label(self, text='Name:')
        label_writing_year.place(x=50, y=45)

        label_author_name = tk.Label(self, text='Patronymic:')
        label_author_name.place(x=50, y=70)

        label_author_surname = tk.Label(self, text='Phone:')
        label_author_surname.place(x=50, y=95)

        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=200, y=20)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=45)

        self.entry_patronymic = ttk.Entry(self)
        self.entry_patronymic.place(x=200, y=70)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=200, y=95)

        btn_ct = ttk.Button(self, text='Add reader')
        btn_ct.place(x=220, y=170)
        btn_ct.bind('<Button-1>', lambda event: self.add_r(
        self.entry_surname.get(), self.entry_name.get(),
        self.entry_patronymic.get(), self.entry_phone.get(), ))

    def add_r(self, surname, name, patronymic, phone):
        self.db.query_add_reader(surname, name, patronymic, phone)

class Add_export(Template):
    def __init__(self):
        super().__init__()
        self.init_add_export()
        self.view = app

    def init_add_export(self):
        self.title('Add export')
        label_title = tk.Label(self, text='Date:')
        label_title.place(x=50, y=20)

        label_writing_year = tk.Label(self, text='Reader ID:')
        label_writing_year.place(x=50, y=45)

        label_author_name = tk.Label(self, text='Book ID:')
        label_author_name.place(x=50, y=70)

        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=200, y=20)

        self.entry_reader_id = ttk.Entry(self)
        self.entry_reader_id.place(x=200, y=45)

        self.entry_book_id = ttk.Entry(self)
        self.entry_book_id.place(x=200, y=70)

        btn_ct = ttk.Button(self, text='Add export')
        btn_ct.place(x=220, y=170)
        btn_ct.bind('<Button-1>', lambda event: self.add_e(
            self.entry_date.get(), self.entry_reader_id.get(),
            self.entry_book_id.get(), ))

    def add_e(self, date, reader_id, book_id):
        self.db.query_add_export(date, reader_id, book_id)

class Print_table(Template):
    def __init__(self):
        super().__init__()
        self.init_print_table()

    def init_print_table(self):
        self.title('Print table')

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=50, y=20)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=100, y=20)

        btn_connect = ttk.Button(self, text='Print')
        btn_connect.place(x=220, y=170)
        btn_connect.bind('<Button-1>', lambda event: self.print_table(
            self.entry_name.get()))

    def print_table(self, name):
        self.db.print_table(name)

class DB:
    def __init__(self):
        self.con = psycopg2.connect(
            user="postgres",
            password="12345",
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
            password="12345",
            host="127.0.0.1",
            port="5432"
        )
        print("Connected")
        self.cur = self.con.cursor()

    def close(self):
        self.con.close()

    def create_table(self):
        try:
            self.cur.execute("CALL create_tables();")
            print("CREATED!")
            self.con.commit()
        except:
            print("Tables are created yet")

    def add_table(self, name, structure):
        try:
            self.cur.execute('CALL add_table(%s, %s);', (name, structure))
            print("TABLE ADDED!")
            self.con.commit()
        except:
            print("TABLE IS CREATED YET!")
        
    def query_add_book(self, title, writing_year, author_surname, author_name, author_patronymic):
        self.cur.execute('CALL add_book(%s, %s, %s, %s, %s);', (title, writing_year, author_surname, author_name, author_patronymic) )
        print("BOOK ADDED!")
        self.con.commit()
        
    def print_table(self, name):
        try:
            if(name == 'author'):
                table= psql.read_sql("SELECT * FROM print_author()", self.con)
            elif(name == 'book'):
                table= psql.read_sql("SELECT * FROM print_book()", self.con)
            elif(name == 'reader'):
                table= psql.read_sql("SELECT * FROM print_reader()", self.con)
            elif(name == 'export'):
                table= psql.read_sql("SELECT * FROM print_export()", self.con)
            print(table)
        except:
            print("There is no table " + name)


    def query_add_reader(self, surname, name, patronymic, phone):
        self.cur.execute('CALL add_reader(%s, %s, %s, %s);',
                         (surname, name, patronymic, phone))
        print("READER ADDED!")
        self.con.commit()

    def query_add_export(self, date, reader_id, book_id):
        try:
            self.cur.execute('CALL add_export(%s, %s, %s);',
                             (date, reader_id, book_id))
            print("EXPORT ADDED!")
            self.con.commit()
        except:
            print("INVALID USER OR BOOK ID!")
        finally:
            print("Go in Library again")

    def query_print_tb(self, name):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Library")
    root.geometry("1050x150+300+200")
    root.resizable(False, False)
    root.mainloop()
