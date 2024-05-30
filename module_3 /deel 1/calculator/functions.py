def addition(nummer1, nummer2):
    return nummer1 + nummer2

def subtraction(nummer1, nummer2):
    return nummer1 - nummer2

def multiplication(nummer1,nummer2):
    return nummer1 * nummer2

def division(nummer1,nummer2):
    if nummer2 == 0:
        raise ValueError("Kan niet delen door nul.")
    return nummer1 / nummer2