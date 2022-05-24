# Inheritance

class grandparent () :

    def feature1 () :
        print("feature1 included")

# inheriting grandparent
# single level inheritance
class parent (grandparent) :

    def feature2 () :
        print("feature2 included")

# inheriting parent
# multi level inheritance
class child (parent) :

    def feature3 () :
        print("feature3 included")

class relative () :

    def feature4 () :
        print("feature4 included")

## inheriting relative, grandparent
# multiple inheritance
class relativeschild (relative, grandparent) :

    def feature5 () :
        print("feature5 included")

child1 = child ()  

child.feature1() 
child.feature2() 
child.feature3()     
relativeschild.feature1()
relativeschild.feature4()
relativeschild.feature5()