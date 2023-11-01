number = int(input("введите ваше число"))
sum = 0
if number % 2 == 0:
    while number > 0:
        sum += number % 10
        number = number // 10
    if sum % 3 == 0:
        print("число делиться на 6")
else:
    print("число не делиться на 6")