class Person: #class is a template
    name="Aniket"
    occupation="software intern"
    def info(self): #self keyword means current instance of class
        print(f"{self.name} is a {self.occupation}")

Aniket=Person() #object creation of Person, Person is a template and Aniket is an instance or copy
Soumashree=Person()
Soumashree.name="Soumashree"
tamojit=Person()
tamojit.name="Tamojit"
tamojit.occupation="Data scientist"
Aniket.info()
Soumashree.info()
tamojit.info()