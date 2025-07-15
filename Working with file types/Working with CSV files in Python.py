'''
In this project, you will use Python to read a CSV file, process the data, and produce a result. In this exercise, you will calculate the price of products and save the information. You will also need to create a new CSV file that contains this processed data.

Project details:
Inputs:

A CSV file that contains the product names, prices, and quantities available.
Outputs:

Calculate the total price of the products by multiplying the price by the quantity and saving the result in a new CSV file.
Create a new CSV file with four columns: product name, price, quantity, and total price.
Project steps:
Read data from the CSV file.
Calculate the total price of the products.
Save the processed data in a new CSV file.
'''
import csv

# File paths
input_file = 'products.csv'
output_file = 'processed_products.csv'

# List to store processed data
processed_data = []

# Step 1: Read data from CSV file
with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        name = row['product_name']
        price = float(row['price'])
        quantity = int(row['quantity'])
        total_price = price * quantity
        
        # Add processed row to list
        processed_data.append({
            'product_name': name,
            'price': price,
            'quantity': quantity,
            'total_price': total_price
        })

# Step 2: Write data to a new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['product_name', 'price', 'quantity', 'total_price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in processed_data:
        writer.writerow(row)

print("✅ Data processed and saved to 'processed_products.csv'")

