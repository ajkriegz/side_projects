# Take inputs for rent and the electric and utility bills
rent_input = input("Enter total rent payment: ")
duke_input = input("Enter Duke payment: ")
# internet_input = input("Enter internet payment: ") # Internet is now included in rent

rent = float(rent_input)
duke = float(duke_input)
pet_fee = 45.00
#internet = float(internet_input)
internet = 0

# Create two variables, AJ_payment and Joel_payment
AJ_rent = 0.00
Joel_rent= 0.00

# Perform calculations
# Halve bills
rent_halved = rent/2
duke_halved = (duke/2)
AJ_rent += rent_halved
Joel_rent += rent_halved
print(f"The monthly rent payment is ${rent}.")
print(f"The rent payment halved is ${rent_halved}.")
print(f"The Duke bill is ${duke}.")
#print(f"The internet bill is ${internet}.")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Subtract $45 from rent for pet fee to be added onto AJ
Joel_rent -= pet_fee
AJ_rent += pet_fee
print(f"Subtracting {pet_fee} from Joel's payment and adding {pet_fee} to AJ's payment for pet fees...")

Joel_rent += duke_halved
AJ_rent -= duke_halved

# # If - else statement to determine which difference gets added
# if duke > internet:
#     difference = duke - internet
#     adjustment = difference / 2
#     AJ_rent -= adjustment
#     Joel_rent += adjustment
#     print(f"The Duke Energy bill (${duke}) is larger than the internet bill (${internet}) this month.")
#     print(f"Adjustment based on half the difference in utilities is {adjustment}.")
# elif internet > duke:
#     difference = internet - duke
#     adjustment = difference / 2
#     AJ_rent += adjustment
#     Joel_rent -= adjustment
#     print("The internet bill (${internet}) is larger than the Duke Energy bill (${duke}) this month.")
#     print(f"Adjustment based on half the difference in utilities is {adjustment}.")
# else:
#     print("Duke and internet payments are the same. No adjustment made.")

if AJ_rent + Joel_rent == rent:
    print(f"AJ's payment + Joel's payment = ${rent}, calculations are correct")
else:
    print("Something's not adding up")
    
print(f"AJ's payment for the month is ${AJ_rent}.")
print(f"Joel's payment for the month is ${Joel_rent}.")

input('Press ENTER to exit')