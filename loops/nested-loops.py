import time

start_time = time.time();

integers = [0,1,2,3,4,5,6,7,8,9]


#print all  numbers less than 10 000 000
for i in integers:
    for j in integers:
        for k in integers:
            for l in integers:
                for m in integers:
                    for n in integers:
                        print (i,j,k,l,m,n)

print(round((time.time() - start_time), 2))
