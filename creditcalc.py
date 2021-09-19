# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import argparse
from math import ceil, floor, log


def differentiated_payments(p, i, n):
    d = []
    for m in range(n):
        d[m] = p/n + i * (p - ((p * (m - 1)) / n))
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


# main



def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-t', '--type', choices=['diff', 'annuity'], required=True,
                        help='options are diff, annuity')
    parser.add_argument('-p', '--principal', type=int, required=True,
                        help='the loan principal')
    parser.add_argument('-n', '--periods', type=int,
                        help='denotes the number of months needed to repay the loan')
    parser.add_argument('-i', '--interest', type=float, required=True,
                        help='annual interest rate')
    parser.add_argument('-a', '--payment', type=float,
                        help='the monthly annuity payment amount and only available with the annuity calculation')

    args = parser.parse_args()
    if len(args) < 3:
        print(f"Too few options {}".len(args))
        exit(1)

    calculation = args.type
    interest = args.interest
    principal = args.principal
    periods = args.periods

    if calculation == "diff":


        print(get_years_months(no_repayments))
    # "a" for annuity monthly payment amount
    elif calculation == "annuity":
        annuity = annuity(principal, interest, periods)
        print('Your monthly payment = {}!'.format(annuity))



# TODO Remove if not required
"""def repayments(p, n):
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
    return r"""

