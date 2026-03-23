print("  \n----FAMILY DETAILS----\n  ")
N=int(input("Enter no of family numbers:"))
input("Enter Account Holder name:")
DOB=int(input("Enter date of birth:"))
age1=int(input("Enter your age:"))
input("Enter mother name:")
DOB1=int(input("Enter date of birth:"))
age2=int(input("Enter mother's age:"))
input("Enter father's name:")
DOB2=int(input("Enter date of birth:"))
age3=int(input("Enter father's age:"))
input("Enter your sibling's age:")
DOB3=int(input("Enter date of birth:"))
age4=int(input("Enter sibling's age:"))
A=int(input("Enter no of Two-Wheeler vehicles:"))
B=int(input("Enter no of Three-Wheeler vehicles:"))
C=int(input("Enter no of Four-Wheeler vehicles:"))
D=int(input("Enter no of children:"))
E=int(input("Enter no of Adults:"))
Income=int(input("Enter Family income:"))
print("  \n----FAMILY EXPENSES----\n  ")
Expenses={
    "Carrer Expenses":int(input("Enter Carrer Expenses:")),
    "Housing Expenses":int(input("Enter Housing Expenses:")),
    "Food Expenses":int(input("Enter Food Expenses:")),
    "Medical Expenses":int(input("Enter Medical Expenses:")),
    "Travel Expenses":int(input("Enter Travel Expenses:")),
    "Electrical Expenses":int(input("Enter Electrical Expenses:")),
    "Water Expenses":int(input("Enter Water Expenses:")),
    "Electricity Expenses":int(input("Enter Electricity Expenses:")),
    "Gas Expenses":int(input("Enter Gas Expenses:")),
    "Telephone Expenses":int(input("Enter Telephone Expenses:")),
    "Internet Expenses":int(input("Enter Internet Expenses:")),
    "Gifts Expenses":int(input("Enter Gifts Expenses:")),
    "Donations Expenses":int(input("Enter Donations Expenses:")),
    "Charity Expenses":int(input("Enter Charity Expenses:")),
    "Savings Expenses":int(input("Enter Savings Expenses:")),
    "Other Expenses":int(input("Enter other Expenses:"))
    }
print("  \n----FINANCIAL DETAILS----\n  ")
total_spent=sum(Expenses.values())
Remaining_Balance=Income-total_spent
print("total expenses:",total_spent)
print("Remaining expenses:",Remaining_Balance)
print("  \n----PERCENTAGE EXPENDITURE----\n  ")
Carrer_Expenses=(Expenses.Carrer_Expenses/Income*100)
print("% of Carrer Expenses:",Carrer_Expenses)
Housing_Expenses=(Expenses.Housing_Expenses/Income*100)
print("% of Housing Expenses:",Housing_Expenses)
Food_Expenses=(Expenses.Food_Expenses/Income*100)
print("% of Food Expenses:",Food_Expenses)
Medical_Expenses=(Expenses.Medical_Expenses/Income*100)
print("% of Medical Expenses:",Medical_Expenses)
Travel_Expenses=(Expenses.Travel_Expenses/Income*100)
print("% of Travel Expenses:",Travel_Expenses)
Electrical_Expenses=(Expenses.Electrical_Expenses/Income*100)
print("% of Electrical Expenses:",Electrical_Expenses)
Water_Expenses=(Expenses.Water_Expenses/Income*100)
print("% of Water Expenses:",Water_Expenses)
Electricity_Expenses=(Expenses.Electricity_Expenses/Income*100)
print("% of Electricity Expenses:",Electricity_Expenses)
Gas_Expenses=(Expenses.Gas_Expenses/Income*100)
print("% of Gas Expenses:",Gas_Expenses)
Telephone_Expenses=(Expenses.Telephone_Expenses/Income*100)
print("% of Telephone Expenses:",Telephone_Expenses)
Internet_Expenses=(Expenses.Internet_Expenses/Income*100)
print("% of Internet Expenses:",Internet_Expenses)
Gifts_Expenses=(Expenses.Gifts_Expenses/Income*100)
print("% of Gifts Expenses:",Gifts_Expenses)
Donations_Expenses=(Expenses.Donations_Expenses/Income*100)
print("% of Donations Expenses:",Donations_Expenses)
Charity_Expenses=(Expenses.Charity_Expenses/Income*100)
print("% of Charity Expenses:",Charity_Expenses)
Savings_Expenses=(Expenses.Savings_Expenses/Income*100)
print("% of Savings Expenses:",Savings_Expenses)
Other_Expenses=(Expenses.Other_Expenses/Income*100)
print("% of Other Expenses:",Other_Expenses)
print("  \n----FAMILY FINANCIAL STATUS----\n  ")
if total_spent<Income:
  print("Sufficient usage of Money,HAPPY FAMILY")
else:
  print("Insufficient usage of Money,UNHAPPY FAMILY")
