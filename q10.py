
amount = float(input("Enter the total purchase amount: "))


if amount > 5000:
    discount_percent = 20
elif amount >= 2000:
    discount_percent = 10
else:
    discount_percent = 0


discount_amount = (amount * discount_percent) / 100
final_amount = amount - discount_amount


print(f"Original Amount: {amount}")
print(f"Discount Applied: {discount_percent}%")
print(f"Discount Value: {discount_amount}")
print(f"Final Amount to Pay: {final_amount}")
