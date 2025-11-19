import math
from uncertainties import ufloat

class Calculator():
    def __init__(self):
        self.c = 3e8 #m/s
        self.data = {}
        self.result = {}

    def get_halflife_by_single_distance(self, workmode):

        if workmode == "1":
            self.data['plunger_distance'] = 13 #float(input("plunger distance in micrometers: "))
            self.data['beta'] = 0.008 #float(input("beta(v/c): "))
            self.data['area_shifted'] = 7676 #float(input("area of shifted component: "))
            self.data['area_unshifted'] = 4447 #float(input("area of unshifted component: "))
            self.result['T_halflife'] = ((-1)*math.log(2)*self.data['plunger_distance']*
                (1e-6)/(self.data['beta']*self.c))/(math.log((self.data['area_unshifted'])/(self.data['area_unshifted'] + self.data['area_shifted'])))
            print(f"T_1/2 = {round(self.result['T_halflife']*(1e+12),2)} ps") 

        