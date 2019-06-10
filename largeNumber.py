n = 123456789123456789
result = []
while n != 0:
    n, d = divmod(n, 10)
    result.append(int(d))
result.reverse()
print (result)