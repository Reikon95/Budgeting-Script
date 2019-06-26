def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total_exp = (food_bill + electricity_bill + internet_bill + rent)
  if (budget < total_exp):
    return True
  else: 
    return False

def how_much(budget, food_bill, electricity_bill, internet_bill, rent):
  total_exp = (food_bill + electricity_bill + internet_bill + rent)
  if (budget < total_exp):
    return 'You are ' + str((total_exp - budget)) + ' over budget!'
  elif (budget > total_exp):
     return 'Nice job, you are ' + str((budget - total_exp)) + ' under budget!'
  else:
        return 'You are exactly at your budget - be careful!'
