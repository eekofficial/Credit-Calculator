import math
import argparse

def calculate_interest(i):
    return i / 12 / 100
def calculate_count_of_months(principal, payment, interest):
    interest = calculate_interest(interest)
    months = int(math.ceil(math.log(payment / (payment - interest * principal), 1 + interest)))
    if months // 12 == 0:
        print('{} month{}'.format(months, 's' * (1 % months)))
    elif months % 12 == 0:
        print('{} year{}'.format(months // 12, 's' * (1 % (months // 12))))
    else:
        print('{} year{} and {} month{}'.format(months // 12, 's' * (1 % (months // 12)), months % 12, 's' * (1 % (months % 12))))
    print('Overpayment = {}'.format(principal - payment * months))

def calculate_monthly_payment(principal, periods, interest):
    interest = calculate_interest(interest)
    payment = int(math.ceil(principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
    print('Your annuity payment = {}!'.format(payment))
    print('Overpayment = {}'.format(principal - payment * periods))

def calculate_credit_principal(payment, periods, interest):
    interest = calculate_interest(interest)
    principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
    print('Your credit principal = {}!'.format(principal))
    print('Overpayment = {}'.format(principal - payment * periods))

def check_input(args):
    if args.type not in ('annuity', 'diff'):
        print('Incorrect parameters')
        return False
    if args.type == 'diff' and args.payment:
        print('Incorrect parameters')
        return False
    if not args.interest:
        print('Incorrect parameters')
        return False
    return True

def calculate_annuity(args):
    if not args.principal:
        calculate_credit_principal(float(args.payment), float(args.periods), float(args.interest))
    elif not args.payment:
        calculate_monthly_payment(float(args.principal), float(args.periods), float(args.interest))
    elif not args.periods:
        calculate_count_of_months(float(args.principal), float(args.payment), float(args.interest))

def calculate_diff(args):
    interest = calculate_interest(float(args.interest))
    principal = float(args.principal)
    periods = int(args.periods)
    payments_sum = 0
    for i in range(1, periods + 1):
        payment_i = int(math.ceil(principal / periods + interest * (principal - (principal * (i - 1)) / periods)))
        print('Month {}: paid out {}'.format(i, payment_i))
        payments_sum += payment_i
    print('Overpayment = {}'.format(principal - payments_sum))

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
args = parser.parse_args()

if check_input(args):
    if args.type == 'annuity':
        calculate_annuity(args)
    elif args.type == 'diff':
        calculate_diff(args)

