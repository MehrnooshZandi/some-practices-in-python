'''
A store offers special discounts to its customers. The discount rules are as follows:

If the purchase amount is more than 50,000 Tomans, a 20% discount is applied.

If the purchase amount is between 20,000 and 50,000 Tomans, a 10% discount is applied.

If the purchase amount is less than 20,000 Tomans, no discount is applied.

Write a program that receives the purchase amount from the user and displays the final amount.

Input 1:

55,000

Output 1:

44,000
'''
# Get the purchase amount from the user
purchase_amount = int(input())

# Determine the discount rate based on the purchase amount
if purchase_amount > 50000:
    discount = 0.20
elif purchase_amount >= 20000:
    discount = 0.10
else:
    discount = 0.0

# Calculate the final amount after applying the discount
final_amount = int(purchase_amount * (1 - discount))

# Print the final amount to be paid
print(final_amount)

