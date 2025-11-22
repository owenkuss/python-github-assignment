#Greet the User
print("Welcome to my Python program!")

#Ask the User for Input (Weekly Savings)
money = input("How much money did you save this week?\n")

#Forcast Monthly Savings based on Weekly Savings
money = float(money)
monthly = money * 4

#Print forcasted Monthly Savings
print(f"You are on track to save ${monthly} this month.")

#Basic Error Handling
try:
    money = float(money)
except ValueError:
    print("Please enter a valid number.")
    exit()