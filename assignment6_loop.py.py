print("question no 1")
x=[]
for y in range(0,10):
    p=int(input("enter any no: "))
    x.append(p)
for y in range(0,10):
    print(x[y])
print("\n\n")




print("question no 2")
i=0
while i<12:
    print("rahul")
print("\n\n")




print("question no 3")
y=[]
z=[]
for i in range(0,5):
    p=int(input("enter any no: "))
    y.append(p)
for i in range(0,5):
    a=y[i]
    p=a*a
    z.append(p)
print(z)
print("\n\n")






print("question no 4")
l=[1,7,'abilash',4.5,6,'rahul',8,5.1]
i=[]
s=[]
f=[]
for a in l:
    if type(a)==int:
        i.append(a)
    if type(a)==str:
        s.append(a)
    if type(a)==float:
        f.append(a)
print("integer list is",i)
print("string list is",s)
print('float string is',f)
print("\n\n")




print("question no 5")
k=[]
l=[]
for a in range (1,101):
    if a%2==0:
        k.append(a)
    else:
        l.append(a)
print("even no list",k)
print("odd no list",l)
print("\n\n")




print("question no 6")
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end='')
    print("\n")
print("\n\n")




print("question no 7")
d={}
for a in range(0,10):
	n=input("enter a key:")
	m=input("enter any values: ")
	d[n]=m
print(d)
print("\n\n")




print("question no 8")
l=[]
flag=0
for x in range(0,10):
    l.append(int(input("enter any no:")))
print(l)
y=int(input("enter any no to serch:"))
for x in l:
    if x==y:
        l.remove(x)                 #delete the element
        flag=1
print(l)
if flag==0:
    print("no not found")


