# Problem 3: Water Bill Calculator

# PROCESS
total_bill = 0.0

while True:
    # INPUT
    entry = input("Enter m3 consumed (or 'exit' to finish): ")
    if entry.lower() == "exit":
        break
    m3_consumed = float(entry)

    # PROCESS
    if m3_consumed <= 10:
        rate = 8.00
    elif m3_consumed <= 20:
        rate = 12.00
    else:
        rate = 18.00

    charge = m3_consumed * rate
    total_bill += charge

    # OUTPUT
    print(f"Month charge: ${charge:.2f} MXN")

# OUTPUT
print(f"Total: ${total_bill:.2f} MXN")