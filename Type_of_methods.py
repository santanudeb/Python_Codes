# Type of methods

from cmath import pi


class numbers():

    pi = 3.14 # Class variable

    def __init__(self, n1, n2) :
        self.n1 = n1 # Instance variable
        self.n2 = n2 # Instance variable
        
    # Instance method   
    def avg(self):
        return (self.n1 + self.n2) / 2

    # Class method   
    @classmethod 
    def sum(cls):
        return pi
    
    # Static method
    @staticmethod
    def info():
        print("Info about something")

# Creating object and passing values
num1 = numbers(2,4)

im_value = num1.avg() # Storing value from Instance method
cm_value = num1.sum() # Storing value from Static method

print(im_value)
print(cm_value)
num1.info()