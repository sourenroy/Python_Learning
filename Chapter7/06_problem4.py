#prime Number 

n = int(input("Enter a Number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not Prime")
        break
else:
    print("This is a Prime Number")