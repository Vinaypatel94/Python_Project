# The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment
import sys
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation:")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.Exit")


while True:
    choice=input("Enter the choice(1/2/3/4/5):")
    if choice in('1','2','3','4','5'):
        if choice=='5':
            print("you are exit")
            break
        try:
            num1=float(input('Enter the first Number: '))
            num2=float(input("Enter Second Number:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=="2":
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=="3":
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=="4":
            print(num1,"/",num2,"=",divide(num1,num2))
       
    else:
        print("Invalid input")
    




