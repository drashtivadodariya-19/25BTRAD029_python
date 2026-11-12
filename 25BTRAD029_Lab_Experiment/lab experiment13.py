import csv
import os

path = os.path.join(os.path.dirname(__file__), "employees.csv")

file = open(path, "r")
reader = csv.reader(file)

next(reader)

total = 0

print("\n--- PAYROLL REPORT ---")

for row in reader:
    name = row[0]
    basic = float(row[1])
    hra = float(row[2])
    da = float(row[3])
    deduction = float(row[4])

    gross = basic + hra + da
    net = gross - deduction

    total += net

    print("\nEmployee:", name)
    print("Gross Salary:", gross)
    print("Deduction:", deduction)
    print("Net Salary:", net)

file.close()

print("\nTotal Payroll:", total)
