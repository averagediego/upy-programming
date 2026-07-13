# Problem 5: Shipping Cost Calculator

# PROCESS
total_shipping = 0.0

while True:
    # INPUT
    weight_input = input("Enter package weight in kg (or 'exit' to finish): ")
    if weight_input.lower() == "exit":
        break
    weight = float(weight_input)
    distance = float(input("Enter distance in km: "))

    # PROCESS
    if distance <= 100:
        cost = 50.00 if weight <= 5 else 80.00
    else:
        cost = 120.00 if weight <= 5 else 200.00

    total_shipping += cost

    # OUTPUT
    print(f"Shipping cost: ${cost:.2f} MXN")

# OUTPUT
print(f"Total: ${total_shipping:.2f} MXN")