#Factorial of a Number

n = int(input("Enter a Number: "))
pro = 1
for i in range(1, n+1):
    pro = pro*i

print("Factorial is :",pro)