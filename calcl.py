import numpy as np

months = 42
AER = 0.05
monthly_deposit = 320.62

def calculate_reg_savings_gains(months, AER):
    """Calculates the returns of my regular savings account given a regular monthly deposit"""
    amounts = np.full(months, monthly_deposit)
    months_remaining = [months - i for i, amounts in enumerate(amounts)]
    # print(amounts)
    # print(months_remaining)

    mySum = 0

    for i, price in enumerate(amounts):

        #Equivalent rate over interval given the annual rate of 5%
        equivalent_rate = (AER + 1.0)**(months / 12) 

        #Add to sum
        mySum += price*(equivalent_rate)**(months_remaining[i]/months)

    print(f'Savings without interest: £{sum(amounts):.2f}')
    print(f'Savings with interest: £{mySum:.2f}')
    print(f'Gains of £{mySum- sum(amounts):.2f}')

calculate_reg_savings_gains(months, AER)



