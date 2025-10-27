marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))

#Check your total percentenge 
total_marks = (100*(marks1 + marks2 + marks3))/300

if(total_marks >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Good !, You Pass",total_marks)
else:
    print("Sorry !!, You Fail !",total_marks)

