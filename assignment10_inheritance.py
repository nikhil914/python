print("question 1")
class animal:
        def show(self):
         print("this is the animal class")
class tiger(animal):
        def display(self):
            print("this is the tiger class")
t1=tiger()
t1.display()
t1.show()



print("question 2")
#Q.2- What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return ('A')

class B(A):
    def g(self):
        return ('B')

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

#output
#A B
#A B





print("question 3")
class cop:
    def add(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.experience=experience
        self.designation=designation
    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
    def update(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.age=age
        self.experience=experience
        self.designation=designation
class mission(cop):
    def add_mission_details(self,mission):
        self.mission=mission
        print(self.mission)
m1=mission()
m1.add_mission_details("filled work")
m1.add('rahul',19,"DS","5years","DM")
m1.display()
m1.update('tiwari',19,"DA","8years","DM")
m1.display()




print("question 4")
class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
class rectangle(shape):
    def area(self):
        area=self.length*self.breadth
        print(area)
class square(shape):
    def area(self):
        area=self.length*self.breadth
        print(area)
m1=rectangle(3,9)
m1.area()
m2=square(5,5)
m2.area()

