# By default python doesn't support Method Overloading
# Polymorphism : Method Overloading

class calculator () :

    def __init__(self) -> None:
        pass

    def sum (self,n1=None,n2=None,n3=None) :
        
        re = 0

        if n1!=None and n2!=None and n3!=None :
            re = n1 + n2 + n3
        elif n1!=None and n2!=None :
            re = n1 + n2
        else :
            re = n1     

        return re

calculator1 = calculator()    
# result = calculator1.sum(3)  # -> 3
# result = calculator1.sum(3,6)  # -> 9
result = calculator1.sum(3,6,9)  # -> 18

print(result)