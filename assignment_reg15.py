import re



print("question no 01")
l=[]
a1="zuck26@facebook.com"
a2="page33@google.com"
a3="jeff42@amazon.com"
print(re.findall(r"(.+)@(.+)\.(.+)",a1),end="")
print(re.findall(r"(.+)@(.+)\.(.+)",a2),end="")
print(re.findall(r"(.+)@(.+)\.(.+)",a3),end="")




print("question no 02")
s="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p=re.compile(r"b[a-z]+")
result=p.findall(s)
for i in result:
    print(i)
p=re.compile(r"B[a-z]+")
result=p.findall(s)
for i in result:
    print(i)



print("question no 03")
s= "A, very very; irregular_sentence"
p=re.sub(r","," ",s)
p=re.sub(r";"," ",p)
p=re.sub(r"_"," ",p)
print(p)





print("question no 04")
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
p=re.sub(r"! RT @TheNextWeb:"," ",tweet)
p=re.sub(r" http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"," ",p)
print(p)

