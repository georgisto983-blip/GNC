from classes.calculator import Calculator
from classes.validator import Validator

#dictionary
mode_list = {
    "1": "calculate half-life by one distance",
}

print("-------This is GNC V1.0 (Georgi's Nuclear Calculator)-------")

while True:
  workmode = Validator.validate_workmode(mode_list)

  calculator = Calculator()
  calculator.get_halflife_by_single_distance(workmode)

  cont = Validator.validate_yes_no(workmode)

  if cont.lower() == 'n':
      break
  elif cont.lower() == 'y':
      continue


print("\n-------End of calculation-------")