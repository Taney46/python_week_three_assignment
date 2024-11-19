def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

try:
    price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the percentage discount: "))

    
    final_price = calculate_discount(price, discount_percentage)
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")