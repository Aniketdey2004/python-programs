#constructor is called when an instance created
class Person: #class is a template
    def __init__(self,name,occupation): #parameterised constructor
        self.name=name
        self.occupation=occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")
Aniket=Person("Aniket","Software Developer")#self is passed automatically the rest we have to pass
Aniket.info()
"""class Person: #class is a template
    name="Aniket"
    occupation="software developer"
    def __init__(self): #default constructor
        print("hi")
    def info(self):
        print(f"{self.name} is a {self.occupation}")"""