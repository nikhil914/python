#question no 1
def area():
    r=float(input("enter radius:"))
    area=(22/7)*r*r
    print(area)
    return
area()
print("\n\n")



#question no 2
p=[]
def perfect():
    for x in range(1,1000):
        l=[]
        s=0
        for y in range(1,x):
            if x%y==0:
                l.append(y)
        for a in l:
            s=s+a
        if s==x:
            p.append(x)
perfect()
print(p)
print("\n\n")




#question no 3
def table(n):
    if n>10:
        return
    else:
        print(12*n)
        table(n+1)
table(1)
print("\n\n")





#question no 4
def power(b,p):
    s=1
    if p==1:
        return b
    else:
        s=b*power(b,p-1)
        return s

print(power(5,5))
print("\n\n")




#question no 5
n=int(input("enter any no:"))
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        b=n*fact(n-1)
        return b
print("factorial is:",fact(n))
d={n:fact(n)}
print("dictionary of factorial is",d)





