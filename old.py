# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# write your code here
import sys
from math import ceil, floor, log
args = sys.argv


def repayments(p, n):
    settlement = ''
    # calculate payment amounts (and settlement payment)
    # payments = principal // number_of_months + additional month if required to settle
    r = int(p / n)
    is_float = bool(p % n)
    if is_float:
        r += 1
    if r * n > p:
        s = p - (r * (n - 1))
        if s:
            settlement = ' and the last payment = {}'.format(s)
    r = 'Your monthly payment = {}{}.'.format(r, settlement)
    return r


def differentiated_payments(p, i, n, m):
    d = p/n + i * (p - ((p * (m - 1)) / n))  # may change to a list output
    return d


def annuity(p, i, n):
    a = p * i * pow((1 + i), n) / (pow((1 + i), n) - 1)
    a = ceil(a)
    return a


def no_repayments(p, i, a):
    base = 1 + i
    x = (a / (a - i * p))
    n = log(x, base)
    n = ceil(n)
    return n


def principal(a, i, n):
    p = a / (i * pow((1 + i), n) / (pow((1 + i), n) - 1))
    p = floor(p)
    return p


def get_interest():
    a = float(input("Enter the loan interest:")) / 100
    i = a / 12
    return i


def get_principal():
    p = int(input("Enter the loan principal:"))
    return p


def get_monthly_payments():
    m = int(input("Enter the monthly payment:"))
    return m


def get_no_periods():
    n = int(input("Enter the number of periods:"))
    return n


def get_annuity():
    a = float(input("Enter the annuity payment:"))
    return a


def get_years_months(n):
    months = ''
    years = ''
    y = n // 12
    m = n % 12
    if y == 0:
        years = ''
    elif y == 1:
        years = '1 year'
    elif y > 1:
        years = '{} years'.format(y)
    if m == 0:
        months = ''
    elif m == 1:
        months = '1 month'
    elif m > 1:
        months = '{} months'.format(m)
    is_and = bool(months or years)
    if is_and is True:
        _and = 'and'
    else:
        _and = ''
    message = 'It will take {} {} {} to repay this loan!'.format(years, _and, months)
    return message


calc_question = """What do you want to calculate?
                type "n" for number of monthly payments,
                type "a" for annuity monthly payment amount,
                type "p" for loan principal:"""

calculation = input(calc_question)

# "n" for number of monthly payments
if calculation == "n":
    principal = get_principal()
    annuity_payments = get_monthly_payments()
    interest = get_interest()
    no_repayments = no_repayments(principal, interest, annuity_payments)
    print(get_years_months(no_repayments))
# "a" for annuity monthly payment amount
elif calculation == "a":
    principal = get_principal()
    periods = get_no_periods()
    interest = get_interest()
    annuity = annuity(principal, interest, periods)
    print('Your monthly payment = {}!'.format(annuity))
# "p" for loan principal:
elif calculation == "p":
    annuity = get_annuity()
    periods = get_no_periods()
    interest = get_interest()
    principal = principal(annuity, interest, periods)
    print('Your loan principal = {}!'.format(principal))



