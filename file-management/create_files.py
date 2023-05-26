# with open('newfile.txt', 'w') as file:
#     file.writelines(["This is a new file.", "\nThis is the second line"])

try:
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(["\nThis is a new file.", "\nThis is the second line"])

except FileNotFoundError as e:
    print("File not found", e)
