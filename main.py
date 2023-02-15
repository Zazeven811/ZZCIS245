interest_Rate = int(input("Please enter the interest rate in a whole number:"))
print()

initial_invesment = float(
  input("How much is the initial investment in a whole number:"))

Target = 2 * initial_invesment

balance = initial_invesment
year = 0

while balance < Target:
  year = year + 1
  interest = balance * interest_Rate / 100
  balance = balance + interest

print("Your investment will have doubled after", year, "years")
