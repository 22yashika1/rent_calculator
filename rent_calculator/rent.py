rent = int(input("enter the flat rent = "))
food = int(input("enter the ordered food amount : "))
electricity_spend = int(input("enter the toatl electricity spent : "))
electricity_charge = int(input("enter the charge per unit : "))
persons = int(input("enter the number of persons living in flat : "))
#now add the total of all of the above and divide it into the persons
electricity = electricity_spend * electricity_charge
total = (food + rent + electricity) // persons
print("each person has to pay = ", total)