A = list(map(int, input().split()))
fife = A.count(5)
bob = fife
print("у вас всего: "+ str(bob) , "пятерок")
all = sum(A)
print((all/100)*fife)
