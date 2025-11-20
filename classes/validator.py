from uncertainties import ufloat
import os
import json

class Validator:

    @staticmethod
    def validate_hand_or_file():
        file_data = None
        if os.path.exists('input_data/GNC_input.json'):
            with open('input_data/GNC_input.json', 'r') as f:
                file_data = json.load(f)
        return file_data 
 
    @staticmethod
    def validate_yes_no(hand_or_file):
        if hand_or_file == 'y':
            return 'n'
        while True:
            cont = input("Do you want to perform another calculation? (y/n): ")
            if cont.lower() in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        return cont
    
    @staticmethod
    def validate_workmode(mode_list, data):
        if data:
            return data['work_mode']
        print("\nWork modes: ")
        for key in mode_list:
            print(f"{key}) {mode_list[key]}")
        print()
        work_mode = input("select work mode: ")
        valid_modes = mode_list.keys()
        while work_mode not in valid_modes:
            work_mode = input("Invalid work mode. Please select valid mode from the list: ")
        return work_mode
    
    @staticmethod
    def validate_data_input(str_data):
        data = str_data.split()
        if len(data) == 1 :
            res = float(data[0])
        elif len(data) == 2 :
            res = ufloat(float(data[0]), float(data[1]))
        else:
            print("Invalid input. Please enter a number or a number with uncertainty (e.g., '10' or '10 0.5').")
            res = None
        return res

    @staticmethod
    def validate_halflife_by_single_distance():
        data = {}
        while True:
            plunger_distance_input = input("plunger distance in micrometers: ")
            data['plunger_distance'] = Validator.validate_data_input(plunger_distance_input)
            if data['plunger_distance'] is not None:
                break
            else:
                continue
        while True:
            beta_input = input("beta(v/c): ").split()
            #TODO: refactor
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