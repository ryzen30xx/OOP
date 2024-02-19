IDs = []
Books = []
Authors = ["Zen"]
Available_status = ["Available"]

def add_book(ID, Title, Author):
    if ID in IDs or Title in Books:
        print(f'The Book {Title} has been exist in the database!')
    else:
        IDs.append(ID)
        Books.append(Title)
        Authors.append(Author)
        Available_status.append('available')
        print(f'Book {Title} added successfully.')

def search_book(book_id):
    if book_id in IDs:
        index = IDs.index(book_id)
        print("ID: {book_id}\nTitle: {Books[index]}\nAuthor: {Authors[index]}\nAvailable Status: {Available_status[index]}")
    else:
        print("Book not found.")

def edit_book(book_id):
    if book_id in IDs:
        index = IDs.index(book_id)
        print("ID: {book_id}\nTitle: {Books[index]}\nAuthor: {Authors[index]}\nAvailable Status: {Available_status[index]}")

        new_title = input("Enter the new title: ")
        new_author = input("Enter the new author: ")
        new_status = input("Enter the new available status: ")

        Books[index] = new_title
        Authors[index] = new_author
        Available_status[index] = new_status

        print("Book details updated.")
    else:
        print("Book not found.")

def delete_book(book_id):
    if book_id in IDs:
        # for i in range(len(IDs)):
        # 	if book_id == IDs[i]:
        i = IDs.index(book_id)
	    del IDs[i]
	    del Books[i]
        del Authors[i]
        del Available_status[i]
        print("Book deleted successfully.")
	else:
        print("Book not found.")

def show_all():
    if not IDs:
        print("No books available.")
    else:
        print("\nAll Books:")
        for i in range(len(IDs)):
            print("ID: {IDs[i]}\nTitle: {Books[i]}\nAuthor: {Authors[i]}\nAvailable Status: {Available_status[i]}")

def borrow():
    

def Return():
    # Implement the Return function as needed
    pass

if __name__ == "__main__":
    while True:
        print("Welcome to Book Shop manager!")
        print("1. Add New Book\n2. Search Book\n3. Edit Book\n4. Delete Book\n5. Show All Book\n6. Borrow A Book\n7. Return A Book\n8. Quit Program\n")
        choose = int(input("Choose Your Function To Run Proccess: "))
        
        if not (1 <= choose <= 8):
            print("Wrong Input")
        elif choose == 1:
            add_book(int(input("Enter new ID for book: ")), input("Type a title of book: "), input("Enter Name of Author: "))
        elif choose == 2:
            search_book(int(input("Type ID's Book To Find: ")))
        elif choose == 3:
            edit_book(int(input("Type ID's Book To Modify: ")))
        elif choose == 4:
            delete_book()
        elif choose == 5:
            show_all()
        elif choose == 6:
            borrow()
        elif choose == 7:
            Return()
        elif choose == 8:
            print("Exiting the program. Goodbye!")
            quit("Goodbye")
