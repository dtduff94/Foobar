def decimalToBase(decimalNumber, b):
    number = int(decimalNumber)
    ints = []
    while number >= n:
        r = number % b
        ints.append(str(r))
        number = (number - r) // b
    ints.append(str(number))
    ints.reverse()
    return ''.join(ints)

def baseToDecimal(baseNumber, b):
    ints = list(baseNumber)
    ints.reverse()
    decimalNumber = 0
    for index, num in enumerate(ints):
        decimalNumber += int(num) * (b ** index)
    return str(decimalNumber)
