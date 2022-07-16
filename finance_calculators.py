#This imports the math library
import math


#The multiline function prints strings into multiple lines
print('''Chooses either 'investment' or 'bond' from the menu below to proceed:

investment    -to calculate the amount of interest you'll earn on interest
bond          -to calculate the amount you'll have to pay on a home loan''')



#The input function allows the user to input information
#The lower case function changes any characters the user has entered into lower case
#I used the lower case function so that the program proceeds even if the user
#spells the words in any case
type_of_calculation = str(input("Enter type of calculation:").lower())

if (type_of_calculation != "investment") and (type_of_calculation != "bond"):
    print("You have not selected any of the above.")

#Calculation for investment
elif type_of_calculation == "investment":
    P = float(input("Enter amount of money you are depositing:"))      #The P stands for principle amount
    
    r = float(input("Enter interest rate:"))/100                       #The r stands for rate, the interest
    
    t = int(input("Enter years of investment:"))                       #The t for time, years invested

    interest = str(input("Do you want simple or compound interest?").lower())
    if (interest != "simple") and (interest != "compound"):
        print("You have not selected any between the two:")
        
    elif interest == "simple":
        A = P*(1 + (r*t))
        print("Total amount:", A)

    else:
        A = P*math.pow((1+r),t)
        print("Total amount:", A)
        
#Calculation for bond
else:
    P = float(input("Enter the present value of the house:"))
    
    i = (float(input("Enter interest rate:"))/100)/12                  #Calulated by dividing annual interest by 12
    
    n = int(input("Enter the number of months you plan to take to repay the bond."))
    
    bond_repayment = (i*P)/(1-math.pow((1 + i),(-n)))
    
    print("Bond repayment:", bond_repayment)
            
                  
    
                    





