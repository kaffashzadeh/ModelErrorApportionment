# !user/bin/env python

"""
This program is written to calculate the error apportionment of the simulated data against observations.
"""
# imports python standard libraries
import os
import sys
import inspect
import matplotlib
import pandas as pd

# import local libraries
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir + '/../../')
os.sys.path.insert(0, parentdir)

font = {'family':'Serif', 'weight':'normal', 'size':12}
matplotlib.rc('font', **font)

__author__='Najmeh Kaffashzadeh'
__author_email__ = 'najmeh.kaffashzadeh@gmail.com'


class ApportionError:

    name = 'Apportion error'

    def __init__(self, file_name_obs=None, file_name_model=None):
        """
        This initializes the variables.

        Args:
            file_name_obs(str): observations file name.
            file_name_model(str): model file name.
        """
        self.fn_o = file_name_obs
        self.fn_m = file_name_model

    def read_data(self):
        """
        It reads the data.
        """
        self.dfo = pd.read_csv(sys.path[1] + '/../data/' + self.fn_o + '.csv',
                               parse_dates=True, index_col=0, header=0)['values']
        self.dfm = pd.read_csv(sys.path[1] + '/../data/' + self.fn_m + '.csv',
                               parse_dates=True, index_col=0, header=0)['values']

    def calc_corr(self):
        """
        It calculates the correlation between modelled and observed data.
        """
        return self.dfo.corr(self.dfm)
        #return stats.pearsonr(self.dfo, self.dfm)

    def calc_mse(self):
        """
        It calculates the mean square error (mse) of the model.
        """
        return ((self.dfm - self.dfo)**2).mean()

    def calc_e1(self):
        """
        It calculates the first term (bias) of the mse.
        """
        return (self.dfm.mean() - self.dfo.mean()) ** 2

    def calc_e2(self):
        """
        It calculates the second term (explained error) of the mse.
        """
        return (self.dfm.std() - (self.calc_corr() * self.dfo.std())) ** 2

    def calc_e3(self):
        """
        It calculates the third term (unexplained error) of the mse.
        """
        return (self.dfo.std() ** 2) * (1. - self.calc_corr()** 2)

    def print_es(self):
        """
        It prints the error terms based on the equation described in the paper.
        """
        print('MSE = ', self.calc_mse(),'\n',
              'E1 = ', self.calc_e1(),'\n',
              'E2 = ', self.calc_e2(),'\n',
              'E3 = ', self.calc_e3())

    def run(self):
        """
        It runs the scripts.

        Here, we assume the correct date-time index has been take into account. That means they are
        sorted based on utc or local time.
        """
        self.read_data()
        self.print_es()

if __name__ == '__main__':
    ApportionError(file_name_obs='temp_obs', file_name_model='temp_m1').run()