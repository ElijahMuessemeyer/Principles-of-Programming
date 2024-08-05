meal_price = float(input("Enter the price of the meal: "))

tip = meal_price * 0.18
sales_tax = meal_price * 0.07
total_price = meal_price + tip + sales_tax

print("The 18% tip is", "${:.2f}".format(tip))
print("The 7% sales tax is", "${:.2f}".format(sales_tax))
print("The total price of the meal is ", "${:.2f}".format(total_price))