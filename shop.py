print(f'\nEXAMPLE:\nEnter the product price: 2\nEnter the product weight: 3\nEnter the amount of money the buyer has: 10\nChange: 4\n')

product_price = int(input('Enter the product price: '))
product_weight = int(input('Enter the product weight: '))
cash_of_buyer = int(input('Enter the amount of money the buyer has: '))

print(f'Change: {cash_of_buyer - product_price * product_weight}')