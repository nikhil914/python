print("queston no 1 ")
#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

# Index	Field	Values
# 0	4-digit year	2008
# 1	Month	1 to 12
# 2	Day	1 to 31
# 3	Hour	0 to 23
# 4	Minute	0 to 59
# 5	Second	0 to 61 (60 or 61 are leap-seconds)
# 6	Day of Week	0 to 6 (0 is Monday)
# 7	Day of year	1 to 366 (Julian day)
# 8	Daylight savings	-1, 0, 1, -1 means library determines DST
# The above tuple is equivalent to struct_time structure. This structure has following attributes −
#
# Index	Attributes	Values
# 0	tm_year	2008
# 1	tm_mon	1 to 12
# 2	tm_mday	1 to 31
# 3	tm_hour	0 to 23
# 4	tm_min	0 to 59
# 5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
# 6	tm_wday	0 to 6 (0 is Monday)
# 7	tm_yday	1 to 366 (Julian day)
# 8	tm_isdst	-1, 0, 1, -1 means library determines DST
print("\n\n"")



print("question no 2")
import time
print(time.ctime())
print("\n\n")

print("question no 3")
s=time.gmtime()
print("the current date and time is:",s)
print("the current month is:",s[1])
print("\n\n")


print("question no 4")
t=time.gmtime()
day=t[6]
print("the current time is",time.ctime())
if day==0:
    print("Monday")
if day==1:
    print("Tuesday")
if day==2:
    print("Wednesday")
if day==3:
    print("Thrusday")
if day==4:
    print("Friday")
if day==5:
    print("Saturday")
if day==6:
    print("Sunday")
print("\n\n")


print("question no 5")
t=time.gmtime()
date=t[2]
print("the current time is",time.ctime())
print("the current date is",date)
print("\n\n")

print("question no 6")
print(time.localtime())
print("\n\n")




print("question no 7")
import math
x=int(input("enter any no to find factorial:"))
print(math.factorial(x))
print("\n\n")



print("question no 8")
a=int(input("enter 1st number for GCD:"))
b=int(input("enter 2nd number for GCD:"))
print("the GCD is:",math.gcd(a,b))
print("\n\n")


print("question no 9")
import os
print(os.getcwd())
print(os.environ)
print("\n\n")

