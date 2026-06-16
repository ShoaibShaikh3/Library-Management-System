from db import cursor, connection
from datetime import date

class Library:

    # ---------------- ADD BOOK ----------------
    def add_book(self, title, author, quantity):

        query = """
        INSERT INTO books (title, author, quantity)
        VALUES (%s,%s,%s)
        """

        values = (title, author, quantity)

        cursor.execute(query, values)
        connection.commit()

        print("Book Added Successfully")

    # ---------------- VIEW BOOKS ----------------
    def view_books(self):
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            print(row)

    # ---------------- SEARCH BOOK ----------------
    def search_book(self, keyword):
        query = "SELECT * FROM books WHERE title LIKE %s"
        cursor.execute(query, ('%' + keyword + '%',))
        for row in cursor.fetchall():
            print(row)

    # ---------------- DELETE BOOK ----------------
    def delete_book(self, book_id):
        cursor.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
        connection.commit()
        print("Book Deleted")