from abc import ABC,abstractmethod
class XYZ(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("we are inside XYZ task ")
class test(XYZ):
    def task(self):
        print("we are inside test class")
obj= test()
obj.task()
obj.print(100)