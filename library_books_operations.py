import sqlite3
#from sqlite3.dbapi2 import Cursor


conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# create table


def create_table():
    conn.execute(' CREATE TABLE library_books(library_book_id int primary key, library_id int, book_id int,\
        last_library_activity_id int);')
    print("Table created successfully");

   
#create_table()

# display all tables

# display_all_tables()

def display_all_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("all the tables {}".format(cursor.fetchall()))
    
#display_all_tables()


# insert into table

def insert_data():
    
    cursor.execute('''INSERT INTO library_books(
        library_book_id, library_id, book_id, last_library_activity_id)\
         VALUES(1,01,2003,0 )''')
    conn.commit()
    
#insert_data()


# display data from table

def display():
    cursor.execute("select * from library_books;")
    print("data from library_books {}".format(cursor.fetchall()))
    

#display()

def insert_data_from_flask(data):
    '''
    insert data from flask
    '''
    cursor = conn.cursor()
    query="INSERT INTO library_books(library_book_id,library_id, book_id, last_library_activity_id) VALUES (?,?,?,?);"
    val = data['library_book_id'],data['library_id'], data['book_id'], data['llaid']
    
    flag = cursor.execute(query,val)
    conn.commit()
    cursor.close()
    if flag:
        return 1
    else: return 0


def checkout_library_book(data):
    
    cursor = conn.cursor()
    library_book_id = [int(data['library_book_id'])]

    query = "delete from library_books where library_book_id=?;"
    flag = cursor.execute(query,library_book_id)

    conn.commit()
    cursor.close()
    if flag:
        return 1
    else: return 0

