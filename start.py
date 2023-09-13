import tkinter as tk
import editBook
from tkinter import messagebox
import mysql.connector

def books():
    books = tk.Tk()
    books.title("Books")
    frame1 = tk.Frame(books)
    frame1.pack(pady=50)
    s=tk.Button(frame1,text="Search",command=search,height=2,width=10)
    s.pack(pady=10)
    s1=tk.Button(frame1,text="Show",command=show,height=2,width=10)
    s1.pack(pady=10)
    badd = tk.Button(frame1, text="Add Book", command=addBook,height=3,width=10)
    bedit = tk.Button(frame1, text="Update Book", command=editBook,height=3,width=10)
    bdelete = tk.Button(frame1, text="Delete Book", command=deleteBook,height=3,width=10)
    badd.pack(side="left", padx=20)
    bedit.pack(side="left", padx=20)
    bdelete.pack(side="left", padx=20)
    books.geometry("400x300")


def search():
    search = tk.Tk()
    search.title("Search Book")
    frame1 = tk.Frame(search)
    frame1.pack(pady=50)
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
            
    label_search = tk.Label(frame1, text="Search by Name or Author")
    label_search.pack()

    entry_search = tk.Entry(frame1)
    entry_search.pack()

    search_button = tk.Button(frame1, text="Search", command=search_books)
    search_button.pack()

    text_result = tk.Text(frame1, height=10, width=50)
    text_result.pack()

    search.geometry("400x300")
    search.mainloop()

def show():
    show = tk.Tk()
    show.title("List of Books")
    frame1 = tk.Frame(show)
    frame1.pack(pady=50)
    text_result = tk.Text(frame1, height=10, width=50)
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

    show.geometry("400x300")
    show.mainloop()


def issue():
    issue = tk.Tk()
    issue.title("Issue and Return")
    frame1 = tk.Frame(issue)
    frame1.pack(pady=50)
    bissue = tk.Button(frame1, text="Issue Book", command=issueBook,height=5,width=10)
    breturn = tk.Button(frame1, text="Return Book", command=deleteMember,height=5,width=10)
    bissue.pack(side="left", padx=20)
    breturn.pack(side="left", padx=20)
    issue.geometry("400x300")
    issue.mainloop()

def addBook():
    addBook = tk.Tk()
    addBook.title("Add a book")
    frame = tk.Frame(addBook)
    frame.pack(pady=50)

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
        
    
    label_title = tk.Label(frame, text="Book Title")
    label_title.pack()

    entry_title = tk.Entry(frame)
    entry_title.pack()

    label_isbn = tk.Label(frame, text="ISBN")
    label_isbn.pack()

    entry_isbn = tk.Entry(frame)
    entry_isbn.pack()

    label_authors = tk.Label(frame, text="Authors")
    label_authors.pack()

    entry_authors = tk.Entry(frame)
    entry_authors.pack()

    label_status = tk.Label(frame, text="Status")
    label_status.pack()

    entry_status = tk.Entry(frame)
    entry_status.pack()

    submit_button = tk.Button(frame, text="Submit", command=submit)
    submit_button.pack()

    addBook.geometry("400x300")
    addBook.mainloop()

def editBook():
    editBook = tk.Tk()
    editBook.title("Edit Book")
    frame = tk.Frame(editBook)
    frame.pack(pady=50)

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
        

    label_bid = tk.Label(frame, text="Book ID")
    label_bid.pack()

    entry_bid = tk.Entry(frame)
    entry_bid.pack()

    label_title = tk.Label(frame, text="New Book Title")
    label_title.pack()

    entry_title = tk.Entry(frame)
    entry_title.pack()

    label_isbn = tk.Label(frame, text="New ISBN")
    label_isbn.pack()

    entry_isbn = tk.Entry(frame)
    entry_isbn.pack()

    label_authors = tk.Label(frame, text="New Authors")
    label_authors.pack()

    entry_authors = tk.Entry(frame)
    entry_authors.pack()

    submit_button = tk.Button(frame, text="Submit", command=submit)
    submit_button.pack()

    editBook.geometry("400x300")
    editBook.mainloop()

def deleteBook():
    deleteBook = tk.Tk()
    deleteBook.title("Delete Book")
    frame = tk.Frame(deleteBook)
    frame.pack(pady=50)
    

    def delete_book():
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

    label_id = tk.Label(frame, text="Book ID")
    label_id.pack()

    entry_id = tk.Entry(frame)
    entry_id.pack()

    delete_button = tk.Button(frame, text="Delete", command=delete_book)
    delete_button.pack()

    deleteBook.geometry("400x300")
    deleteBook.mainloop()


