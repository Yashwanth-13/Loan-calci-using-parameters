import argparse, support

parcel = argparse.ArgumentParser(description="This is a program to calculate the loan")

# Parsing the passed arguments
parcel.add_argument("--type",choices=["annuity", "diff"])
parcel.add_argument("--principal")
parcel.add_argument("--payment")
parcel.add_argument("--interest")
parcel.add_argument("--periods")

the_args = parcel.parse_args()

if the_args.type == 'annuity':
    # Finding the principal
    if the_args.principal is None:
        support.principal_calculator()
    # Finding the number of months
    elif the_args.periods is None:
        support.periods_calculator()
    # Finding the monthly payment
    elif the_args.payment is None:
        support.monthly_payment_calculator()

elif the_args.type == 'diff':
    support.differentiated_payment()
else:
    print('Incorrect parameters')