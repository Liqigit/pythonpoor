numbers = input("введите ваш спискок").split()
if sorted(numbers) == numbers:
    print("все правильно")
else: print("вы дурачок")

print(sorted(numbers))
