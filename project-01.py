#             # task 1

# import os
# def menu():
#      print("Library")
#      print("1. Add a book:")
#      print("2. view books:")
#      print("3. Exit:")
     
# def add_new_book(filename):
#         try:
#             with open(filename, "a") as file:
#                 title=input("Enter the book title: ")
#                 author=input("Enter the author:")
#                 publication_year=input("Enter the year: ")
#                 book=f'{title},{author},{publication_year}\n'
#                 file.write(book)
#                 print("Book added successfully.")
#         except Exception as e:
#             print(f' An Error Ocuured:{e}')

# def view_inventory(filename):
#     try:
#         if os.path.exists(filename):
#             with open (filename,"r") as file:
#                 books=file.readlines()
#                 if books:
#                     print("Inventory:")
#                     for book in books:
#                             try:
#                                 title,author,publication_year=book.strip().split(',')
#                                 print(f'Title: {title}, Author : {author}, Year of publication: {publication_year}')
#                             except ValueError:
#                                 print(f"skipping malformed line: {book.strip()}")
#                 else:
#                     print("No record found...")
#         else:
#             print("inventory file does not exists.")

#     except Exception as e:
#         print(f"An error ocuured: {e}:")

# # In your main function, call the delete_book function
# def main():
#     filename = "books.txt"
#     while True:
#         menu()
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             add_new_book(filename)
#         elif choice == "2":
#             view_inventory(filename)
#         elif choice == "3":
#             print("Exiting the code.")
#         else:
#             print("Invalid choice.")
#             break

# if __name__ == "__main__":
#     main()


# #             # task 2
# import os
# def menu():
#      print("Library")
#      print("1. Add a book:")
#      print("2. view books:")
#      print("3. search for book:")
#      print("4. Exit")

# def add_new_book(filename):
#         try:
#             with open(filename, "a") as file:
#                 title=input("Enter the book title: ")
#                 author=input("Enter the author:")
#                 publication_year=input("Enter the year: ")
#                 book=f'{title},{author},{publication_year}\n'
#                 file.write(book)
#                 print("Book added successfully.")
#         except Exception as e:
#             print(f' An Error Ocuured:{e}')

# def view_inventory(filename):
#     try:
#         if os.path.exists(filename):
#             with open (filename,"r") as file:
#                 books=file.readlines()
#                 if books:
#                     print("Inventory:")
#                     for book in books:
#                             try:
#                                 title,author,publication_year=book.strip().split(',')
#                                 print(f'Title: {title}, Author : {author}, Year of publication: {publication_year}')
#                             except ValueError:
#                                 print(f"skipping malformed line: {book.strip()}")
#                 else:
#                     print("No record found...")
#         else:
#             print("inventory file does not exists.")

#     except Exception as e:
#         print(f"An error ocuured: {e}:")

# def search_book(filename):
#     try:
#         if os.path.exists(filename):
#             search=input("Enter the book name: ")
#             with open (filename, "r") as file:
#                 books=file.readlines()
#                 found=False
#                 for book in books:
#                         title,author,publication_year=book.strip().split(",")
#                         if title==search:
#                             print(f'Found-Title:{title}, Author is: {author}, year of publication: {publication_year}\n ')
#                             found=True
#                 if not found:
#                     print("Book not found")
#         else: 
#             print("Inventory file does not exist.")

#     except Exception as e:
#         print(f" An Error occured: {e}")

# def main():
#     filename = "books.txt"
#     while True:
#         menu()
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             add_new_book(filename)
#         elif choice == "2":
#             view_inventory(filename)
#         elif choice == "3":
#             search_book(filename)
#         elif choice == "4":
#             print("Exiting the code.")
#         else:
#             print("Invalid choice.")
#             break

# if __name__ == "__main__":
#     main()


# #             # TASK 03
    
# # import os
# # def menu():
# #      print("Library")
# #      print("1. Add a book:")
# #      print("2. view books:")
# #      print("3. search for book:")
# #      print("4. Exit")

# # def add_new_book(filename):
# #         try:
# #             with open(filename, "a") as file:
# #                 title=input("Enter the book title: ")
# #                 author=input("Enter the author:")
# #                 publication_year=input("Enter the year: ")
# #                 book=f'{title},{author},{publication_year}\n'
# #                 file.write(book)
# #                 print("Book added successfully.")
# #         except Exception as e:
# #             print(f' An Error Ocuured:{e}')

# # def view_inventory(filename):
# #     try:
# #         if os.path.exists(filename):
# #             with open (filename,"r") as file:
# #                 books=file.readlines()
# #                 if books:
# #                     print("Inventory:")
# #                     for book in books:
# #                             try:
# #                                 title,author,publication_year=book.strip().split(',')
# #                                 print(f'Title: {title}, Author : {author}, Year of publication: {publication_year}')
# #                             except ValueError:
# #                                 print(f"skipping malformed line: {book.strip()}")
# #                 else:
# #                     print("No record found...")
# #         else:
# #             print("inventory file does not exists.")

# #     except Exception as e:
# #         print(f"An error ocuured: {e}:")

