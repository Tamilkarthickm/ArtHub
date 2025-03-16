#problem: You are given two lists of numbers and you need to find total of each of these list
tamil_total = [1000, 1850, 7850, 2025, 9696]
moni_total = [800, 600, 9000, 8655, 890]


def calculate_total(exp):
    """
    This function does addition of values from the list provided through arguments
    and it returns total value as an output
    """
    total = 0
    for item in exp:
        total = total + item
    return total


karthick_exp = calculate_total(tamil_total)
Moni_exp = calculate_total(moni_total)

print("Karthick's total expense is:", karthick_exp)
print("Moni's total expense is:", Moni_exp)


