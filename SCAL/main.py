#%%
import pandas as pd
import numpy as np
import os
from classes.core import Core
import functions.calculation as cal
import functions.array as arr

list_file = np.array(os.listdir("Data/"))
sample_list = [x.split('.')[0] for x in list_file]

# Create empty np array to store the h,k,Krw,Kro for all example
names = list()
h = arr.nans(len(sample_list))
k = arr.nans(len(sample_list))
Krw_Soc = arr.nans(len(sample_list))
Kro_Swc = arr.nans(len(sample_list))

# Indicator to write/count
j = 0

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
    # Create DataFrame consist of all cores data, consist of name, h, k, Krw, Kro of all example
    names.append(globals()[i].name)
    h[j] = globals()[i].h
    k[j] = globals()[i].K_k
    Krw_Soc[j] = globals()[i].Krw_Soc
    Kro_Swc[j] = globals()[i].Kro_Swc
    j = j + 1

all_samples = pd.DataFrame({'h': h,'K': k, 'Krw_Soc': Krw_Soc, 'Kro_Swc': Kro_Swc, 'Sample Name': names})
all_samples.set_index('Sample Name', inplace=True)

Krw_Soc_ave = cal.Krw_Soc_ave(all_samples.h, all_samples.K, all_samples.Krw_Soc)
Kro_Swc_ave = cal.Kro_Swc_ave(all_samples.h, all_samples.K, all_samples.Kro_Swc)
#%%


# Now we calculate normalized Kro_Star and Krw_Star with Sw_Star

Sw_Star = np.linspace(0,1,11)

#%%
