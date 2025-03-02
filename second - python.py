# Decisions in Python

# Relational Operators / Comparison 

# ==
# !=
# >=
# <=
# >
# <

# && #it require every condition true
# 
# or  #it requires only one condition to be true
# 
# not #its requires both false condition


# po=input("what's your Name:")
# 
# if po=="Rafay" or po=="rafay" or po=="rfy" or po=="rfffyyy" or po=="RAFAY": #TRUE
#     print("Your Condition is true!")
# else:
#     print("You are wrong")


print("********WELCOME TO CASIO CALCULATOR**********")

print("What you want to do? \nPress 1 for Addition \nPress 2 for Subtraction \nPress 3 for Division \nPress 4 for multiplication")

ud=int(input("Press your decision here:"))

if ud==1:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("This is your results for addtion:",num1+num2)
    
elif ud==2:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("This is your results for subtraction:",num1-num2)
    
elif ud==3:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("This is your results for Division:",num1/num2)
    
elif ud==4:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("This is your results for Multiplication:",num1*num2)
    
else:
    Print("The condition is false!")
    
    
print("Assignment for next class :::: 1:calculator \n2:University addmission program \n3Car/Mobile/Clothes/Course Selection System:")


name=input("Enter your name:")
father_name=input("Enter your Father Name:")
age=int(input("Enter your Age:"))
father_cnic=input("CNIC Format(42201-55555555-7):")

t_marks=int(input("Enter your obtained total marks in matric:"))

t_inter=int(input("Enter your obtained total marks in inter:"))

total=500

i_per=(t_inter/total*100)

if i_per>=55:
    print("You're elegible for the below programs \nSE, BM, CS, BBA, B.com, MBBS, ")




















