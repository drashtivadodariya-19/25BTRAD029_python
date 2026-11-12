num = int(input("Enter a number: "))

# Prime Number
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


# Factorial
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)
