name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
dbms = float(input("Enter DBMS marks: "))
java = float(input("Enter Java marks: "))
physics = float(input("Enter Physics marks: "))

total = maths + python + dbms + java + physics
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
