#compound interest calculator

def compound_interest(principal, rate, time):
    amount= principal*pow((1+rate/100),time)
    ci=amount-principal

    return ci

principal= int(input("Enter the principal value: "))
rate = float(input("Enter the rate of interest in percentage: "))
time = float(input("Enter the time in years: "))

print(f"The total compound interest is: {compound_interest(principal, rate, time)}")
