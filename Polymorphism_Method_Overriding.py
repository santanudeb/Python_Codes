# Polymorphism : Method Overriding

class father () :

    def mobile (self) :
        print("Samsung")

class son (father) :
    pass

    def mobile (self) : # changing behaviour of mobile method
        print("Nokia")


mbName = son()
mbName.mobile()