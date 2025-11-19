from uncertainties import ufloat, UFloat
from classes.validator import Validator
from uncertainties import unumpy as unp  
import math 

class Calculator():
    def __init__(self):
        self.c = 3e8 #m/s
        self.data = {}
        self.result = {}

    def get_halflife_by_single_distance(self, workmode):

        if workmode == "1":
            self.data = Validator.validate_halflife_by_single_distance()
            if isinstance(self.data['plunger_distance'], UFloat) or isinstance(self.data['beta'], UFloat) or isinstance(self.data['area_shifted'], UFloat):
                self.result['T_halflife'] = ((-1)*unp.log(2)*self.data['plunger_distance']*
                    (1e-6)/(self.data['beta']*self.c))/(unp.log((self.data['area_unshifted'])/(self.data['area_unshifted'] + self.data['area_shifted'])))
                print("T_1/2 = {:.2u} ps".format(self.result['T_halflife']*(1e+12)))
            else:
                self.result['T_halflife'] = ((-1)*math.log(2)*self.data['plunger_distance']*
                    (1e-6)/(self.data['beta']*self.c))/(math.log((self.data['area_unshifted'])/(self.data['area_unshifted'] + self.data['area_shifted'])))
                print("T_1/2 = {:.2f} ps".format(self.result['T_halflife']*(1e+12)))