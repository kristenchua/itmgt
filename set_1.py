'''
Savings
'''
def savings(gross_pay, tax_rate, expenses):
  net_income=int(gross_pay*(1-tax_rate))
  return net_income-expenses

'''
Material Waste
'''
def material_waste(total_material, material_units, num_jobs, job_consumption):
  material_used=num_jobs*job_consumption
  material_left=total_material-material_used
  return str(material_left)+material_units

'''
Interest
'''
def interest(principal, rate, periods):
  total=int(principal*rate*periods)
  return principal+total
