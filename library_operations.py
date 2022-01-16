import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# print ("Opened database successfully");

# conn.execute(' CREATE TABLE libraries(library_id INTEGER PRIMARY KEY , name VARCHAR, city VARCHAR,state VARCHAR,postal_code VARCHAR);')
# print ("Table created successfully");

#conn.execute('INSERT INTO libraries (library_id, name, city, state, postal_code) VALUES (1, "tui","mumbai", "maharastra", "400001");')

def create_table():
    conn.execute(' CREATE TABLE libraries(library_id INTEGER PRIMARY KEY , name VARCHAR, city VARCHAR,state VARCHAR,postal_code VARCHAR);')
    print ("Table created successfully");


def insert_libraries():

    cursor.execute('''INSERT INTO libraries(
        library_id,name, city, state, postal_code) VALUES 
        (1, 'Sharma','mumbai', 'maha','40001')''')
    conn.commit()



def display_all_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("all the tables {}".format(cursor.fetchall()))


def display_libraries():
    cursor.execute("select * from libraries;")
    print(cursor.fetchall())

display_all_tables()

conn.close()