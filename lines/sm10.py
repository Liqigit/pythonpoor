num = "+7 (812) 134-12-324"
tell = ("1234567890")
res = "+"

for i in num:
    if i in tell:
        res += i
print(res)