from uncertainties import UFloat, ufloat
from classes.validator import Validator
from uncertainties import unumpy as unp  
import math 
from scipy.odr import ODR, Model, RealData
from classes.ploter import Ploter
from uncertainties.umath import log

class Calculator():
    def __init__(self, data=None):
        self.c = 3e8 #m/s
        self.data = data if data else {}
        self.result = {}

    def get_halflife_by_single_distance(self, hand_or_file_check):

        if hand_or_file_check == 'y':
            for key in self.data:
                if key == 'work_mode':
                    continue
                self.data[key] = Validator.validate_data_input(self.data[key])
                if self.data[key] is None:
                    raise ValueError(f"Invalid data for {key}.")
        else:
            self.data = Validator.validate_halflife_by_single_distance()

        if isinstance(self.data['plunger_distance'], UFloat) or isinstance(self.data['beta'], UFloat) or isinstance(self.data['area_shifted'], UFloat):
            self.result['T_halflife'] = ((-1)*unp.log(2)*self.data['plunger_distance']*
                (1e-6)/(self.data['beta']*self.c))/(unp.log((self.data['area_unshifted'])/(self.data['area_unshifted'] + self.data['area_shifted'])))
            print("T_1/2 = {:.2u} ps".format(self.result['T_halflife']*(1e+12)))
        else:
            self.result['T_halflife'] = ((-1)*math.log(2)*self.data['plunger_distance']*
                (1e-6)/(self.data['beta']*self.c))/(math.log((self.data['area_unshifted'])/(self.data['area_unshifted'] + self.data['area_shifted'])))
            print("T_1/2 = {:.2f} ps".format(self.result['T_halflife']*(1e+12)))

    def get_halflife_by_multiple_distances(self):
        beta_ = ufloat(float(self.data['beta'][0]),float(self.data['beta'][1]))
        distances = [ ufloat(float(self.data['plunger_distance'][i][0]), float(self.data['plunger_distance'][i][1])) for i in range(len(self.data['plunger_distance'])) ]
        area_shifted = [ ufloat(float(self.data['area_shifted'][i][0]), float(self.data['area_shifted'][i][1])) for i in range(len(self.data['area_shifted'])) ]
        area_unshifted = [ ufloat(float(self.data['area_unshifted'][i][0]), float(self.data['area_unshifted'][i][1])) for i in range(len(self.data['area_unshifted'])) ]    
        log_area = [log(area_unshifted[i]/(area_unshifted[i] + area_shifted[i])) for i in range(len(area_shifted))]
        self.get_linear_fit_coefficients_plot_get_lifetime(distances, log_area, beta_)  

    def get_linear_fit_coefficients_plot_get_lifetime(self, distanse, log_area, beta_):
        x = unp.nominal_values(distanse)
        x_err = unp.std_devs(distanse)
        y = unp.nominal_values(log_area)
        y_err = unp.std_devs(log_area)

        # Define a function  to fit the data with.
        def linear_func(p, x):
            m, c = p
            return m*x + c
        # Create a model for fitting.
        linear_model = Model(linear_func)
        # Create a RealData object using our initiated data from above.
        data = RealData(x, y, sx=x_err, sy=y_err)
        # Set up ODR with the model and data.
        odr = ODR(data, linear_model, beta0=[0., 1.])
        # Run the regression.
        out = odr.run()
        # Use the in-built pprint method to give us results.
        #out.pprint()

        a = ufloat(float(out.beta[0]), float(out.sd_beta[0]))
        self.result['T_halflife'] = log(2)*(1e-6)/(beta_*abs(a)*self.c)
        print("T_1/2 = {:.2u} ps".format(self.result['T_halflife']*(1e+12)))
        T_for_plot = "= {:.2u} ps".format(self.result['T_halflife']*(1e+12))
        Ploter.plot_data_and_fit(x, x_err, y, y_err, linear_func, out, T_for_plot )