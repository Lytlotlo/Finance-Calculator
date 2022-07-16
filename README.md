# Finance calculator.

This program is a finance calculator. It allows a user to access two types of calculators, an investment calculator 
and a home loan calculator.

The investment calculator calculates simple and compound interest.To calculate the simple and compound their formulas
are used.
_Simple intrest: A=P(1+r*t).
Compound intrest: A=P(math.pow((1+r),t))_
The calculator gets the formula values r(interest), P(Principal amount) and t(time/number of years the money is 
invested for) from user input and returns A(the amount of simple or compound interest that has been applied).

The home loan repayment calculator calculates the amount that a person needs to be repaid on a home loan each month.
The formula _repayment = x = (i.P)/(1 - (1+i)^(-n))_ is used. The calculator gets the formula values P(present value 
of the house), i(The monthly interestrate) and n(number of months which the bond will be repaid) from user input then
reutrns the calculated value.

This program has the math module imported and the program was created using python.
