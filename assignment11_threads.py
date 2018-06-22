import threading
from threading import Thread
import time

print("question no 01")
def display():
    time.sleep(5)
    print("hello !")
t=Thread(target=display)
t.start()


print("question no 02")
def table():
    for x in range (1,11):
        t.join()	#only for purpose  display the result in sequence
        print(x)
        time.sleep(1)
t1=Thread(target=table)
t1.start()



print("question no 03")
def list_element_print():
    m=2
    for x in l:
        t1.join()		#only for purpose  display the result in sequence
        print(x)
        time.sleep(m)
        m=m+2
l=[5,8,9,0,3]
t2=Thread(target=list_element_print)
t2.start()



print("question no 04")
def factorial():
    t2.join()     #only for purpose  display the result in sequence
    x=int(input("enter any no to find factorial:"))
    fact=1
    for a in range(1,x+1):
        fact=fact*a
    print(fact)
t3=Thread(target=factorial)
t3.start()