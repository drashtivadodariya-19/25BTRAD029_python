a = float(input("Enter first number: ")) 
b = float(input("Enter second number: ")) 
print("1.Add  2.Subtract  3.Multiply  4.Divide") 
choice = int(input("Enter choice: ")) 
if choice == 1: 
    print("Result:", a + b) 
elif choice == 2: 
    print("Result:", a - b) 
elif choice == 3: 
    print("Result:", a * b) 
elif choice == 4: 
    print("Result:", a / b) 
else: 
    print("Invalid choice") 
r = float(input("Enter radius: "))   #circle 
area = 3.14 * r * r 
print("Area of circle:", area) 
