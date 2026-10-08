# library.py

class Library:
    def __init__(self):
        # Sample books dictionary: {book_id: {"title": title, "author": author, "status": "Available"}}
        self.books = {
            "101": {"title": "Python Programming", "author": "Guido van Rossum", "status": "Available"},
            "102": {"title": "Data Analytics Basics", "author": "Jil Sojitra", "status": "Available"}
        }

    def display_books(self):
        print("\n--- Available Books ---")
        for book_id, details in self.books.items():
            print(f"ID: {book_id} | Title: {details['title']} | Author: {details['author']} | Status: {details['status']}")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ").strip()
        if book_id in self.books:
            if self.books[book_id]["status"] == "Available":
                self.books[book_id]["status"] = "Issued"
                print(f"Success: Book '{self.books[book_id]['title']}' has been issued.")
            else:
                print("Sorry, this book is already issued.")
        else:
            print("Error: Invalid Book ID. Please try again.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ").strip()
        if book_id in self.books:
            if self.books[book_id]["status"] == "Issued":
                self.books[book_id]["status"] = "Available"
                print(f"Success: Book '{self.books[book_id]['title']}' has been returned.")
            else:
                print("This book was not marked as issued.")
        else:
            print("Error: Invalid Book ID.")

# main.py
from library import Library

def main():
    lib = Library()
    while True:
        print("\n===== LIBRARY AUTOMATION SYSTEM =====")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                lib.display_books()
            elif choice == 2:
                lib.issue_book()
            elif choice == 3:
                lib.return_book()
            elif choice == 4:
                print("Exiting system. Thank you!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter valid numeric digits.")

if __name__ == "__main__":
    main()