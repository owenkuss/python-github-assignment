print("Welcome to my Python program!")

money = input("How much money did you save this week?)

money = float(money)
monthly = money * 4

print(f"You are on track to save ${monthly} this month.")

try:
    money = float(money)
except ValueError:
    print("Please enter a valid number.")
    exit()