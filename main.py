from flask import Flask, jsonify, request,render_template
import sqlite3, json

import books_operations as bkoperation
import library_books_operations as lb_operations


# from db_library_operations import display_all_tables
# conn = sqlite3.connect('database.db', check_same_thread=False)
# cursor = conn.cursor()

# creating a Flask app
app = Flask(__name__)


@app.route("/")
@app.route("/login")
def home():
    if request.method == 'GET':
        return render_template('/auth/login.html')
        

@app.route('/books/allbooks', methods = ['GET'])
def display_all_book():
    data = bkoperation.display_all_data()
    return jsonify(data)
    
# 3.a --> create a new book record
@app.route("/books/insertrecord", methods=['GET','POST'])
def insertrecord():
    if request.method == 'GET':
        return render_template('/library/library_books_insert.html')
    if request.method == 'POST':
        bookid = request.form.get("bookid")
        title = request.form.get("title")
        authorname = request.form.get("authorname")
        isbn = request.form.get("isbn")
        genre = request.form.get("genre")
        description = request.form.get("description")

        book_dict = {"bookid":bookid, "title":title,"authorname":authorname, "isbn":isbn,"genre":genre,\
            "description":description} 

        flag = bkoperation.insert_data_from_flask(data=book_dict)
        if flag == 1: writestatus = "data recored in the db."
        else: writestatus = "data not recored."
        book_dict.update(info = writestatus )

        return book_dict  # returning json format data back to webpage
    
# 3.b --> create library record
@app.route("/library/libraryrecord", methods=['GET','POST'])
def libraryrecord():
    if request.method == 'GET':
        return render_template('/library/library_books_insert.html')
    if request.method == 'POST':
        libray_book_id = int(request.form.get("librarybookid"))
        library_id = int(request.form.get("libraryid"))
        book_id = int(request.form.get("bookid"))
        llaid =int(request.form.get("llaid"))
        
        library_dict = {"library_book_id":libray_book_id, "library_id":library_id,"book_id":book_id, "llaid":llaid} 

        flag = lb_operations.insert_data_from_flask(data=library_dict)
        if flag == 1: writestatus = "data recored in the db."
        else: writestatus = "data not recored."
        library_dict.update(info = writestatus )

        return library_dict

# 3.c library book check out
@app.route("/library/bookcheckout", methods=['GET','POST'])
def library_book_checkout():
        if request.method == 'GET':
            return render_template('/library/librarybookcheckout.html')
        if request.method == 'POST':
            libray_book_id = int(request.form.get("librarybookid"))
            info_dict = {"library_book_id":libray_book_id}

            flag = lb_operations.checkout_library_book(data=info_dict)
            if flag:
                return {"operation status ": "book checked out"}
            if flag:
                return {"operation status": "book not check out"}

if __name__ == '__main__':
    app.run(host = '127.0.0.1',port=8000)