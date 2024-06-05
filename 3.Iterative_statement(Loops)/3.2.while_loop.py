num = int(input("Enter a number: "))
n = 1
while n<=num:
    print(n)
    n=n+1

# while-else:
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)    # 5

cn = 1
while cn < 4:
    print(cn)
    cn = cn+1
    if cn ==3:
        break

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1