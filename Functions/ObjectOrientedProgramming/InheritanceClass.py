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



# print("\n------ student tests ------")
# s1 = Student('alice', 20, "CS")
# s2 = Student('beth', 18)
# print(s1)
# print(s2)
# print(s1.get_name(), "says:", end= " ")
# s1.speak()
# print(s2.get_name()," says:", end= " ")
# s2.speak()

""" Rabbit Getter Methods"""

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    
    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.paren2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

    
print("\n---- rabbit tests ------")
print("------ testing creating rabbits ------")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)

print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())