#Imports
import numpy as np
import pandas as pd
import scipy as sp



def Gaussian(mu, sigma):
    '''
        This function is the normal distribution function;
        it returns an array of x and y values for the Gaussian function.
    '''
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 2000)
    y = 1 / (np.sqrt(2*np.pi)*sigma) * np.e**(-(x - mu)**2/(2*sigma**2))

    return y



def static_measurand(n, mu, sigma):
    '''
        This function takes a 2-dimensional list of size n (measurements);
        it starts as zeros but is filled with values +/- 2 standard deviations
        of the mean in one dimension, and the probabilities associated with
        those values in the other. The probabilities are calculated using a
        Gaussian (normal) distribution (for a probability density function)
        and integrating over small ranges about the values to obtain an
        approximate probability for a given value.
    '''
    
    pass


def monovariate_cont():
    '''Words'''
    pass


def monovariate_jump():
    '''Words'''
    pass


def bivariate_cont():
    '''words'''
    pass


def bivariate_jump():
    '''words'''
    pass


def trivariate():
    '''words'''
    pass



def to_file():
    pass


def plot2d():
    '''For plotting monovariate samples and static measurands'''
    pass


def plot3d():
    '''For plotting bivariate samples'''
    pass


def plot4d():
    '''For plotting trivariate samples'''
    pass
