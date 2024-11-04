from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class humun(animal):
    def move(self):
        print("i can walk and run")
class dog(animal):
    def move(self):
        print("i can bark")
r= humun()
r.move()
t= dog()
t.move()