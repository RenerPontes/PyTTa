# -*- coding: utf-8 -*-
"""
This is a package developed to perform acoustic and vibration measurements
and signal analysis.

Our current dependencies are:

    * Numpy
    * Scipy
    * Matplotlib
    * Numba
    * h5py
    * SoundDevice
    * SoundFile

We recommend using the Anaconda Python distribution.


You can install directly from PyPI for a stable but rarely updated version:

    ~ $ pip install pytta

Or directly from the repository with:

    ~ $ pip install git+https://github.com/pyttamaster/pytta.git


The documentation is available at:

    https://pytta.readthedocs.io/


To get started, try:

    >>> import pytta
    >>> pytta.default()
    >>> pytta.list_devices()


For further information, check the documentation.


Authors:
    João Vitor Gutkoski Paes, joao.paes@eac.ufsm.br
    Matheus Lazarin, matheus.lazarin@eac.ufsm.br

"""

# Importing .py files as submodules
from ._properties import default

# Instantiate the Default parameters to be loaded by other
# methods and function calls

from .classes import SignalObj, ImpulsiveResponse,\
    RecMeasure, PlayRecMeasure, FRFMeasure,\
    Streaming, Monitor,\
    OctFilter, weighting,\
    Analysis

from . import _h5utils
from . import _plot
from . import generate
from . import utils
from . import rooms
from . import iso3741

from .functions import read_wav, write_wav, merge, list_devices, get_device_from_user,\
    fft_convolve, find_delay, corr_coef, resample,\
    peak_time, save, load, fft_degree, plot_time, plot_time_dB, plot_freq,\
    plot_bars, plot_spectrogram, plot_waterfall

from .apps import roomir

__version__ = '0.1.0b8'  # package version

# package submodules and scripts to be called as pytta.something
__all__ = [  # Apps
           'roomir',

           # Submodules
           'generate',
           'utils',
           'iso3741',
           'rooms',

           # Functions
           'merge',
           'fft_convolve',
           'read_wav',
           'write_wav',
           'list_devices',
           'get_device_from_user',
           'find_delay',
           'resample',
           'corr_coef',
           'peak_time',
           'save',
           'load',
           'weighting',
           'fft_degree',
           'plot_time',
           'plot_time_dB',
           'plot_freq',
           'plot_bars',
           'plot_spectrogram',
           'plot_waterfall',

           # Classes
           'RecMeasure',
           'PlayRecMeasure',
           'FRFMeasure',
           'SignalObj',
           'ImpulsiveResponse',
           'Analysis',
           'OctFilter',
           'Monitor',
           'Streaming',

           # Objects
           'default']
