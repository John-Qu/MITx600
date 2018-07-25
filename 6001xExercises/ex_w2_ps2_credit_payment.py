# MITx 6.001x week 2 problem set 2: credit card payment.
# Created by john at 2018-05-07.
# Checked with text case and passed grader.

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate, tot_month = 12):
    """to calculate the credit card balance after one year if a person only pays the minimum monthly payment
    required by the credit card company each month.
    :param balance: float, the outstanding balance on the credit card
    :param annualInterestRate: float, annual interest rate as a decimal
    :param monthlyPaymentRate: float, minimum monthly payment rate as a decimal
    :param tot_month: int, the paying periods
    :return: remaining_balance at the end of tot_month: float
    """
    monthly_interest_rate = annualInterestRate / 12
    balances = [balance]
    for m in range(1, tot_month+1):
        min_monthly_payment = monthlyPaymentRate * balances[-1]
        unpaid_balance = balances[-1] - min_monthly_payment
        new_balance = unpaid_balance + unpaid_balance*monthly_interest_rate
        balances.append(new_balance)
    return balances[-1]


def test_remaining_balance(balance, annualInterestRate, monthlyPaymentRate, tot_month = 12):
    rb = remaining_balance(balance, annualInterestRate, monthlyPaymentRate, tot_month = 12)
    print("Remaining balance:", round(rb, 2))

# test_remaining_balance(balance, annualInterestRate, monthlyPaymentRate, tot_month = 12)


def remaining_balance2(balance, annualInterestRate, monthly_payment, tot_month = 12):
    """to calculate the credit card balance after one year if a person pays a fixed monthly payment.
    :param balance: float, the outstanding balance on the credit card
    :param annualInterestRate: float, annual interest rate as a decimal
    :param monthly_payment: float, monthly payment as a decimal
    :param tot_month: int, the paying periods
    :return: remaining_balance at the end of tot_month: float
    """
    monthly_interest_rate = annualInterestRate / 12
    balances = [balance]
    for m in range(1, tot_month+1):
        unpaid_balance = balances[-1] - monthly_payment
        new_balance = unpaid_balance + unpaid_balance*monthly_interest_rate
        balances.append(new_balance)
    return balances[-1]


def lowest_monthly_payment_by_ten(balance, annualInterestRate, tot_month = 12):
    """
    to find the lowest monthly payment
    so that at the end of tot_month, there are no positive remaining balance.
    :param balance: float, the outstanding balance on the credit card
    :param annualInterestRate: float, annual interest rate as a decimal
    :param tot_month: int, the paying periods
    :return monthly_payment: int by tens, minimum monthly payment as a decimal
    """
    monthly_payment = 10
    try_remaining_balance = balance
    while try_remaining_balance > 0:
        monthly_payment += 10
        try_remaining_balance = remaining_balance2(balance, annualInterestRate, monthly_payment, tot_month = 12)
    return monthly_payment


def test_lowest_monthly_payment_by_ten(balance, annualInterestRate, tot_month = 12):
   print("Lowest Payment:", lowest_monthly_payment_by_ten(balance, annualInterestRate, tot_month))

# balance = 3329
# annualInterestRate = 0.2
# balance = 4773
# annualInterestRate = 0.2
# balance = 3926
# annualInterestRate = 0.2
# test_lowest_monthly_payment_by_ten(balance, annualInterestRate)


def lowest_monthly_payment(balance, annualInterestRate, tot_month = 12):
    """
    to find the lowest monthly payment
    so that at the end of tot_month, there are no positive remaining balance.
    :param balance: float, the outstanding balance on the credit card
    :param annualInterestRate: float, annual interest rate as a decimal
    :param tot_month: int, the paying periods
    :return monthly_payment: float, minimum monthly payment as a decimal
    """
    monthly_interest_rate = annualInterestRate / 12
    low  = balance/12.0
    high = balance*(1 + monthly_interest_rate)**tot_month / 12
    epsilon = 0.001
    guess_payment = (low + high) / 2.0
    try_remaining_balance = remaining_balance2(balance, annualInterestRate, guess_payment, tot_month = 12)
    while not (0 > try_remaining_balance > -epsilon):
        # print("low: %d, high: %d", low, high)
        # 不该在迭代中用圆整，这会折损精度，导致达不到epsilon的范围内。
        # guess_payment = round((low + high) / 2.0, 2)
        if try_remaining_balance > 0:
            low = guess_payment
        elif try_remaining_balance < 0:
            high = guess_payment
        guess_payment = (low + high) / 2.0
        try_remaining_balance = remaining_balance2(balance, annualInterestRate, guess_payment, tot_month = 12)
    return guess_payment


def test_lowest_monthly_payment(balance, annualInterestRate):
    min_monthly_payment = lowest_monthly_payment(balance, annualInterestRate)
    print("Lowest Payment:", round(min_monthly_payment, 2))


# Test Case 1:
balance = 320000
annualInterestRate = 0.2

# Test Case 2:
# balance = 999999
# annualInterestRate = 0.18
test_lowest_monthly_payment(balance, annualInterestRate)
