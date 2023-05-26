with open('file.txt', 'r') as f:
    print(f.read())

with open('file.txt', 'r') as f:
    print(f.read(5))

with open('file.txt', 'r') as f:
    print(f.readline())

with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines[1])

with open('file.txt', 'r') as f:
    for x in f:
        print(x)
