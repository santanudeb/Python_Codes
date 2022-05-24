# Inner Class

class alien :
    
    # Constructor 
    def __init__(self, height, color) :
        self.height = height
        self.color = color
    
    # Method
    def show(self) :
        print(self.height, self.color)    
    
    # Inner Class
    class spaceship :
        
        # Inner Class Constructor 
        def __init__(self,shape) :
            self.shape = shape
        
        # Inner Class Method
        def show(self) :
            print(self.shape)     


alien1 = alien(5, "blue") # Object of Class alien
alien2 = alien(6, "white") # Object of Class alien

alien1.show()
alien2.show()

alien1ship = alien1.spaceship("round") # Object of Class spaceship
alien1ship.show()

alien2ship = alien2.spaceship("triangle") # Object of Class spaceship
alien2ship.show()