# # def search_book(filename):
# #     try:
# #         if os.path.exists(filename):
# #             search=input("Enter the book name: ")
# #             with open (filename, "r") as file:
# #                 books=file.readlines()
# #                 found=False
# #                 for book in books:
# #                         title,author,publication_year=book.strip().split(",")
# #                         if title==search:
# #                             print(f'Found-Title:{title}, Author is: {author}, year of publication: {publication_year}\n ')
# #                             found=True
# #                 if not found:
# #                     print("Book not found")
# #         else: 
# #             print("Inventory file does not exist.")

# #     except Exception as e:
# #         print(f" An Error occured: {e}")

# # def delete_book(filename):
# #     try:
# #         if os.path.exists(filename):
# #             title1=input("Enter the title of book:" ).lower()
# #             with open(filename, "r") as file:
# #                 books = file.readlines()

# #             with open(filename, "w") as file:
# #                 deleted = False
# #                 for book in books:
# #                     title, author, publication_year = book.strip().split(",")
# #                     if title != title1:
# #                         file.write(book)
# #                     else:
# #                         deleted = True
                
# #                 if deleted:
# #                     print("Book deleted successfully.")
# #                 else:
# #                     print("Book not found.")
# #         else:
# #             print("Inventory file does not exist.")
            
# #     except Exception as e:
# #         print(f"An error occurred: {e}")

# # # In your main function, call the delete_book function
# # def main():
# #     filename = "books.txt"
# #     while True:
# #         menu()
# #         choice = input("Enter your choice: ")
# #         if choice == "1":
# #             add_new_book(filename)
# #         elif choice == "2":
# #             view_inventory(filename)
# #         elif choice == "3":
# #             search_book(filename)
# #         elif choice == "4":
# #             print("Exiting the code.")
# #         else:
# #             print("Invalid choice.")
# #             break

# # if __name__ == "__main__":
# #     main()

# # #                  TASK 04
    
import os
def menu():
     print("Library")
     print("1. Add a book:")
     print("2. view books:")
     print("3. search for book:")  
     print("4. Delete a book")
     print("5. borrow a book")
     print("6. Exit")


def add_new_book(filename):
        try:
            with open(filename, "a") as file:
                title=input("Enter the book title: ")
                author=input("Enter the author:")
                publication_year=input("Enter the year: ")
                book=f'{title},{author},{publication_year}\n'
                file.write(book)
                print("Book added successfully.")
        except Exception as e:
            print(f' An Error Ocuured:{e}')

def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open (filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                            try:
                                title,author,publication_year=book.strip().split(',')
                                print(f'Title: {title}, Author : {author}, Year of publication: {publication_year}')
                            except ValueError:
                                print(f"skipping malformed line: {book.strip()}")
                else:
                    print("No record found...")
        else:
            print("inventory file does not exists.")

    except Exception as e:
        print(f"An error ocuured: {e}:")

def search_book(filename):
    try:
        if os.path.exists(filename):
            search=input("Enter the book name: ")
            with open (filename, "r") as file:
                books=file.readlines()
                found=False
                for book in books:
                        title,author,publication_year=book.strip().split(",")
                        if title==search:
                            print(f'Found-Title:{title}, Author is: {author}, year of publication: {publication_year}\n ')
                            found=True
                if not found:
                    print("Book not found")
        else: 
            print("Inventory file does not exist.")

    except Exception as e:
        print(f" An Error occured: {e}")

def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the title of book:" ).lower()
            with open(filename, "r") as file:
                books = file.readlines()

            with open(filename, "w") as file:
                deleted = False
                for book in books:
                    title, author, publication_year = book.strip().split(",")
                    if title != title1:
                        file.write(book)
                    else:
                        deleted = True
                
                if deleted:
                    print("Book deleted successfully.")
                else:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

def borrow_book(books_filename, borrowed_filename):
    try:
        if os.path.exists(books_filename):
                search=input("Enter the book title5 to borrow: ")
                with open (books_filename,"r") as file:
                     books=file.readlines()

                with open(books_filename, "w") as file:
                    borrowed = False

                for book in books:
                        title,author,publication_year, status=book.strip().split(",")
                        if title.lower() == borrow_book and "available" in status:
                            print(f'Found-Title:{title}, Author is: {author}, year of publication: {publication_year},borrowed\n ')
                            with open (borrowed_filename,"a") as borrowed_file:
                                borrowed_file.write(f'{title }, {author},{publication_year}, \n')
                            borrowed =True
                            
                        else:
                            file.write(book)

                if borrowed:
                    print("book borrowed sucessfully")
                else:
                    print("book not found")    
        else:
            print("inventory file does not exist.")    
    except Exception as e:
        print(f" An Error occured: {e}")
     


# In your main function
def main():
    filename = "books.txt"
    borrowed_filename= "borrow_book.txt"
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_new_book(filename)
        elif choice == "2":
            view_inventory(filename)
        elif choice == "3":
            search_book(filename)
        elif choice =="4":
             delete_book(filename)
        elif choice == "5":
           borrow_book(filename, borrowed_filename)
        elif choice == "6":
            print("Exiting the code.")
        else:
            print("Invalid choice.")
            break

if __name__ == "__main__":
    main()