def members():
    members = tk.Tk()
    members.title("Members")
    frame1 = tk.Frame(members)
    frame1.pack(pady=50)
    mlist = tk.Button(frame1, text="List of Members", command=listMembers,height=2,width=20)
    mlist.pack()
    madd = tk.Button(frame1, text="Add Member", command=addMember,height=2,width=20)
    medit = tk.Button(frame1, text="Update Member", command=editMember,height=2,width=20)
    mdelete = tk.Button(frame1, text="Delete Member", command=deleteMember,height=2,width=20)
    madd.pack()
    medit.pack()
    mdelete.pack()
    members.geometry("400x300")

def listMembers():
    lmembers = tk.Tk()
    lmembers.title("List of Members")
    frame1 = tk.Frame(lmembers)
    frame1.pack(pady=50)
    text_result = tk.Text(frame1, height=50, width=50)
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
    lmembers.geometry("400x300")
    lmembers.mainloop()
  

def addMember():
    addMember = tk.Tk()
    addMember.title("Add a member")
    frame = tk.Frame(addMember)
    frame.pack(pady=50)

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
        
    label_name = tk.Label(frame, text="Name")
    label_name.pack()

    entry_name = tk.Entry(frame)
    entry_name.pack()

    label_contact = tk.Label(frame, text="Contact")
    label_contact.pack()

    entry_contact = tk.Entry(frame)
    entry_contact.pack()

    label_email = tk.Label(frame, text="Email")
    label_email.pack()

    entry_email = tk.Entry(frame)
    entry_email.pack()

    submit_button = tk.Button(frame, text="Submit", command=submit)
    submit_button.pack()

    addMember.geometry("400x300")
    addMember.mainloop()

def editMember():
    editMember = tk.Tk()
    editMember.title("Edit member Information")
    frame = tk.Frame(editMember)
    frame.pack(pady=50)

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
        

    label_id = tk.Label(frame, text="Member ID")
    label_id.pack()

    entry_id = tk.Entry(frame)
    entry_id.pack()
        
    label_name = tk.Label(frame, text="New Name")
    label_name.pack()

    entry_name = tk.Entry(frame)
    entry_name.pack()

    label_contact = tk.Label(frame, text="New Contact")
    label_contact.pack()

    entry_contact = tk.Entry(frame)
    entry_contact.pack()

    label_email = tk.Label(frame, text="New Email")
    label_email.pack()

    entry_email = tk.Entry(frame)
    entry_email.pack()

    submit_button = tk.Button(frame, text="Submit", command=submit)
    submit_button.pack()

    editMember.geometry("400x300")
    editMember.mainloop()

def deleteMember():
    deleteMember = tk.Tk()
    deleteMember.title("Delete Member")
    frame = tk.Frame(deleteMember)
    frame.pack(pady=50)
    

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

    label_id = tk.Label(frame, text="Member ID")
    label_id.pack()

    entry_id = tk.Entry(frame)
    entry_id.pack()

    delete_button = tk.Button(frame, text="Delete", command=delete)
    delete_button.pack()

    deleteMember.geometry("400x300")
    deleteMember.mainloop()

def issueBook():
    issueBook = tk.Tk()
    issueBook.title("Edit member Information")
    frame = tk.Frame(issueBook)
    frame.pack(pady=50)

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
        
    label_member_id = tk.Label(frame, text="Member ID")
    label_member_id.pack()

    entry_member_id = tk.Entry(frame)
    entry_member_id.pack()

    label_book_id = tk.Label(frame, text="Book ID")
    label_book_id.pack()

    entry_book_id = tk.Entry(frame)
    entry_book_id.pack()

    issue_button = tk.Button(frame, text="Issue Book", command=issue_book)
    issue_button.pack()

    issueBook.geometry("400x300")
    issueBook.mainloop()

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
main_window.title("Main Page")


frame = tk.Frame(main_window)
frame.pack(pady=50)

button1 = tk.Button(frame, text="Books", command=books,height=3,width=20)
button2 = tk.Button(frame, text="Members", command=members,height=3,width=20)
button3 = tk.Button(frame, text="Issue/Return", command=issue,height=3,width=20)

button1.pack()
button2.pack()
button3.pack()

main_window.geometry("400x300")
main_window.mainloop()

