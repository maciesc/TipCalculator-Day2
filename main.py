print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
percentage = float(input("How much tip you would like to give? %"))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill + bill * percentage / 100
bill_with_tip_per_person = bill_with_tip / people
final_amount = "{:.2f}".format(bill_with_tip_per_person)
print(f"Every person should pay ${final_amount}")