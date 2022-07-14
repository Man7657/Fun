# class Everything:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def something(self):
#         print(self.name, "is",  self.age,  "years old")
#
#     def something(self,place):
#         print(self.name, "who is", self.age, "years old lives in", place)
#
#
# class Anything(Everything):
#     def __init__(self, name, age, place): # the moment u define init function will overrides the parents class methods and function
#         self.place = place
#         Everything.__init__(self, name, age) #should include parent init fntn so that to inherit parents methods and fntns along with new one
#
#     def allthing(self):
#         print(self.name, "living in", self.place, "has completed his life journey of", self.age, "years")
#
#
# Student1 = Everything("Enrique",25)
# Student2 = Anything("Pit-bull",28, "Denmark")
# #Student1.something() # parent class object
# Student1.something("Tokyo")
# Student2.something("Nairobi")
# #Student2.something() #inherits parent class properties
# Student2.allthing() # inherits and overrides parent class properties
#
class A:
    def __init__(self):
        print("Hello")

    def set(self):
        print("Set A")

    def get(self):
        print("Get A")


class B:
    def __init__(self):
        print("Hello world")

    def set(self):
        print("Set B")

    def get(self):
        print("Get B")


class C(B,A):
    def __init__(self):
        print("Good Morning")
        super().__init__()

    # def set(self):
    #     print("Set C")
    #     #A.set(self)
    #     #B.get(self)


obj = C() # displays object instances
obj.set() # displays according to MRO
A.set(obj) # class.method(created object for derived class) gives particular method from particular class
B.get(obj)
