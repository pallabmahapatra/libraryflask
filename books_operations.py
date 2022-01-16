import sqlite3
import json

conn = sqlite3.connect('database.db',check_same_thread=False)
cursor = conn.cursor()

def create_table():
    conn.execute(' CREATE TABLE books(book_id INTEGER PRIMARY KEY , title varchar,\
         author_name varchar, isbn_num varchar, genre varchar, descriptions text);')
    print("Table created successfully");

#create_table()

def insert_data():
    """
    insert data manually
    """
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO books(
    book_id,title, author_name, isbn_num, genre, descriptions) VALUES 
        (3, 'book_2','Mr.X_1', 'book002','zology','life_science')''')
    
    conn.commit()
    cursor.close()

def insert_data_from_flask(data):
    '''
    insert data from flask
    '''
    cursor = conn.cursor()
    query="INSERT INTO books(book_id,title, author_name, isbn_num, genre, descriptions) VALUES (?,?,?,?,?, ?);"
    val = [int(data['bookid']),data['title'], data['authorname'], data['isbn'],data['genre'], data['description']]
    
    flag = cursor.execute(query,val)
    conn.commit()
    cursor.close()
    if flag:
        return 1
    else: return 0

    

#insert_data()


def display_all_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("all the tables {}".format(cursor.fetchall()))
    cursor.close()
# display_all_tables()


def display_all_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("select * from books")
    columns = [description[0] for description in cursor.description]
    data = cursor.fetchall()
    data = list(zip(*data))

    result = dict(zip(columns,data))

    cursor.close()
    return [result]

#print(display_all_data())
    




