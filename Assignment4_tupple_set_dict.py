print("question no 1 & 2")
t=(1,3,5,7,9,11,)
t1=('india','china','japan')
print(t)
print(len(t))		#find the length
print(max(t)) 		#find maximum
print(min(t))		#find minimum
print(t1)
print(len(t1))
print(max(t1))
print(min(t1))
print("\n\n\n")

print("question no 3 ")
t=(1,3,5,7,9,11)
q=1
for a in range(0,6):
	k=t[a]					
	q=k*q
print(q)
print("\n\n\n")

print("question no 4(1,2,3) ")
l=[0,0,0]
l[0]=input("enter 1st element of 1st set ")
l[1]=input("enter 2nd element of 1st set ")
l[2]=input("enter 3rd element of 1st set ")

l1=[0,0,0]
l1[0]=input("enter 1st element of 2nd set ")
l1[1]=input("enter 2nd element of 2nd set ")
l1[2]=input("enter 3rd element of 2nd set ")
s1=set(l)			#type casting
s2=set(l1)
print(s1)
print(s2)
print(s1-s2) 		#difference of two sets
if s1==s2:
	print("sets are equal")
else:
	print("sets are not equal")
print(s1&s2)
print("\n\n\n")

print("question no 5 & 6 ")
d={}
l=[]
for a in range(0,10):
	name=input("enter a name:")
	marks=int(input("enter any marks: "))
	l.append(marks)
	d[name]=marks
print(d)
l.sort()				#sort the list
print("the sorted marks are",l)
print("\n\n\n")

print("question no 7 ")
s='MISSISSIPPI'
m=list(s)
a=m.count('M')		#count the m in mississippi
b=m.count('I')
c=m.count('S')
d=m.count('P')
g={'M':a,'I':b,'S':c,'P':d}
print("the dictionary of MISSISSIPPI of each letter is",g)
print("\n\n") 