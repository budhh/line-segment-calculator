import sympy as sp
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import *
from sympy.parsing.mathematica import *

input = input("Input: ")
test = parse_mathematica(input)

print(test)
