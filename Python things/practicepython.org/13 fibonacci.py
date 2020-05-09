number = 19

swap = [1, 1, 2]
fib = []

if number == 1:
    fib.append(1)
    print(fib)
elif number == 2:
    fib.append(1)
    fib.append(1)
    print(fib)
else:
    fib.append(1)
    fib.append(1)
    fib.append(2)
    for i in range(0, number-3):
        swap[0] = swap[1]
        swap[1] = swap[2]
        swap[2] = swap[0] + swap[1]
        fib.append(swap[2])
    print(fib)

