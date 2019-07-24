# -*- utf-8 -*-

# Problem sets 1 part a of MIT60001F16

# input:
annual_salary = int(input("Enter your annual salary:​ "))  # such as 120000
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:​ "))  # such as 0.1
total_cost = int(input("Enter the cost of your dream home:​ "))  # such as 1000000
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:"))

# assume:
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12.0

down_payment = total_cost * portion_down_payment
months = 0
while current_savings - down_payment < 0:
    current_savings += monthly_salary * portion_saved + \
                      current_savings * r / 12
    months += 1
    if months % 6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)

print("Number of months:​", months)
