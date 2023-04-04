#Define a function for addition 

def add(x, y):
	return x + y 
#Define a function for Subtraction 

def sub(x, y): 
	return x - y
#Define a function for Multiplication 
def multiply(x, y): 
	return x * y
#Define a function for Division 
def divide(x, y):
	return x / y

#display menu to choose

print("select an operator:")
print("1: Addition:")
print("2: Subtraction:")
print("3: Multiplication:")
print("4: Division:")

choice = input("Enter Choice: (1,2,3,4):")


#get the input numbers from choice 

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

if choice == "1":
	print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
	print(num1, "-", num2, "=", sub(num1, num2))

elif choice == "3":
	print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == "4":
	print(num1, "/", num2, "=", divide(num1, num2))

else:
	print("invalid argument")

	
