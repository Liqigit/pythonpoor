a = float(input(""))
b = float(input(""))
c = float(input(""))
pay = sum([a,b,c])
if a < b and a <c:
    if b < c:
        print(pay/2)
    else: print("к оплате",pay)
elif a > b and a > c:
    if b > c:
        print(pay/3)
    else: print("к оплате", pay)
else: print("к оплате",pay)


