#Author:  Brian Stamm
#Assignment:  loanPayments.py
#Date:  12.21.15
#Notes:  None.

import math

def main():
    print()
    loan = float(input('Amount of loan: $'))
    rate = float(input('Monthly interest rate: '))
    pay = int(input('Number of payments: '))

    c = (rate / 100) + 1
    d = math.pow(c, pay)
    a = (rate / 100) * d
    b = d - 1
    monthly = a / b * loan
    total = monthly * pay
    paid = total - loan

    print("\nHere is the loan information:\n")
    print("Loan amount: $", format(float(loan), ',.2f'), sep='')
    print("Monthly Interest Rate:  ", format(rate, '.2f'), "%", sep='')
    print("Number of payments:  ", pay, sep='')
    print("Monthly payments:  $", format(float(monthly), ',.2f'), sep='')
    print("Amount Paid Back:  $", format(float(total), ',.2f'), sep='')
    print("Interest Paid:  $", format(float(paid), ',.2f'), sep='')
    print()

main()
