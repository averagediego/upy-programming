# Problem 2: BMI Calculator

while True:
    # INPUT
    weight_input = input("Enter weight in kg (or 'exit' to finish): ")
    if weight_input.lower() == "exit":
        break
    weight = float(weight_input)
    height = float(input("Enter height in m: "))

    # PROCESS
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # OUTPUT
    print(f"BMI: {bmi:.2f} — {category}")