# Class Object Constructor Method

from ast import Return

# Class definition
class book:
    
    # Class Variables. Changing here will impact all objects. 
    booktype = "Hardcover"

    # Constructor __init__
    def __init__(self, name, price, genre):

        # Instance Variables
        self.name = name      # self.name is storing the name for the object being created
        self.price = price    # self.price is storing the price for the object being created
        self.genre = genre    # self.genre is storing the genre for the object being created

    # Function within class or Method
    def compare(self,valueFromOther) :
        if (self.price == valueFromOther.price) :
            return True
        else :
            return False  

book1 = book("1984", 199, "Dystopian") # book1 is the object of the class book and Passing the value.
book2 = book("Animal Farm", 199, "Political Satire") # book2 is the object of the class book and Passing the value.

print(book1.name)
print(book1.price)
print(book1.genre)
print(book1.booktype)

print(book2.name)
print(book2.price)
print(book2.genre)
print(book1.booktype)

# Checking if both books has same price
check = book1.compare(book2)
if check == True :
    print("Same Price")
else : 
    print("Different Price")    