import numpy as np
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter


def fbin(x, width=2):
    '''bin the data with width
    '''
    return  x[:(x.size // width) * width].reshape(-1, width).mean(axis=1)

def frunning_mean(x, N=2):
    '''smooth data with N
    '''
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

def fsavgol_filter(x, window_length=51, polyorder=3, deriv=0, delta=1.0, axis=-1, mode='interp', cval=0.0):
    '''apply savgol_filter filter to data with window and order
    '''
    return savgol_filter(x, window_length=window_length, polyorder=polyorder, deriv=0, delta=1.0, axis=-1, mode='interp', cval=0.0)

def fgaussion_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0):
    '''apply gaussion filter to 2D image
    '''
    return gaussian_filter(input, sigma=sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)

