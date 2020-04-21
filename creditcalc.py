import math
import argparse
import sys

credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

parser = argparse.ArgumentParser()

parser.add_argument("--type", type=str, help="input type of calculation")

def check_positive(value):
    ivalue = float(value)
    if ivalue <= 0:
        print("Incorrect parameters")
        #sys.exit()
    return ivalue


parser.add_argument("--principal", type=check_positive, help="input value of credit principal")
parser.add_argument("--interest", type=check_positive, help="input value of credit interest")
parser.add_argument("--periods", type=check_positive, help="input count of periods")
parser.add_argument("--payment", type=check_positive, help="input monthly payment")

args = parser.parse_args()

if args.interest:
    #ANNUITY
    if args.type == "annuity":
        if args.payment and args.principal and not args.periods:

            nominal_interest_rate = float((args.interest / 100) / (12 * 1))

            # calculations
            periods_calculation = (math.ceil(
                math.log((args.payment / (args.payment - nominal_interest_rate * args.principal)), (1 + nominal_interest_rate))))
            years = math.floor(periods_calculation / 12)
            months = periods_calculation % 12

            # count of period string formatting
            years_over_one = f"year{'s' if years > 1 else ''}"
            andicko = f"{' and ' if years != 0 and months != 0 else ''}"
            years_over_zero = f'{years} {years_over_one}{andicko}'
            years_final = f"{years_over_zero if years > 0 else ''}"

            months_over_one = f"month{'s' if months > 1 else ''}"
            months_over_zero = f'{months} {months_over_one}'
            months_final = f"{months_over_zero if months > 0 else ''}"

            # output
            periods_output = f"You need {years_final}{months_final} to repay this credit!"
            print(periods_output)
            print("Overpayment = {:.0f}".format(args.payment * periods_calculation - args.principal))

        elif args.principal and args.periods and not args.payment:

            nominal_interest_rate = float((args.interest / 100) / (12 * 1))

            # calculations
            payment_calculation = math.ceil(args.principal * (
                        (nominal_interest_rate * math.pow((1 + nominal_interest_rate), args.periods)) / (
                            math.pow((1 + nominal_interest_rate), args.periods) - 1)))

            # output
            payment_output = ("Your annuity payment = {:.0f}!".format(payment_calculation))
            print(payment_output)
            print("Overpayment = {:.0f}".format(payment_calculation * args.periods - args.principal))

        elif args.payment and args.periods and not args.principal:

            nominal_interest_rate = float((args.interest / 100) / (12 * 1))

            # calculations
            principal_calculation = int(args.payment / (
                        (nominal_interest_rate * math.pow((1 + nominal_interest_rate), args.periods)) / (
                            math.pow((1 + nominal_interest_rate), args.periods) - 1)))

            # output
            principal_output = f"Your credit principal = {principal_calculation}!"
            print(principal_output)
            print("Overpayment = {:.0f}".format(args.payment * args.periods - principal_calculation))

    # DIFFERENTIATE
    elif args.type == "diff":
        if args.payment:
            print("Incorrect parameters")
        elif args.principal and args.periods:

            nominal_interest_rate = float((args.interest / 100) / (12 * 1))

            current_period = 1
            paid = 0
            while current_period <= args.periods:
                diff_payment = math.ceil(args.principal/args.periods + nominal_interest_rate * (args.principal - (args.principal *
                                                                                (current_period - 1)) / args.periods))
                print("Month {}: paid out {:.0f}".format(current_period, diff_payment))
                paid += diff_payment
                current_period += 1
            print("Overpayment = {:.0f}".format(paid - args.principal))

    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")

print(final_output)
