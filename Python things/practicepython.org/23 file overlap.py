primes = []
happy = []
with open("primenumbers.txt", "r") as primes_file:
    line = primes_file.readline()
    while line:
        primes.append(int(line))
        line = primes_file.readline()

with open("happynumbers.txt", "r") as happy_file:
    line = happy_file.readline()
    while line:
        happy.append(int(line))
        line = happy_file.readline()

overlap = [prime for prime in primes if prime in happy]

print(overlap)
