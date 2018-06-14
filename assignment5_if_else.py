print("question no 1")
y = int(input("Enter any year to check leap year: "))

if (y % 4) == 0:

   if (y % 100) == 0:

       if (y % 400) == 0:

           print(" {} is a leap year".format(y))

       else:

           print(" {} is not a leap year".format(y))

   else:

       print(" {} is a leap year".format(y))
else:

   print(" {} is not a leap year".format(y))
print("\n\n\n")




print("question no 2")
x=int(input("enter length "))
y=int(input("enter breadth "))
if x==y:
	print("the given dimension {}*{} is square".format(x,y))
else:
	print("the given dimension {}*{} is rectangle".format(x,y))
print("\n\n\n")




print("question no 3")
p=int(input("enter age of 1st person "))
q=int(input("enter age of 2nd person "))
r=int(input("enter age of 3rd person "))
if (p>q) and (p>r):
	print("1st person is oldest")
elif (q>r) and (q>p):
	print("2nd person is oldest")
else :
	 	print("3rd person is oldest")
if (p<q) and (p<r):
	print("1st is youngest")
elif (q<r) and (q<p):
	print("2nd person is youngest")
else :
	 	print("3rd person is youngest")
print("\n\n\n")





print("question no 4")
y=int(input("enter the points that you scored <200 :"))
if y>=1 and y<=50:
	print("Sorry! No prize this time.")
if y>=51 and y<=150:
	print("Congratulations! You won a Wooden Dog")
if y>=151 and y<=180:
	print("Congratulations! You won a Book")
if y>=181 and y<=200:
	print("Congratulations! You won a Chocolates")
print("\n\n\n")




print("question no 5")
s=int(input("enter the purchase quantity"))
c=s*100										#calculating cost
if c>=1000:
	print("you are eligible for discount")
	d=(c*10)/100							#calculating discount
	p=c-d									#calculate total payble amount
	print("your total cost is:",p)
else:
	print("you are not eligible for discount")

	
	
	





