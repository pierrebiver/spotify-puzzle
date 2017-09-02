def number_to_binary(number: int):
    binary = []
    while number != 0:
        binary.append(number % 2)
        number = number // 2

    binary.reverse()
    return int(''.join(str(i) for i in binary))


def binary_to_number(binary_number: int):
    decimal = 0
    for i in str(binary_number):
        if i == '1':
            decimal = decimal * 2 + 1
        else:
            decimal = decimal * 2

    return decimal


def reverse_binary_number(number):
    binary = number_to_binary(number)
    reverse_binary = str(binary)[::-1]
    return binary_to_number(int(reverse_binary))
