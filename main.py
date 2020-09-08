class Library:
    def __init__(self,libname,list):
        self.libname = libname
        self.listofbooks = list
        self.bookrent = {}
    
    #Adding Function To Display Books of Library.
    def display(self):
        print("These Are the Books :")
        print("\n")
        for books in self.listofbooks:
            print(books)
        print("\n")
    
    #Adding Lend Function to Display lender of Book's.
    def rent(self,renter,book):
        if book not in self.bookrent.keys():
            self.bookrent.update({renter: book})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    #Addding ADD Books Function.
    def addbooks(self,book):
        listofbooks.append(book)
        print("Book has been added to the book list")

    #Adding Return Book Function.
    def returnbook(self,book):
        self.bookrent.pop(book)
        print("You  have returned the Book. Thank you. : )")


if __name__ == "__main__":
    # Add Library into Class.
    Govind = Library("Govind Suroliya", ["Martin Garrix Books","Harry Potter","Python Basics","Java Basics"])

    print("Walcame to Library Managent System. ©2020 Ti Corporation \n")
    print(f"Walcame to {Govind.libname} Library.\n\n")

    while True:
        #Shownig the Options from Library
        print("1. Display Books.")
        print("2. Rent Book.")
        print("4. Donate Books.")
        print("4. Return Books.\n")
        user_input = input("Enter Choice From These Options : ")

        if user_input not in ["1", "2", "3", "4"]:
            print("Invalid User Input. Plase Enter Current Input.")
        else:
            user_input = int(user_input)


        if user_input == 1: # Show Case All Library Books.
            Govind.display()

        elif user_input == 2: # Taking input Lender Name or Books.
            usernames = input("Enter Your Name : ")
            userbooks = input("Enter Book Name which You want : ")
            Govind.rent(usernames,userbooks)
        
        elif user_input == 3: # Donate the Books form Users.
            Govind.rent(input("Enter Book Name : "))

        elif user_input == 4:
            Govind.returnbook(input("Enter the Name of the Book You want to return : "))

        else: 
            print("Invalid User Input. Plase Enter Current Input.")

        user_input2 = input("Press 'Q' to Quit and 'C' to Continue : ")
        user_input2 = ""
        if user_input == "q":
            exit()
        elif user_input == "c":
            continue
        else:
            print("Invalid User Input. Plase Enter Current Input.")
