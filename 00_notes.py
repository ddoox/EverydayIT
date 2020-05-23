#indexing

reverse = [1, 2, 3]
reverse = reverse[::-1]
print(reverse)

end = reverse[-1]
print(end)

#some fun
print([[number for number in reverse if number % 2 == 0]])

#uniq
a = [1, 1, 2, 2, 3, 3, 4, 4]
print(set(a))

#split + join
a = "lorem ipsum dolor sit amet"
a = a.split(" ")
print(a)
print("----join----".join(a))



