import numpy as np

def tax(income):
    """
    Return the taxes owned for a given income
    """
    if income <= 300_000:
        tax = 0
    elif 300_000 < income <= 700_000:
        tax = (income - 300_000) * 0.2
    else:
        tax = round(400_000 * 0.2 + (income - 700_000) * 0.35,2)
    return tax

incomes = np.linspace(0,1_200_000,13)
taxes_loop = np.empty(len(incomes))
after_tax = np.array([])
net_income = np.empty(len(incomes))

for i, income in enumerate(incomes):
    taxes = tax(incomes[i])
    taxes_loop[i] = taxes

for i, taxes in enumerate(taxes_loop): 
    inc = incomes[i]
    net_income[i] = inc - taxes
    #print(f"Gross Income: {inc:10.0f} Tax: {taxes:10.0f} After-tax Income: {net_income[i]:10.0f}")

#print(taxes_loop)
#print(after_tax)

def tax_numpy(income):
    """
    Takes an array of annual incomes and,
    Returns an array containing the corresponding taxes
    Uses vectorized NumPy operations
    """
    mid = np.maximum(np.minimum(income, 700_000) - 300_000, 0)
    top = np.maximum(income - 700_000, 0)
    return mid * 0.2 + top * 0.35

tax_np = tax_numpy(incomes)
after_tax_np = incomes - tax_np
#print(tax_np)
#print(after_tax_np)

equal_tax = np.allclose(tax_np, taxes_loop)
equal_net = np.allclose(after_tax_np, net_income)
print(equal_tax)
print(equal_net)
