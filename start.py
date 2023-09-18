import tkinter as tk
from tkinter import ttk
import editBook
from tkinter import messagebox
import mysql.connector


def books():
    global books_frame
    books_frame = ttk.Frame(notebook)
    books_frame.pack(pady=50)
    s=tk.Button(books_frame,text="Search",command=search,height=2,width=10)
    s.pack(pady=10)
    s1=tk.Button(books_frame,text="Show",command=show,height=2,width=10)
    s1.pack(pady=10)
    badd = tk.Button(books_frame, text="Add Book", command=addBook,height=3,width=10)
    bedit = tk.Button(books_frame, text="Update Book", command=editBook,height=3,width=10)
    bdelete = tk.Button(books_frame, text="Delete Book", command=deleteBook,height=3,width=10)
    badd.pack(side="left", padx=20)
    bedit.pack(side="left", padx=20)
    bdelete.pack(side="left", padx=20)
    notebook.add(books_frame,text="Books")
    notebook.select(books_frame)
    notebook.forget(main)


def search():
    search = ttk.Frame(notebook)
    search.pack(pady=50)
    def search_books():
        search_query = entry_search.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE bname LIKE %s OR authors LIKE %s"
            values = (f'%{search_query}%', f'%{search_query}%')

            cursor.execute(query, values)
            result = cursor.fetchall()

            if result:
                for row in result:
                    book_info = f"ID: {row[0]}, Name: {row[1]}, Authors: {row[3]}, Status: {row[4]}"
                    text_result.insert(tk.END, book_info + '\n')
            else:
                text_result.insert(tk.END, "No books found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()
            
    label_search = tk.Label(search, text="Search by Name or Author")
    label_search.pack()

    entry_search = tk.Entry(search)
    entry_search.pack()

    search_button = tk.Button(search, text="Search", command=search_books)
    search_button.pack()

    text_result = tk.Text(search, height=10, width=50)
    text_result.pack()

    notebook.add(search,text="Search Book")
    notebook.select(search)
    notebook.forget(books_frame)
    

def show():
    show = ttk.Frame(notebook)
    show.pack(pady=50)
    text_result = tk.Text(show, height=10, width=50)
    text_result.pack()
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='toor',
            database='library'
        )
        cursor = conn.cursor()

        query = "SELECT * FROM books"

        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                book_info = f"ID: {row[0]}, Name: {row[1]}, Author: {row[3]}, Status: {row[4]}"
                text_result.insert(tk.END, book_info + '\n')
        else:
            text_result.insert(tk.END, "No books found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        cursor.close()
        conn.close()
    
    notebook.add(show,text="Show Books List")
    notebook.select(show)
    notebook.forget(books_frame)


def issue():
    global issue_frame
    issue_frame = ttk.Frame(notebook)
    issue_frame.pack(pady=50)
    notebook.add(issue_frame,text="Issue/Return")
    issue_frame.pack(pady=50)
    bissue = tk.Button(issue_frame, text="Issue Book", command=show,height=5,width=10)
    breturn = tk.Button(issue_frame, text="Return Book", command=listMembers,height=5,width=10)
    bissue.pack(side="left", padx=20)
    breturn.pack(side="left", padx=20)
    notebook.add(issue_frame,text="Issue/Return")
    notebook.select(issue_frame)
    notebook.forget(main)

def addBook():
    add_book = ttk.Frame(notebook)
    add_book.pack(pady=50)

    def submit():
        title = entry_title.get()
        isbn = entry_isbn.get()
        authors = entry_authors.get()
        status = entry_status.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()
            query = "INSERT INTO books (bname,isbn,authors,status) VALUES (%s, %s, %s, %s)"
            values = (title,isbn,authors,status)

            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", "Book added successfully!")
            addBook.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()
        
    
    label_title = tk.Label(add_book, text="Book Title")
    label_title.pack()

    entry_title = tk.Entry(add_book)
    entry_title.pack()

    label_isbn = tk.Label(add_book, text="ISBN")
    label_isbn.pack()

    entry_isbn = tk.Entry(add_book)
    entry_isbn.pack()

    label_authors = tk.Label(add_book, text="Authors")
    label_authors.pack()

    entry_authors = tk.Entry(add_book)
    entry_authors.pack()

    label_status = tk.Label(add_book, text="Status")
    label_status.pack()

    entry_status = tk.Entry(add_book)
    entry_status.pack()

    submit_button = tk.Button(add_book, text="Submit", command=submit)
    submit_button.pack()

    
    notebook.add(add_book,text="Add Book")
    notebook.select(add_book)
    notebook.forget(books_frame)

def editBook():
    edit_book = ttk.Frame(notebook)
    edit_book.pack(pady=50)

    def submit():
        bid=entry_bid.get()
        title = entry_title.get()
        isbn = entry_isbn.get()
        authors = entry_authors.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()
            query = "UPDATE books SET bname = %s, authors = %s, isbn = %s WHERE bid = %s"
            values = (title, authors,isbn, bid)

            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", "Book details updated successfully!")
            editBook.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()
        

    label_bid = tk.Label(edit_book, text="Book ID")
    label_bid.pack()

    entry_bid = tk.Entry(edit_book)
    entry_bid.pack()

    label_title = tk.Label(edit_book, text="New Book Title")
    label_title.pack()

    entry_title = tk.Entry(edit_book)
    entry_title.pack()

    label_isbn = tk.Label(edit_book, text="New ISBN")
    label_isbn.pack()

    entry_isbn = tk.Entry(edit_book)
    entry_isbn.pack()

    label_authors = tk.Label(edit_book, text="New Authors")
    label_authors.pack()

    entry_authors = tk.Entry(edit_book)
    entry_authors.pack()

    submit_button = tk.Button(edit_book, text="Submit", command=submit)
    submit_button.pack()

    
    notebook.add(edit_book,text="Edit Book Details")
    notebook.select(edit_book)
    notebook.forget(books_frame)

def deleteBook():
    delete_book = ttk.Frame(notebook)
    delete_book.pack(pady=50)
    

    def submit():
        book_id = entry_id.get()
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()

            query = "DELETE FROM books WHERE bid = %s"
            values = (book_id,)

            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", "Book deleted successfully!")
            deleteBook.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    label_id = tk.Label(delete_book, text="Book ID")
    label_id.pack()

    entry_id = tk.Entry(delete_book)
    entry_id.pack()

    delete_button = tk.Button(delete_book, text="Delete", command=submit)
    delete_button.pack()

    
    notebook.add(delete_book,text="Delete Book")
    notebook.select(delete_book)
    notebook.forget(books_frame)



def members():
    global members_frame
    members_frame = ttk.Frame(notebook)
    members_frame.pack(pady=50)
    mlist = tk.Button(members_frame, text="List of Members", command=listMembers,height=2,width=20)
    mlist.pack()
    madd = tk.Button(members_frame, text="Add Member", command=addMember,height=2,width=20)
    medit = tk.Button(members_frame, text="Update Member", command=editMember,height=2,width=20)
    mdelete = tk.Button(members_frame, text="Delete Member", command=deleteMember,height=2,width=20)
    madd.pack()
    medit.pack()
    mdelete.pack()
    notebook.add(members_frame,text="Members")
    notebook.select(members_frame)
    notebook.forget(main)
    


def listMembers():
    member_list = ttk.Frame(notebook)
    member_list.pack(pady=50)
    text_result = tk.Text(member_list, height=50, width=50)
    text_result.pack()
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='toor',
            database='library'
        )
        cursor = conn.cursor()

        query = "SELECT * FROM members"

        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            for row in result:
                member_info = f"ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Email: {row[3]}"
                text_result.insert(tk.END, member_info + '\n')
        else:
            text_result.insert(tk.END, "No members found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        cursor.close()
        conn.close()
    
    notebook.add(member_list,text="List of Members")
    notebook.select(member_list)
    notebook.forget(members_frame)
  

def addMember():
    add_member = ttk.Frame(notebook)
    add_member.pack(pady=50)

    def submit():
        name = entry_name.get()
        contact = entry_contact.get()
        email = entry_email.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()

            query = "INSERT INTO members (mname, contact, email) VALUES (%s, %s, %s)"
            values = (name, contact, email)

            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", "Member added successfully!")
            addMember.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()
        
    label_name = tk.Label(add_member, text="Name")
    label_name.pack()

    entry_name = tk.Entry(add_member)
    entry_name.pack()

    label_contact = tk.Label(add_member, text="Contact")
    label_contact.pack()

    entry_contact = tk.Entry(add_member)
    entry_contact.pack()

    label_email = tk.Label(add_member, text="Email")
    label_email.pack()

    entry_email = tk.Entry(add_member)
    entry_email.pack()

    submit_button = tk.Button(add_member, text="Submit", command=submit)
    submit_button.pack()

    
    notebook.add(add_member,text="Add Member")
    notebook.select(add_member)
    notebook.forget(members_frame)

def editMember():
    edit_member = ttk.Frame(notebook)
    edit_member.pack(pady=50)

    def submit():
        mid = entry_id.get()
        name = entry_name.get()
        contact = entry_contact.get()
        email = entry_email.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()

            query = "UPDATE members SET mname = %s, contact = %s, email = %s WHERE mid = %s"
            values = (name, contact, email, mid)

            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Member information updated successfully!")
            editMember.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()
        

    label_id = tk.Label(edit_member, text="Member ID")
    label_id.pack()

    entry_id = tk.Entry(edit_member)
    entry_id.pack()
        
    label_name = tk.Label(edit_member, text="New Name")
    label_name.pack()

    entry_name = tk.Entry(edit_member)
    entry_name.pack()

    label_contact = tk.Label(edit_member, text="New Contact")
    label_contact.pack()

    entry_contact = tk.Entry(edit_member)
    entry_contact.pack()

    label_email = tk.Label(edit_member, text="New Email")
    label_email.pack()

    entry_email = tk.Entry(edit_member)
    entry_email.pack()

    submit_button = tk.Button(edit_member, text="Submit", command=submit)
    submit_button.pack()

    
    notebook.add(edit_member,text="Update Member Details")
    notebook.select(edit_member)
    notebook.forget(members_frame)

def deleteMember():
    delete_member = ttk.Frame(notebook)
    delete_member.pack(pady=50)
    

    def delete():
        mid = entry_id.get()
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()

            query = "DELETE FROM members WHERE mid = %s"
            values = (mid,)

            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", " Member deleted successfully!")
            deleteMember.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    label_id = tk.Label(delete_member, text="Member ID")
    label_id.pack()

    entry_id = tk.Entry(delete_member)
    entry_id.pack()

    delete_button = tk.Button(delete_member, text="Delete", command=delete)
    delete_button.pack()

    
    notebook.add(delete_member,text="Delete Member")
    notebook.select(delete_member)
    notebook.forget(members_frame)

def issueBook():
    issue_book = ttk.Frame(notebook)
    issue_book.pack(pady=50)

    def issue_book():
        member_id = entry_member_id.get()
        book_id = entry_book_id.get()

        try:
            conn = mysql.connector.connect(
                host='loaclhost',
                user='root',
                password='toor',
                database='library'
            )
            cursor = conn.cursor()

            member_query = "SELECT mid FROM members WHERE mid = %s"
            member_values = (member_id,)
            cursor.execute(member_query, member_values)
            member_result = cursor.fetchone()

        
            book_query = "SELECT bid, status FROM books WHERE bid = %s"
            book_values = (book_id,)
            cursor.execute(book_query, book_values)
            book_result = cursor.fetchone()

            if not member_result:
                messagebox.showerror("Error", "Member does not exist.")
            elif not book_result:
                messagebox.showerror("Error", "Book does not exist.")
            elif book_result[1] != 'Available':
                messagebox.showerror("Error", "Book is not available for borrowing.")
            else:
                rental_sum_query = "SELECT rental FROM rental WHERE member_id = %s"
                cursor.execute(rental_sum_query, (member_id,))
                rental_sum = cursor.fetchone()[0]

                if rental_sum is None:
                    rental_sum = 0

                if rental_sum + 50 > 500:
                    messagebox.showerror("Error", "Renting this book would exceed the limit of 500.")
                else:
                    update_book_query = "UPDATE books SET status = 'Issued' WHERE bid = %s"
                    cursor.execute(update_book_query, (book_id,))
                    
                    insert_issue_query = "INSERT INTO issues (member_id, book_id,issue_date) VALUES (%s, %s, %s)"
                    cursor.execute(insert_rental_query, (member_id, book_id,CURRENT_DATE))

                    if rental_sum==0:
                        insert_rental_query ="INSERT INTO rental (member_id,rental) VALUES (%s,%s)"
                        cursor.execute(insert_rental_query, (member_id,50))
                    else:
                        insert_rent_query="UPDATE rental SET rental=%s WHERE member_id = %s"
                        cursor.execute(insert_rent_query,(rental_sum+50,member_id))
                    conn.commit()
                    
                    messagebox.showinfo("Success", "Book issued successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()
        
    label_member_id = tk.Label(issue_book, text="Member ID")
    label_member_id.pack()

    entry_member_id = tk.Entry(issue_book)
    entry_member_id.pack()

    label_book_id = tk.Label(issue_book, text="Book ID")
    label_book_id.pack()

    entry_book_id = tk.Entry(issue_book)
    entry_book_id.pack()

    issue_button = tk.Button(issue_book, text="Issue Book", command=issue_book)
    issue_button.pack()

    
    notebook.add(issue_book,text="Issue Book")
    notebook.select(issue_book)
    notebook.forget(issue_frame)

def return_book(book_id):
    book_id = entry_book_id.get()
    
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='toor',
            database='library'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books WHERE bid = %s AND status = 'Issued'", (book_id,))
        book = cursor.fetchone()

        if book:
            cursor.execute("UPDATE books SET status = 'Available' WHERE id = %s", (book_id,))
            conn.commit()
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showinfo("Error", "Book not found or is already returned.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        cursor.close()
        conn.close()

    label_book_id = tk.Label(frame, text="Book ID")
    label_book_id.pack()

    entry_book_id = tk.Entry(frame)
    entry_book_id.pack()

main_window = tk.Tk()
main_window.title("Book Library")

notebook = ttk.Notebook(main_window)
notebook.pack()

books_frame=None
issue_frame=None
members_frame=None

main=ttk.Frame(notebook)
main.pack(pady=50)

button1 = tk.Button(main, text="Books", command=books,height=3,width=20)
button2 = tk.Button(main, text="Members", command=members,height=3,width=20)
button3 = tk.Button(main, text="Issue/Return", command=issue,height=3,width=20)

button1.pack()
button2.pack()
button3.pack()

notebook.add(main,text="Welcome")
notebook.select(main)

main_window.geometry("400x300")
main_window.mainloop()
