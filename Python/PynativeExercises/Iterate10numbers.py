
PreviousNumber = 0
print("Printing current and previous number sum in a range 10")

for i in range(1,11):
    Sum=i+PreviousNumber
    print ("current number",i,"Previous Number",PreviousNumber ,"Sum:", Sum)
    PreviousNumber=i
    