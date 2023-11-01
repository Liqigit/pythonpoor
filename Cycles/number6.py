a = int(input("ваша сумма?: "))
if a % 2 != 0:
    b = a / 100 * 15
    print("ваша скидка 15%\nк оплате: ", a - b)
elif a % 2 == 0:
    while a % 2 == 0:
        a = a / 2
    print("к оплате: ", a)
