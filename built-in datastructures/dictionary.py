sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}

print(sample_dict[1])
sample_dict[2] = 'Milk'
print(sample_dict[2])


for x in sample_dict:
    print(x)

for x in sample_dict.items():
    print(x)

for x, y in sample_dict.items():
    print(y)
