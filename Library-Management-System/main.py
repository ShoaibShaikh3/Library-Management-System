from library import Library

lib = Library()

while True:
    print("\n===== LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Register Student")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Transaction History")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        lib.add_book(input("Title: "), input("Author: "), int(input("Quantity: ")))

    elif choice == "2":
        lib.view_books()

    elif choice == "3":
        lib.search_book(input("Keyword: "))

    elif choice == "4":
        lib.delete_book(int(input("Book ID: ")))

    elif choice == "5":
        lib.register_student(input("Name: "), input("Course: "))

    elif choice == "6":
        lib.issue_book(int(input("Student ID: ")), int(input("Book ID: ")))

    elif choice == "7":
        lib.return_book(int(input("Issue ID: ")))

    elif choice == "8":
        lib.view_issued_books()

    elif choice == "9":
        break