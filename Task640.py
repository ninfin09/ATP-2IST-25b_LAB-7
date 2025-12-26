def sum_three(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

try:
    nums = input("Введіть три числа саме через пробіл: ").split()
    x, y, z = map(int, nums)

    print(sum_three(x, y, z))
except:
    print("Будь ласка, введіть саме три цілих числа.")