import numpy as np

def Sw_Star(Sw):
    Swc = Sw[0]
    Sw_Soc = Sw[-1]
    result = (Sw - Swc)/(Sw_Soc - Swc)
    return result

def Krw_Star(Krw):
    Krw_Soc = Krw[-1]
    result = Krw/Krw_Soc
    return result

def Kro_Star(Kro):
    Kro_Swc = Kro[0]
    result = Kro/Kro_Swc
    return result
