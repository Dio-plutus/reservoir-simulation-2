import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import functions.calculation as cal


class Core:
    def __init__(self, name, depth, porosity, length, K_k, K_e_Swi, Sw, Krw, Kro):
       self.name = name
       self.depth = depth
       self.porosity = porosity
       self.length = length
       self.K_k = K_k
       self.K_e_Swi = K_e_Swi
       self.Sw = Sw
       self.Krw = Krw
       self.Kro = Kro

    def critical_spec(self):
        self.Kro_Swc = self.Kro[0]
        self.Krw_Soc = self.Krw[-1]
        return 0

    def normalized(self):
        self.Sw_Star = cal.Sw_Star(self.Sw)
        self.Krw_Star = cal.Krw_Star(self.Krw)
        self.Kro_Star = cal.Kro_Star(self.Kro)
        return 0

    
