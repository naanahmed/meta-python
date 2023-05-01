bill_total = 500
discount1 = 20
discount2 = 50

if bill_total > 200 and bill_total < 500:
    print("Bill is greater than 200!")
    bill_total = bill_total - discount1

elif bill_total > 100 :
    print ("Bill is greater than 500")
    bill_total = bill_total - discount2

else:
    print("Bill is less than 200")

print ("Total Bill: " + str(bill_total))
