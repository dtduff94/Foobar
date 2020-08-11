def decimalToBase(decimalNumber, b):
    number = int(decimalNumber)
    ints = []
    while number >= b:
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

def solution(n, b):
    k = len(n)
    m = n
    usedIDS = []
    while m not in usedIDS:
        usedIDS.append(m)
        sortedInts = sorted(m)
        ascendingInts = ''.join(sortedInts)
        sortedInts.reverse() 
        descendingInts = ''.join(sortedInts)
             
        subtractValue = int(baseToDecimal(descendingInts, b)) - int(baseToDecimal(ascendingInts, b))
        m = decimalToBase(str(subtractValue), b)
        
        m = (k - len(m)) * '0' + m
    return len(usedIDS) - usedIDS.index(m)
