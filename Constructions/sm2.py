pay = float(input("price in your order"))
time = int(input("time"))
cooficient = 1
if time <=22 and time >= 10:
    if 10 <= time <= 12:
        cooficient = 0.5
        print(pay * cooficient)
    elif 10 <= time <= 22:
        cooficient = 0.25
        print(pay * cooficient)
    else: print(pay)
else: print("вы видимо без личной жизни, магазин закрыт")