import json

# File to store the library data
LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    save_library(library)
    print("Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        query = input("Enter the title: ").lower()
        results = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        query = input("Enter the author: ").lower()
        results = [book for book in library if query in book["author"].lower()]
    else:
        print("Invalid choice.\n")
        return
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.\n")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return
    
    print("Your Library:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print()

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# Menu system
def main():
    library = load_library()
    while True:
        print("Menu:\n1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
