total_sum  = 0

for current_number in range(50, 10000):
    total_sum += current_number
    text = ''

    text += f"{current_number - 49}. "
    current_sum = 0

    for num in range(50, current_number + 1):
        current_sum += num
        text += f"{num}"
        if num != current_number:
            text += " + "

    print(f"{text} = {current_sum}")

    if total_sum > 1000:
        break
