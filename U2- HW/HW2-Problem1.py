# Problem 1: Grade Averaging System

# INPUT
grades = []
while True:
    entry = input("Enter grade (or 'done' to finish): ")
    if entry.lower() == "done":
        break
    grades.append(float(entry))

# PROCESS
if len(grades) == 0:
    average = None
    status = None
else:
    total = sum(grades)
    average = total / len(grades)
    if average >= 7.0:
        status = "Passed"
    else:
        status = "Failed"

# OUTPUT
if len(grades) == 0:
    print("No grades entered. Please enter at least one grade.")
else:
    print(f"Average: {average:.2f} — {status}")