#Classes in Python

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print milton.full_time_wage(10)

#empty class
class Car(object):
  pass
#calling methods
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    return "This is a "+self.color+" "+self.model+" with "+str(self.mpg)+" MPG."

my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()
