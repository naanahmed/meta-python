with open('newfile.txt', 'w') as file:
    file.writelines(["This is a new file.", "\nThis is the second line"])

with open('newfile.txt', 'a') as file:
    file.writelines(["\nThis is a new file.", "\nThis is the second line"])
