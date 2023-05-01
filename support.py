import __main__, math

def principal_calculator():
    the_args = __main__.the_args
    values = [the_args.payment, the_args.periods, the_args.interest]
    
    # Checking if the required parameters are not passed by the user
    value_checker(values)

    # Assigning the respective values
    monthly = int(values[0])
    periods = int(values[1])
    yearly_interest = float(values[2])

    # Converting the yearly interest into monthly interest
    monthly_interest = (yearly_interest / 100) / 12

    the_one_with_power = math.pow((1 + monthly_interest), periods)
    numerator = the_one_with_power - 1
    denominator = monthly_interest * the_one_with_power

    # The formula to find the loan principal
    loan_principal = math.ceil(monthly * (numerator / denominator))

    print(f"Your loan principal: {loan_principal}!")

def periods_calculator():
    
    the_args = __main__.the_args
    values = [the_args.payment, the_args.principal, the_args.interest]
    
    # Checking if the required parameters are not passed by the user
    value_checker(values)

    #Assigning the respective values
    payment = int(values[0])
    principal = int(values[1])
    yealy_interest = float(values[2]) 

    # Converting the yearly interest into monthly interest
    monthly_interest = (yealy_interest / 100) / 12
    x = payment / (payment - (monthly_interest * principal))
    base = 1 + monthly_interest

    # Formula to find the number of payments
    number_of_payments = math.ceil(math.log(x, base))
    over_payment = 0

    # Printing appropriate statements with respect to the {number_of_payments} and {over_payment}
    if number_of_payments < 12:
        print(f"It will take {number_of_payments} months to repay this loan")
    else:
        if number_of_payments % 12 == 0:
            over_payment = (number_of_payments * payment) - principal
            print("\nIt will take {0} years to repay this loan!".format(math.ceil(number_of_payments / 12)))
        elif number_of_payments > 12 and number_of_payments < 24:
            months = 24 - number_of_payments
            print(f"\nIt will take 1 year and {months} months to repay this loan")
        else:
            years = math.floor(number_of_payments / 12)
            months = number_of_payments % 12
            print("\nIt will take {0} years and {1} months to repay this loan".format(years, months))
        print(f'The over payment is {over_payment}\n') if over_payment > 0 else print("There is no overpayment for this loan!\n")

def monthly_payment_calculator():

    the_args = __main__.the_args
    values = [the_args.principal, the_args.periods, the_args.interest]
    
    # Checking if the required parameters are not passed by the user
    value_checker(values)

    # Assigning the variables accordingly
    principal = int(values[0])
    months = int(values[1])
    yearly_interest = float(values[2])

    # Converting the yearly interest into monthly interest
    monthly_interest = (yearly_interest / 100) / 12
    the_one_with_power = math.pow((1 + monthly_interest), months)
    numerator = monthly_interest * the_one_with_power
    denominator = the_one_with_power - 1
    
    # The formula to find the monthly payment
    monthly_payment = math.ceil(principal * (numerator / denominator))
    over_payment = (monthly_payment * months) - principal

    # Printing the required things
    print(f"\nYour monthly payment for {months} months is {monthly_payment}")
    print(f"The overpayment is {over_payment}\n") if over_payment > 0 else print("\nThere is no overpayment for this loan!\n")   

def differentiated_payment():
    the_args = __main__.the_args
    values = [the_args.principal, the_args.periods, the_args.interest]

    # Checking if the required parameters are not passed by the user
    value_checker(values)

    # Assigning the variables accordingly
    principal = int(values[0])
    periods = int(values[1])
    yearly_interest = float(values[2])

    # Converting the yearly interest into monthly interest
    monthly_interest = (yearly_interest / 100) / 12
    the_constant = principal / periods
    sum = 0

    # Differentiated payment calculation and displaying them..
    print(f"\nDifferentiated Payment for {periods} months is: \n")
    for month_index in range(1, periods + 1):
        current_month_payment =  the_constant + (monthly_interest * (principal - (principal * (month_index - 1)) / periods))
        sum += math.ceil(current_month_payment)
        print(f'Month {month_index}: {math.ceil(current_month_payment)}')
    over_payment = sum - principal

    # For overpayment, if any
    print(f"\nThe overpayment will be {over_payment}\n") if over_payment > 0 else print("\nThere is no overpayment for this loan!")



def value_checker(values):
    for _ in values:
        if _ is None:
            print('Incorrect parameters')
            exit(1)