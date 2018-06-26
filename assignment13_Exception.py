print("question 01")
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except Exception as e:
    print(e)
#Exception name:division by zero


print("question 02")
l=[1,2,3]
try:
    print(l[3])
except Exception as e:
    print(e)
#Exception name:list index out of range



print("question no 03")
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")

#exception is raised exception name is:NameError: Hi there





print("question 04")
def AbyB(a,b):
	try:
		c = ((a+b)/(a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output
#-5.0
#a/b result in 0




print("question no 05")
#import rahul
#it genrate import exception ModuleNotFoundError: No module named 'rahul'
m=int(input("enter any string:"))
try:
    print(m)
except Exception as e:
    print(e)

#ValueError: invalid literal for int() with base 10: 'rahul'

l=[1,2,3]
try:
    print(l[3])
except Exception as e:
    print(e)
#list index out of range


print("question no 06")
class AgeTooSmallError(Exception):
    pass
try:
    while True:
        age = int(input("enter any age:"))
        if age<18:
            print("age is less than 18: ",age)
        else:
            raise AgeTooSmallError("age is above 18")
except AgeTooSmallError as e:
    print(e)



