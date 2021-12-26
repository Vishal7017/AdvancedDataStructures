import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str(self):
        return "animal:"+ str(self.name)+":"+str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.name = name
        self.friends = []

    def get_friends(self):
        return self.friends
    
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    
    def speak(self):
        print("Hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25<= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
        
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)



# print("\n------ person tests ------")
# p1 = Person("jack", 30)
# p2 = Person("jill", 25)
# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)



print("\n------ student tests ------")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
print(s1)
print(s2)
print(s1.get_name(), "says:", end= " ")
s1.speak()
print(s2.get_name()," says:", end= " ")
s2.speak()