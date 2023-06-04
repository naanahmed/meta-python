file = open('file1.txt', mode='r')

data = file.readline()
print (data)

file.close()


########################################################################

with open('file2.txt', mode='r') as file:
    data = file.readline()
    print(data)
