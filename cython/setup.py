# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:40:12 2024

@author: usuario
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
setup(ext_modules=cythonize('cy_sum.pyx'), 
      include_dirs=[np.get_include()], 
      requires=['Cython', 'numpy'])

