num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

counter = 0
for idx, i in enumerate(num_list):
    counter +=1
    if i > 45 :
        print ("Over 45: ", idx, i, end= ",")

    elif i == 36:
        print ("Number found at postion: ", idx)
        break
    else:
        print ("Under 45: ", str(idx) + ":", str(i), end= ",")

print (counter)
