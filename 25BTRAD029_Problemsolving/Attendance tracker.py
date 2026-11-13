attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ").upper()
    attendance[name] = [status]

print("\n--- ATTENDANCE RECORDS ---")

for name, records in attendance.items():
    print(name, ":", records)

print("\n--- ATTENDANCE PERCENTAGE ---")

for name, records in attendance.items():
    present = records.count("P")
    total = len(records)
    percentage = (present / total) * 100

    print(name, ":", percentage, "%")

threshold = float(input("\nEnter attendance threshold: "))

print("\nStudents below threshold:")

for name, records in attendance.items():
    percentage = (records.count("P") / len(records)) * 100

    if percentage < threshold:
        print(name)
