product = []
quantity = []
price = []
total = []

counter = 1
overAllTotal = 0
transactionCount = 1
buyMore = "YES"
while buyMore == "YES":

    product_name = str(input("What are you buying: ").capitalize())
    product.append(product_name)

    quantity_of_product = int(input("Quantity: "))
    quantity.append(quantity_of_product)

    price_of_product = int(input("Price: "))
    price.append(price_of_product)

    total_per_product = quantity_of_product * price_of_product
    total.append(total_per_product)
    overAllTotal += total_per_product

    buyMore = str(input("Would you like to purchase more stuff?(yes/no) ").upper())
    if buyMore == "NO":
        break
    else:
        transactionCount += 1

    counter += 1

print()
print()

design = "*"
print(design * 50)
print("     Florence & Sons Group Of Company")
print("     312, Herbert Macaulay Way, Sabo, Yaba")
print("     Tel:  07013780556")
print(design * 50)
print()
print("     Product    Quantity    Price    Total")
print(design * 50)
print()

loop = 0
while loop < transactionCount:
    print(f'{product[loop]:>12s} {quantity[loop]:10d} {price[loop]:>9d} {total[loop]:>8d}')
    #print("     ", product[loop], "      ", quantity[loop], "      ", price[loop], "    ", total[loop])
    loop += 1

print(design * 50)
print(f'{"Total: ":>36s} {overAllTotal:>5d}')
print(design * 50)
print("         THANK YOU FOR YOUR PATRONAGE!!!        ")
print(design * 50)
