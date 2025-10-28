lst = [10, 20, 50, "He", True]

i = 0

while(i<len(lst)):
    print(lst[i])
    i+=1

#For Loop
ls= [10, 20, 30, 40]
for i in ls:
    print(i)
    i+=1

l= [1,7,8] 
for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!


#Continue and Break

for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    

for i in range(645):
    pass #Pass the loop(do it later)
