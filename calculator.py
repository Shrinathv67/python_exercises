def add(num1, num2):
    res = num1 + num2
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

#Main starts from here
alpha = 10
beta = 20
total = add(alpha, beta)
print("Sum:", total)

diff = sub(alpha, beta)
print("Diff:", diff)

eng1 = 250
ind1 = 220
eng2 = 180

eng_tot = add(eng1, eng2)
#print(eng_tot)
ind2 = sub(eng_tot, ind1)
#print(ind2)
target = add(ind2, 1)
print("Runs to win:", target)

veg = 120
fruits = 45
cash = 200
tot_cost = add(veg, fruits)
balance_amt = sub(cash, tot_cost)
print("Amount to return:", balance_amt)