def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total_exp = (food_bill + electricity_bill + internet_bill + rent)
  if (budget < total_exp):
    return True
  else: 
    return False
