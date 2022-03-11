def sumOfDigits(number):
    assert number >= 0 and int(number) == number, "The Value must be integer and Greater than 0"
    if number == 0:
        return 0
    else:
        return (number % 10) + sumOfDigits(int(number/10))

print(sumOfDigits(1234))