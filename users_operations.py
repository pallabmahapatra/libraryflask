import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

def create_table():
    conn.execute(' CREATE TABLE users(users_id int primary key, name varchar);')
    print("Table created successfully");

#create_table()

def insert_data():
    
    cursor.execute('''INSERT INTO users(users_id, name ) VALUES 
        (1,"tui" )''')
    conn.commit()

#insert_data()




def display_all_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("all the tables {}".format(cursor.fetchall()))

#display_all_tables()

def display():
    cursor.execute("select * from users;")
    print("data from users table {}".format(cursor.fetchall()))

display()



conn.close()