# Abstract Class & Abstract Method

from abc import ABC, abstractmethod

# Abstract Class : Have one abstract method
class Computer () :
    
    # Abstract method
    @abstractmethod
    def process (self) :
        pass

class Laptop (Computer) :

    def process (self) : # Overiding process method
        print("in laptop")

# computer1 = Computer() # does nothing
# computer1.process()    # does nothing

computer2 = Laptop() 
computer2.process()