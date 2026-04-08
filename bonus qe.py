


units = float(input("Enter the number of units consumed: "))

bill = 0


if units <= 100:
    
    bill = units * 10
elif units <= 200:
    
    bill = (100 * 10) + ((units - 100) * 15)
else:
    
    bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)


print(f"Total units consumed: {units}")
print(f"Total Electricity Bill: Rs. {bill}")
