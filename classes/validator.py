from uncertainties import ufloat
class Validator:

    @staticmethod
    def validate_yes_no(input_str):
        while True:
            cont = input("Do you want to perform another calculation? (y/n): ")
            if cont.lower() in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        return cont
    
    @staticmethod
    def validate_workmode(mode_list):
        print("\nWork modes: ")
        for key in mode_list:
            print(f"{key}) {mode_list[key]}")
        print()
        work_mode = input("select work mode: ")
        valid_modes = mode_list.keys()
        while work_mode not in valid_modes:
            work_mode = input(f"Invalid work mode. Please select valid mode from the list: ")
        return work_mode
    
    @staticmethod
    def validate_halflife_by_single_distance():
        data = {}
        while True:
            plunger_distance_input = input("plunger distance in micrometers: ").split()
            if len(plunger_distance_input) == 1 :
                data['plunger_distance'] = float(plunger_distance_input[0])
                break
            elif len(plunger_distance_input) == 2 :
                data['plunger_distance'] = ufloat(float(plunger_distance_input[0]), float(plunger_distance_input[1]))
                break
            else:
                print("Invalid input. Please enter a number or a number with uncertainty (e.g., '10' or '10 0.5').")
                continue
        while True:
            beta_input = input("beta(v/c): ").split()
            if len(beta_input) == 1 :
                data['beta'] = float(beta_input[0])
                break
            elif len(beta_input) == 2 :
                data['beta'] = ufloat(float(beta_input[0]), float(beta_input[1]))
                break
            else:
                print("Invalid input. Please enter a number or a number with uncertainty (e.g., '10' or '10 0.5').")
                continue
        while True:
            area_shifted_input = input("area of shifted component: ").split()
            if len(area_shifted_input) == 1 :
                data['area_shifted'] = float(area_shifted_input[0])
                break
            elif len(area_shifted_input) == 2 :
                data['area_shifted'] = ufloat(float(area_shifted_input[0]), float(area_shifted_input[1]))
                break
            else:
                print("Invalid input. Please enter a number or a number with uncertainty (e.g., '10' or '10 0.5').")
                continue
        while True:
            area_unshifted_input = input("area of unshifted component: ").split()
            if len(area_unshifted_input) == 1 :
                data['area_unshifted'] = float(area_unshifted_input[0])
                break
            elif len(area_unshifted_input) == 2 :
                data['area_unshifted'] = ufloat(float(area_unshifted_input[0]), float(area_unshifted_input[1]))
                break
            else:
                print("Invalid input. Please enter a number or a number with uncertainty (e.g., '10' or '10 0.5').")
                continue 
        return data
