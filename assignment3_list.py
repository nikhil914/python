print("question no 1 method 1")
l=[0,0,0]
l[0]=input("enter 1st element of list ")
l[1]=input("enter 2nd element of list ")
l[2]=input("enter 3rd element of list ")
print(l)
print("\n\n\n")


#method 2 
print("question no 1 method 2")
x=int(input('enter 1st element of list '))
y=int(input('enter 2nd element of list '))
z=int(input('enter 3rd element of list '))
l=[x,y,z]
print(l)
print("\n\n\n")



print("question no 2")
x=['india','japan','chaina']
x1=['google','apple','facebook','microsoft','tesle']
x.extend(x1)
print(x)
print("\n\n\n")

print("question no 3")
y=[1,2,1,4,2,3,2,2,3,2]
print("the list is",y)
print("the no of 2 in above list ",y.count(2))
print("\n\n\n")

print("question no 4")
z=[2,4,1,8,5,6]
z.sort()         #sort the list ("ascending order")
print(z)
print("\n\n\n")

print("question no 5")
a=[1,2,7,5,3]
b=[5,2,1,4,6]
c=a+b
print("merge list is",c)
c.sort()					#sort the list ("ascending order")
print("sorted list is",c)
print("\n\n\n")

print("question no 6")
p=[]
print('stack is',p)
p.append(int(input("enter any no to push in stack ")))   #for adding a new element in list(stack)
p.append(int(input("enter any no to push in stack ")))
p.append(int(input("enter any no to push in stack ")))
print(p)
del p[0]								 #for removing a element from list(queue)
del p[0]								 #for removing a element from list(queue)
                                    #for removing a element from list(stack)
print('after pop the stack is',p)
print("\n\n\n")

p=[]
print('queue is',p)
p.insert(0,int(input("enter any no to push in queue ")))    #for adding a new element in list(queue)
p.insert(0,int(input("enter any no to push in queue ")))
p.insert(0,int(input("enter any no to push in queue ")))
print('after push a element the queue is',p)
del p[0]								 #for removing a element from list(queue)
print("after deleting the queue is",p)


print("question no 7")
v=0
n=0
q=[4,5,6,7,8,9,10,2,12,15]
print("list is",q)
for a in range q:
	if q[a]%2==0:			# checking even no
		v=v+1 
	if q[a]%2!=0:			#checking odd no
		n=n+1
print("the odd no is in list=",n) 
print("the even no is in list=",v)
	













