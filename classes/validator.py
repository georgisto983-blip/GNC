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
