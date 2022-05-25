# Polymorphism : Dusk Typing

class mobile () :

    def gaming (self) :
        print("Game is runnig")

class computer () :

    def gaming (self) :
        print("Game is runnig")   
        print("Better FPS")  


#game = mobile()
game = computer()

# Changing class of game will change behaviour
game.gaming()