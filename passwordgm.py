# ==========================================
# # INPUT
# ==========================================
import datetime

character = "!@#$%^&"
# Obtiene el mes actual en inglés y minúsculas de forma dinámica
month = datetime.datetime.now().strftime("%B").lower() 

unlocked = 1

# ==========================================
# # PROCESS
# ==========================================
while True:
    # Siempre se solicita la contraseña en cada iteración para evaluar las reglas activas
    password = input("Ingresa tu contraseña: ")
    errors = ""
    
    # rule 1: Longitud mínima
    if unlocked >= 1:
        if len(password) < 8:
            errors = errors + "Your password must be at least 8 characters.\n"
            
    # rule 2: Al menos una mayúscula
    if unlocked >= 2:
        if password == password.lower():
            errors = errors + "Add at least one uppercase letter.\n"
            
    # rule 3: Al menos una minúscula
    if unlocked >= 3:
        if password == password.upper():
            errors = errors + "Add at least one lowercase letter.\n"
            
    # rule 4: Al menos un número
    if unlocked >= 4:
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
        if has_digit == False:
            errors = errors + "Add at least one number.\n"
            
    # rule 5: Al menos un carácter especial
    if unlocked >= 5:
        has_special = False
        for char in password:
            if char in character:
                has_special = True
        if has_special == False:
            errors = errors + "Add at least one special character (!@#$%^&).\n"
            
    # rule 6: La suma de los dígitos debe ser 25
    if unlocked >= 6:
        digit_sum = 0
        for char in password:
            if char.isdigit():
                digit_sum = digit_sum + int(char)
        if digit_sum != 25:
            errors = errors + "The digits in your password must add up to 25.\n"
            
    # rule 7: Longitud total debe ser número primo
    if unlocked >= 7:
        length = len(password)
        is_prime = True
        if length < 2:
            is_prime = False
        else:
            divisor = 2
            while divisor < length:
                if length % divisor == 0:
                    is_prime = False
                divisor = divisor + 1
        if is_prime == False:
            errors = errors + "Your password length must be a prime number.\n"
            
    # rule 8: Incluir el mes actual en minúsculas
    if unlocked >= 8:
        if month not in password:
            errors = errors + "Your password must include the current month in lowercase.\n"

    # ==========================================
    # # OUTPUT
    # ==========================================
    if errors == "":
        if unlocked < 8:
            unlocked = unlocked + 1
            print(f"Rule passed! Level {unlocked} unlocked. Try adding the new requirement.")
        else:
            print("Congrats! Your password is fully valid.")
            break
    else:
        print("\nTo fix:")
        print(errors)