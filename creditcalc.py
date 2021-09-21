
import argparse
from math import ceil, floor, log


def annuity(p, i, n):
    a = {}
    i = get_interest(i)
    a['payments'] = p * i * pow((1 + i), n) / (pow((1 + i), n) - 1)
    a['payments'] = ceil(a['payments'])
    t = n * a['payments']
    a['overpayment'] = t - p
    return a


def differentiated_payments(p, i, n):
    d = {}
    t = 0
    i = get_interest(i)
    for m in range(1, n+1):
        d[m] = ceil(p/n + (i * (p - ((p * (m - 1)) / n))))
        t += d[m]
    d['overpayment'] = t - p
    return d


def no_repayments(p, i, a):
    i = get_interest(i)
    base = 1 + i
    x = (a / (a - i * p))
    n = log(x, base)
    n = ceil(n)
    return n


def principal(a, i, n):
    i = get_interest(i)
    p = a / (i * pow((1 + i), n) / (pow((1 + i), n) - 1))
    p = floor(p)
    return p


def calc_overpayment(p, a, n):
    t = n * a
    overpayment = t - p
    return ceil(overpayment)


def get_interest(i):
    a = float(i) / 100
    i = a / 12
    return i


def format_years_months(n):
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


def format_diff_payments(d):
    message = ''
    for m, value in d.items():
        if m != "overpayment":
            message = "{}\nMonth {}: payment is {}".format(message, m, value)
    message += '\n'
    return message


def format_overpayment(overpayment):
    message = 'Overpayment = {}'.format(overpayment)
    return message


# main
def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-t', '--type', choices=['diff', 'annuity'], required=True,
                        help='options are diff, annuity')
    parser.add_argument('-p', '--principal', type=int,
                        help='the loan principal')
    parser.add_argument('-n', '--periods', type=int,
                        help='denotes the number of months needed to repay the loan')
    parser.add_argument('-i', '--interest', type=float, # required=True, this would be more useful
                        help='annual interest rate')
    parser.add_argument('-a', '--payment', type=float,
                        help='the monthly annuity payment amount and only available with the annuity calculation')

    args = parser.parse_args()
    calculation = args.type
    interest_arg = args.interest
    principal_arg = args.principal
    periods_arg = args.periods
    payment_arg = args.payment  # a - Annuity

    if calculation == "diff":
        if principal_arg is not None \
        and interest_arg is not None \
        and periods_arg is not None:  # Minimum requirements
            diff = differentiated_payments(principal_arg, interest_arg, periods_arg)
            print(format_diff_payments(diff))
            print(format_overpayment(diff['overpayment']))
        else:
            print("Incorrect parameters.")
    # "a" for annuity monthly payment amount
    elif calculation == "annuity":
        if principal_arg is not None \
                and periods_arg is not None \
                and interest_arg is not None:  # Have principal - calc annuity payments
            ann = annuity(principal_arg, interest_arg, periods_arg)
            print('Your monthly payment = {}!'.format(ann['payments']))
            print(format_overpayment(ann['overpayment']))
        elif principal_arg is not None \
                and interest_arg is not None \
                and payment_arg is not None:  # No Periods - calc periods
            periods_arg = no_repayments(principal_arg, interest_arg, payment_arg)
            overpayment = calc_overpayment(principal_arg, payment_arg, periods_arg)
            print(format_years_months(periods_arg))
            print(format_overpayment(overpayment))
        elif payment_arg is not None \
                and interest_arg is not None \
                and periods_arg is not None:  # No Principal - calc principal
            principal_arg = principal(payment_arg, interest_arg, periods_arg)
            ann = annuity(principal_arg, interest_arg, periods_arg)
            print("Your loan principal = {}!".format(principal_arg))
            print(format_overpayment(ann['overpayment']))
        else:
            print("Incorrect parameters.")


main()
