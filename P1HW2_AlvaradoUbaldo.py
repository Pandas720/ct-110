# Ubaldo Alvarado
#June 16, 2025
#P1HW2
#Program that does basic math on numbers that are inputed

print("This program calculates and displays travel expenses")

print("Enter Bedget:", end=" ")
Budget=int(input())

print("Enter your travel destination:", end=" ")
Destination=input()

print("How mcuh do you think you will spend on gas?", end=" ")
Gas=int(input())

print("Approximately, how much will you need for accomidation/hotel?", end=" ")
Hotel=int(input())

print("Last, how much do you need for food?", end=" ")
Food=int(input())

print("------Travel Expenses-----")

print("Location:", Destination)
print("Initial Budget:", Budget)
print("Fuel:", Gas)
print("Accomodation:", Hotel)
print("Food:", Food)

Balance=Budget-Gas-Hotel-Food
print("Remaining Balance:", Balance)
