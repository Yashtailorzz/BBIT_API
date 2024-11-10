class Book:
    def __init__(self, title, author, is_borrowed=False):
#is borrowed is false because an newly added book isnt borrowed before        
        self.title= title
        self.author= author
        self.is_borrowed= is_borrowed 
    def mark_as_borrowed(self):
        
        if not self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def mark_as_returned(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False


class LibraryMember:
         def __init__(self, name, member_id, borrowed_books=[]):
              self.name= name
              self.member_id= member_id
              self.borrowed_books= borrowed_books

         def borrow_a_book(self, book):
              if book.mark_as_borrowed():
                    self.borrowed_books.append(book)
                    print(f"{self.name} borrowed '{book.title}'.")
              else:
                   print(f"{book.title} is not available for borrowing.")

         def return_a_book(self):
              if book in self.borrowed_books and book.mark_as_returned():
                   self.borrowed_books.remove(book)
                   print(f"{self.name} returned '{book.title}'.")
              else:
                   print(f"{book.title} is not borrowed by {self.name}.")
              
         def List_of_borrowed_books(self, books):
              if self.borrowed_books:
                   print(f"{self.name} has borrowed the following books:")
                   for book in self.borrowed_books:
                        print(f" - {book.title} by {book.author}")
              else:
                   print(f"{self.name} has not borrowed any books.")
    
#creating a instance
def main():
#adding books
   books = [
      Book("the 48 laws of power", "Robert Greene"),
      Book("Atomic Habits", "James Clear"),
      Book("The 7 Habits of Highly Effective People", "Stephen Covey"),
 ]
#creating a library membe
member = LibraryMember("Yash Tailor", "169168")
while True:
     print("\nLibrary Menu:")
     print("1. View Books")
     print("2. Borrow a Book")
     print("3. Return Book")
     print("4. List Borrowed Books")
     print("5. Exit")
     
     choice = input("Choose an option: ")

     if choice == "1":
        for i, book in enumerate(books, 1):
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{i}. {book.title} by {book.author} ({status})")

     elif choice == "2":
            for i, book in enumerate(books, 1):
                if not book.is_borrowed:
                    print(f"{i}. {book.title} by {book.author}")
            book_index = int(input("Enter book number: ")) - 1
            if 0 <= book_index < len(book):
                member.borrow_book(book[book_index])
            else:
                print("Invalid choice.")

     elif choice == "3":
            for i, books in enumerate(member.borrowed_books, 1):
                print(f"{i}. {book.title} by {book.author}")
            book_index = int(input("Enter book number to return: ")) - 1
            if 0 <= book_index < len(member.borrowed_books):
                member.return_book(member.borrowed_books[book_index])
            else:
                print("Invalid choice.")

     elif choice == "4":
            member.list_borrowed_books()

     elif choice == "5":
            print("Goodbye!")
            break

     else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
