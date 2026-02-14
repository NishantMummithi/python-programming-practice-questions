marks=int(input("Enter your marks:"))
if marks==100:
    print("Outstanding")
elif marks>=90:
    print("Excellent")
elif marks>=80:
    print("Very good")
elif marks>=60:
    print("Average")
elif 50<=marks<40:
    print("Satisfactory")
elif marks>=35:
    print("Pass")
else:
    print("Fail")
