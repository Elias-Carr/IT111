# Inputs   
customerName = input("Please enter your name: ")
amountInput = input("Please enter the amount of your purchase: ")

# Format
amountPurchase = float(amountInput)

# Calculate Tax
amountTax = amountPurchase * 0.1
amountTotal = amountPurchase + amountTax

# Prints
print("Hello " + customerName + ", here is your sales receipt:")
print("Subtotal = $ " + format(amountPurchase, ',.2f'))
print("     Tax = $   " + format(amountTax, ',.2f'))
print("             --------")
print("   Total = $ " + format(amountTotal, ',.2f'))
