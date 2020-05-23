lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis2 = [1, 2, 3, 4, "yep"]

# print(lis[0])

num = int(input())

for element in lis:
    if element <= num:
        print(element)

print([output for output in lis if output <= num])