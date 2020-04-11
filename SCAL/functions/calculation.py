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

def Krw_Soc_ave(h,k,Krw):
    # Simple arithmetric average
    # Take input as numpy series
    h_k = np.sum(h * k)
    h_k_Krw = np.sum(h * k * Krw)
    result = h_k_Krw / h_k
    return result

def Kro_Swc_ave(h,k,Kro):
    # Simple arithmetric average
    # Take input as numpy series
    h_k = np.sum(h * k)
    h_k_Kro = np.sum(h * k * Kro)
    result = h_k_Kro / h_k
    return result

# def Krw_Normalize(Krw_)
