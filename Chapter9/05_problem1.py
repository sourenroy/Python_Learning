f = open("poem.txt")
c = f.read()

if("twinkle" in c):
    print("The Word is Present")
    
else:
    print("Word is not Present")

f.close()