def checkValidPassword(password: str):
    previousDigit = 0
    for digit in password:
        digit = int(digit)
        if digit < previousDigit:
            return False
        else:
            previousDigit = digit

    for i in range(10):
        if str(i) + str(i) in password and not str(i) + str(i) + str(i) in password:
            return True

    return False


with open('data/data.txt') as data:
    passwordRange = list(map(int, data.readline().split('-')))

count = 0
for password in range(passwordRange[0], passwordRange[1] + 1):
    if checkValidPassword(str(password)):
        count += 1

print(count)
