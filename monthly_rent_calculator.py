# Take inputs for rent and the electric and utility bills
rent_input = input("Enter total rent payment: ")
duke_input = input("Enter Duke payment: ")
# internet_input = input("Enter internet payment: ") 
pet_fee = 35.00

rent = float(rent_input)
duke = float(duke_input)
# internet = float(internet_input)
internet = 0
# rent += duke
# rent += internet
# print(f"Rent is {rent}")

# Create two variables, AJ_payment and Joel_payment
AJ_rent = 0.00
Joel_rent= 0.00
Ben_rent= 0.00

# Perform calculations
# Split bills
# rent -= pet_fee
# rent_split = round((rent/3), 2)
# duke_split = round((duke/3), 2)
rent_split = (rent/3)
duke_split = (duke/3)
internet_split = (internet/3)

AJ_rent += rent_split
Joel_rent += rent_split
Ben_rent += rent_split
print(f"The monthly rent payment is ${rent}.")
print(f"The rent payment split is ${rent_split}.")
print(f"The Duke bill is ${duke}. Split three ways, that's ${round((duke/3), 2)}.")
print(f"The internet bill is ${internet}. Split three ways, that's ${round((internet/3), 2)}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Subtract $35 from rent for pet fee to be added onto AJ
Joel_rent -= (round((pet_fee/2),2))
Ben_rent -= (round((pet_fee/2),2))
AJ_rent += pet_fee
print(f"Adding {pet_fee} to AJ's payment for monthly pet rent...")

# print(f"Subtracting {pet_fee} from Joel's and Ben's payments and adding {pet_fee} to AJ's payment for pet fees...")

Joel_rent += duke_split
Ben_rent += duke_split
AJ_rent -= (duke_split * 2) # AJ already paid Duke, so 2/3 of the payment is rebalanced to him.

Joel_rent -= internet_split # Joel already paid the internet bill, so 2/3 of the payment is rebalanced to him.
Ben_rent += internet_split
AJ_rent += internet_split

if AJ_rent + Joel_rent + Ben_rent == rent:
    print(f"The sum of all three payments equals this month's rental payment of ${rent}. Calculations are correct")
else:
    print(f"Something's not adding up. {round(AJ_rent, 2)} + {round(Joel_rent, 2)} + {round(Ben_rent, 2)} is {(AJ_rent + Joel_rent + Ben_rent)}, not {rent}.")
    
print(f"AJ's payment for the month is ${round(AJ_rent, 2)}.")
print(f"Joel's payment for the month is ${round(Joel_rent, 2)}.")
print(f"Ben's payment for the month is ${round(Ben_rent, 2)}.")

input('Press ENTER to exit')