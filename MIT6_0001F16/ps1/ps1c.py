# -*- utf-8 -*-

# Problem sets 1 part C of MIT60001F16

# input:
annual_salary = int(input("Enter your annual salary:​ "))  # such as 120000

# assume:
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
r = 0.04
semi_annual_raise = 0.07
monthly_salary = annual_salary / 12.0

down_payment = total_cost * portion_down_payment
months = 36
portion_saved_low = 0
portion_saved_high = 10000
for m in range(months):
        portion_saved = portion_saved_high
        current_savings += monthly_salary * portion_saved / 10000 + \
                           current_savings * r / 12
        if (m+1) % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
distance = current_savings - down_payment
if distance < 0:
    print("It is not possible to pay the down payment in three years.")
else:
    steps_of_bisection_search = 0
    while not 0 <= distance < 100:
        portion_saved = (portion_saved_low + portion_saved_high) // 2
        current_savings = 0
        monthly_salary = annual_salary / 12.0
        for m in range(months):
            current_savings += monthly_salary * portion_saved / 10000 + \
                               current_savings * r / 12
            if (m+1) % 6 == 0:
                monthly_salary = monthly_salary * (1 + semi_annual_raise)
        distance = current_savings - down_payment
        if distance < 0:
            portion_saved_low = portion_saved
        else:
            portion_saved_high = portion_saved
        steps_of_bisection_search += 1
    print("Best savings rate:​​", portion_saved/10000.0)
    print("Steps in bisection search:", steps_of_bisection_search)
