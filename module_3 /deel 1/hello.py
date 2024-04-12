def hello_functie(num):
    result = ""
    for i in range(1, num + 1):
        result += f"Hello from function town {i}!\n"
    return result

print(hello_functie(3))
print(hello_functie(7))