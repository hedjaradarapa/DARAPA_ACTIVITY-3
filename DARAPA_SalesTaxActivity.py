print("Sales Tax Calculate")
amount = float(input("Enter purchase amount:"))

calculate = amount * 0.06

tax = "{:.2f}".format(calculate)
print("Amount:" ,"Sales Tax:" ,"{:.2f}".format(calculate))