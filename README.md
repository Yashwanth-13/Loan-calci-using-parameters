# Loan-Calculator
This is a python script to calculate principal of a loan, number of months to repay a loan, monthly payment to be done for a loan or just a differentiated payment
<br /> <br />
Arguments have to be passed in order to calculate any one of the above mentioned things. Example command for each of it is given too.<br />
<br />
* Finding *total loan* needs --> payment, number of months you have to repay the loan, **YEARLY** interest
* Finding *number of months required* needs --> principal of the loan, payment you would do in a single month, **YEARLY** interest
* Finding *monthly payment* needs --> principal of the loan, number of months you have to repay the loan, **YEARLY** interest
* Finding *differentiated payment* needs --> principal of the loan, number of months you have to repay the loan and **YEARLY** interest
<br /><br />
* For *principal*:
  * python ./loan_calci.py --type=annuity --payment=800 --periods=12 --interest=2.3
* For *months* requried to repay:
  * python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
* For *monthly payment* to be done over some months:
  * python ./loan_calci.py --type=annuity --principal=10000 --periods=10 --interest=2.5
* For *differentiated payment*:
  * python .\loan_calci.py --type=diff --principal=10000 --periods=6 --interest=4.2
 

