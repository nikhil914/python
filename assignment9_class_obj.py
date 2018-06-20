print("question no 01")
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        self.area=(3.14*self.radius*self.radius)
        print("area of circle is:",str(self.area))
    def circumfrance(self):
        self.circumfrance=(2*3.14*self.radius)
        print("circumfrance of circle is:",str(self.circumfrance))

r=int(input("enter any radius:"))
obj1=circle(r)
obj1.area()
obj1.circumfrance()
print("\n\n")



print("question no 02")
class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(self.name,self.roll)
n=input("enter any name:")
r=input("enter rollno")
o=student(n,r)
o.display()
print("\n\n")





print("question no 03")
class temprature:
    def __init__(self,celc,fahrn):
        self.celc=celc
        self.fahrn=fahrn
    def fah(self):
        fahrn=(1.8)*self.celc+32
        print("the converted temprature celcius to fahernhight is:",fahrn)
    def cel(self):
        celc=(self.fahrn-32)*5/9
        print("the converted temprature fahrenheit into celcius:",celc)
n=int(input("enter any cecius temprature to convert fahernheit: "))
m=int(input('enter any fahernheit temprature to  convert celcius: '))
t1=temprature(n,m)
t1.fah()
t1.cel()
print("\n\n")




print("question no 04")
class movie_details:
    def __init__(self,movie_name,artist_name,year_of_relese,ratings):
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.year_of_relese=year_of_relese
        self.ratings=ratings
    def show(self):
        print("movie name:",self.movie_name)
        print("artist name",self.artist_name)
        print("year of relese:",self.year_of_relese)
        print("rating:",self.ratings)
    def update(self):
        self.movie_name=input("enter any movie name to update:")
        self.artist_name=input("artist name:")
        self.year_of_relese=input("enter year of relese:")
        self.ratings=input("enter rating:")
        print("movie name:", self.movie_name)
        print("artist name", self.artist_name)
        print("year of relese:", self.year_of_relese)
        print("rating:", self.ratings)
m1=movie_details("3idiot","aamir khan","2009","5")
m1.show()
m1.update()
print("\n\n")




print("question no 05")
class Expenditure:
    def __init__(self,expenditure,saving):
        self.expenditure=expenditure
        self.saving=saving
    def show(self):
        print("expenditure :",self.expenditure)
        print("saving:",self.saving)
    def total_salary(self):
        salary=self.expenditure+self.saving
        print("Total salary :",salary)
ex=int(input("enter expenditure:"))
s=int(input("enter saving:"))
sal=Expenditure(ex,s)
sal.show()
sal.total_salary()

































































































































































































































