import argparse
import sys
import math

parcel = argparse.ArgumentParser(description="This is a program to calculate the loan")

parcel.add_argument("--type",choices=["annuity", "diff"])
parcel.add_argument("--principal")
parcel.add_argument("--payment")
parcel.add_argument("--interest")
parcel.add_argument("--periods")


the_args = parcel.parse_args()


if the_args.type == 'annuity':

    # Finding the principal
    if the_args.principal is None: # Checking what the user wants based on the passed arguments
        values = [the_args.payment, the_args.periods, the_args.interest]
        for _ in values:  # Checking for required parameters having no value passed by the user
            if _ is None:
                print('Incorrect parameters')
                exit(1)

        # Assigning the respective values
        monthly = int(values[0])
        periods = int(values[1])
        interest = float(values[2])
        interest = (interest / 100) / 12 # Converting the yearly interest into monthly interest

        the_one_with_power = math.pow((1 + interest), periods)
        numerator = the_one_with_power - 1
        denominator = interest * the_one_with_power
        loan_principal = math.ceil(monthly * (numerator / denominator)) # The formula to find the loan principal
        print(f"Your loan principle: {loan_principal}!")

    # Finding the number of months required
    elif the_args.periods is None:
        values = [the_args.payment, the_args.principal, the_args.interest]
        for _ in values:  # Checking for required parameters having no value passed by the user
            if _ is None:
                print('Incorrect parameters')
                exit(1)

        #Assigning the respective values
        principal = int(values[1])
        payment = int(values[0])
        interest = float(values[2])
        interest = (interest / 100) / 12
        x = payment / (payment - (interest * principal))
        base = 1 + interest
        number_of_payments = math.ceil(math.log(x, base))
        over_payment = 0
        if number_of_payments < 12:
            print(f"It will take {number_of_payments} months to repay this loan")
        else:
            if number_of_payments % 12 == 0:
                over_payment = (number_of_payments * payment) - principal
                print("It will take {0} years to repay this loan!".format(math.ceil(number_of_payments / 12)))
                print(f'Overpayment = {over_payment}')
            elif number_of_payments > 12 and number_of_payments < 24:
                months = 24 - number_of_payments
                print(f"It will take 1 year and {months} months to repay this loan")
            else:
                years = math.floor(number_of_payments / 12)
                months = number_of_payments % 12
                print("It will take {0} years and {1} months to repay this loan".format(years, months))

    # Finding the monthly payment
    elif the_args.payment is None:

        values = [the_args.principal, the_args.periods, the_args.interest]
        for _ in values:  # Checking for required parameters having no value passed by the user
            if _ is None:
                print('Incorrect parameters')
                exit(1)
        principle = int(values[0])
        months = int(values[1])
        interest = float(values[2])
        interest = (interest / 100) / 12
        the_one_with_power = math.pow((1 + interest), months)
        numerator = interest * the_one_with_power
        denominator = the_one_with_power - 1

        monthly_payment = math.ceil(principle * (numerator / denominator)) # The formula to find the monthly payment
        over_payment = (monthly_payment * months) - principle
        print(f"Your monthly payment = {monthly_payment}!")

elif the_args.type == 'diff':
    the_values = [the_args.principal, the_args.periods, the_args.interest]
    for _ in the_values:
        if _ is None:
            print('Incorrect parameters')
            exit(1)
    principal = int(the_args.principal)
    periods = int(the_args.periods)
    interest = float(the_args.interest)
    interest = (interest / 100) / 12
    the_constant = principal / periods
    sum = 0

    for month_index in range(1, periods + 1):
        current_month_payment =  the_constant + (interest * (principal - (principal * (month_index - 1)) / periods))
        sum += math.ceil(current_month_payment)
        print(f'Month {month_index}: payment is {math.ceil(current_month_payment)}')
    over_payment = sum - principal
    print(f'Overpayment is: {over_payment}')
else:
    print('Incorrect parameters')