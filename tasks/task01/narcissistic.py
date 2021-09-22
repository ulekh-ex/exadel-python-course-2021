def get_num_digits(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10

    return digits


def is_narcissisric(num):
    digits = get_num_digits(num)
    count, sum = len(digits), 0
    for d in digits:
        sum += d ** count

    return sum == num


for k in range(1, 1001):
    if (is_narcissisric(k)):
        print(f'{k} is narcisstic number')

