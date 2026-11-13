name=input("Customer Name:")

product1= input("Product 1 :")
price1=float(input("Price : "))

product2= input("Product 2 :")
price2=float(input("Price : "))

product3= input("Product 3 :")
price3=float(input("Price : "))


subtotal = (price1+price2+price3)
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.00
Discount = (subtotal * discount_rate)
Final_Total = (subtotal-Discount)


print(f"Subtotal:{subtotal}")
print(f"Discount:{Discount}")
print(f"Final Total: {Final_Total}")
