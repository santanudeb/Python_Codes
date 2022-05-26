# Polymorphism : Operator Overloading

class student () :

    def __init__(self,GDP) :
        self.GDP = GDP
    
    # Overloading Operator +
    def __add__(self, other) :
        return self.GDP + other.GDP


student1 = student(6)       
student2 = student(8)   
totalGDP = student1 + student2 # Without Overloading __add__ Operator this will not work

print(totalGDP)