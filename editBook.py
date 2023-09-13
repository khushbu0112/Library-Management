import tkinter as tk
from tkinter import messagebox
import mysql.connector

def editBooks():
    books = tk.Tk()
    books.title("Edit Book")
    frame = tk.Frame(books)
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
            query = "UPDATE books SET title = %s, author = %s, isbn = %s WHERE id = %s"
            values = (new_title, new_author, new_isbn, book_id)

            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", "Book details updated successfully!")
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

    editBooks.geometry("400x300")
    editbooks.mainloop()

if __name__ == "__main__":
    print("This is executed when file2.py is run directly.")
