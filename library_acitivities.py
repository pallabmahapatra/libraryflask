import sqlite3

#from db_library_operations import display_all_tables

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


def create_table():
    conn.execute(' CREATE TABLE library_activities(library_activity_id int primary key, activity_type boolean, user_id int, library_book_id int,\
        checked_out_at datetime, checked_in_at datetime);')
    print("Table created successfully");

#create_table()


def insert_data():
    
    cursor.execute('''INSERT INTO library_activities(
        library_activity_id, activity_type, user_id,library_book_id, checked_out_at,checked_in_at) VALUES 
        (1,0,25,2003,'2014-10-23','2014-10-22' )''')
    conn.commit()

# insert_data()




def display_all_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("all the tables {}".format(cursor.fetchall()))

# display_all_tables()

def display():
    cursor.execute("select * from library_activities;")
    print("data from library_activities {}".format(cursor.fetchall()))

#display()




conn.close()