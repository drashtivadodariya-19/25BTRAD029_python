sales = {}

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter product price: "))

    sales[name] = {
        "quantity": quantity,
        "price": price
    }

total_sales = 0

print("\n--- SALES REPORT ---")

for name, details in sales.items():
    revenue = details["quantity"] * details["price"]
    total_sales += revenue

    print("Product:", name)
    print("Quantity:", details["quantity"])
    print("Revenue:", revenue)

highest = max(sales, key=lambda x: sales[x]["quantity"])

print("\nTotal Sales:", total_sales)
print("Highest Selling Product:", highest)
