# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price   # return original price if discount < 20%


# Main program
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. Final price: {final_price}")
else:
    print(f"Discount applied! Final price: {final_price}")
