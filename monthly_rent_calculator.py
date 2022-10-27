# Take inputs for rent and the electric and utility bills
rent_input = input("Enter total rent payment: ")
duke_input = input("Enter Duke payment: ")
internet_input = input("Enter internet payment: ")

rent = float(rent_input)
duke = float(duke_input)
internet = float(internet_input)

# Create two variables, AJ_payment and Joel_payment
AJ_rent = 0.00
Joel_rent= 0.00

# Perform calculations
# Halve bills
rent_halved = rent/2
AJ_rent += rent_halved
Joel_rent += rent_halved
print(f"The monthly rent payment is ${rent}.")
print(f"The rent payment halved is ${rent_halved}.")

# Subtract $40 from rent for pet fee to be added onto AJ
Joel_rent -= 40.00
AJ_rent += 40.00
print("Subtracting $40 from Joel's payment and adding $40 to AJ's payment for pet fees...")

# If - else statement to determine which difference gets added
if duke > internet:
    difference = duke - internet
    adjustment = difference / 2
    AJ_rent -= adjustment
    Joel_rent += adjustment
    print(f"The Duke Energy bill (${duke}) is larger than the internet bill (${internet}) this month.")
    print(f"Adjustment based on half the difference in utilities is {adjustment}.")
elif internet > duke:
    difference = internet - duke
    adjustment = difference / 2
    AJ_rent += adjustment
    Joel_rent -= adjustment
    print("The internet bill (${internet}) is larger than the Duke Energy bill (${duke}) this month.")
    print(f"Adjustment based on half the difference in utilities is {adjustment}.")
else:
    print("Duke and internet payments are the same. No adjustment made.")

if AJ_rent + Joel_rent == rent:
    print(f"AJ + Joel = $1249, calculations are correct")
else:
    print("Something's not adding up")
    
print(f"AJ's payment for the month is ${AJ_rent}.")
print(f"Joel's payment for the month is ${Joel_rent}.")

input('Press ENTER to exit')