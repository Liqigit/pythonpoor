while True:
    for i in range(3):
        a = input("что вы хотите").lower()
        if a == 'game':
            b = int(input("введите число"))
            if b == 5:
                print("we win")
                break
            else: print("вы проиграли")
        elif a == "off":
            print('работа завершается')
            break
        else: print("а что вы вообще хотите")
    break