example = []
b = ""
while True:
    if "end" in example:
        print("конец")
        break

    b = input("ваша игра")
    example.append(b)
    example.sort()
