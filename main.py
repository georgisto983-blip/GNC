from classes.calculator import Calculator
from classes.validator import Validator

#dictionary
mode_list = {
    "1": "calculate half-life by one distance",
}

print("-------This is GNC V1.1 (Georgi's Nuclear Calculator)-------")

data = Validator.validate_hand_or_file()

if data:
    hand_or_file_check = 'y'
else:
    hand_or_file_check = 'n'

while True:
  workmode = Validator.validate_workmode(mode_list, data)

  calculator = Calculator(data)
  #TODO: manage workmode
  calculator.get_halflife_by_single_distance(hand_or_file_check)

  cont = Validator.validate_yes_no(hand_or_file_check)

  if cont.lower() == 'n':
      break
  elif cont.lower() == 'y':
      continue


print("\n-------End of calculation-------")