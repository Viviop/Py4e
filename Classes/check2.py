class Person:
   def __init__(self,name,age):
     self.name= name
     self.age= age
    
    def myfunc(self):
      print("Hi My name is",self.name)
    
p1=Person("Vivhaan",16)
p1.myfunc()