list1 = [1, 2, 3, 4, 5]

print(*list1)
print(*list1, sep = '-')

list1.insert(len(list1), 6)
print(*list1, sep = '-')

list1.append (7)
print(*list1, sep = '-')

list1.extend([8,9,10])
print(*list1, sep = '-')


list1.pop(9)
print(*list1, sep = '-')

del list1[8]
print(*list1, sep = '-')
