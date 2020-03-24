

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
        Kro_Swc = Sw[0]
        
