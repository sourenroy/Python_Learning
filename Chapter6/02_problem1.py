a1 = int(input("Enter the number 1: "))
a2 =int(input("Enter the number  2: "))
a3 = int(input("Enter the number 3: "))


if(a1 > a2 and a1>a3):
    print(f"Greates Number is {a1}")
elif(a2 > a1 and a1>a3):
    print(f"Greates Number is {a2}")
elif(a3 > a1 and a3>a2):
    print(f"Greates Number is {a3}")

else:
    print("All are same")