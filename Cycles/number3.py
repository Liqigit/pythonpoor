forbiden = "=?*^$№@_"
login = input("введите логин")
a = 0
for i in forbiden:
    for b in login:
        if i == b:
            print("у вас есть запрещенные символ =="+i)
            break
        while a < 1:
            print("все гуд")
            a +=1