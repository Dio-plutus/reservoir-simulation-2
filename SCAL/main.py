##{
import pandas as pd
import numpy as np
import os
from classes.core import Core

list_file = np.array(os.listdir("Data/"))
sample_list = [x.split('.')[0] for x in list_file]

# Read and initiate data
for i in sample_list:
    core_data = pd.read_csv("Data/{}.csv".format(i), sep=',')
    globals()[i] = Core(core_data.loc[0][0], core_data.loc[0][1] 
                    , core_data.loc[0][2], core_data.loc[0][3]
                    , core_data.loc[0][4], core_data.loc[0][5]
                    , core_data['Sw'].to_numpy(), core_data['Krw'].to_numpy()
                    , core_data['Kro'].to_numpy())
    globals()[i].critical_spec()
    globals()[i].normalized()
##}
