print("question no 01")
c=0
count_line=0
n=int(input("enter the no of lines which you wannt to print from last:"))
f=open("test.txt",'r')
for line in f:
    count_line=count_line+1
m=count_line-n
f.seek(0)
for line in f:
    c+=1
    if c>m:
        print(line)



print("question no 02")
with open('test.txt','r') as f:
    content=f.read()
    words=content.split()
    print(words)
    s=set(words)
    print(s)
    for n in s:
        print(n,words.count(n))



print("question no 03")
with open('test.txt','r')  as f1:
    with open('test1.txt','w') as f2:
        for line in f1:
            f2.write(line)



print("question no 04")
with open('test.txt','r') as f1:
    c1=f1.readlines()
with open('test1.txt','r') as f1:
    c2=f1.readlines()
i=0
for a in c1:
    print(c1[i]+c2[i])
    i=i+1



print('question no 05')
import random
with open ('test.txt','w')as f1:
    for i in range(10):
        m=random.randint(0,9)
        f1.write(str(m))
        f1.write("\n")
with open("test.txt",'r')as f:
    l=f.readlines()
    print(l)
l.sort()
print(l)
with open ('test1.txt','w')as f1:
    for n  in l:
        f1.write(n)
        f1.write('\n')


