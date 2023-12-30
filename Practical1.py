def calculate_simple_interest(principal, rate_of_interest, time):
    simple_interest = (principal * rate_of_interest * time) / 100
    return simple_interest

principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time in years: "))


simple_interest = calculate_simple_interest(principal, rate_of_interest, time)
print("Simple Interest:",simple_interest)

print("This Program is Prepared by 22CE103 Bhavya")