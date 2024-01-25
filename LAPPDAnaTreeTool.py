import uproot
import pandas as pd
import matplotlib.pyplot as plt

class LAPPDAnaTree:
    def __init__(self, pathfile):
        self.pathfile =  pathfile
    
    def readVariables(self, variable1, variable2, stripN, treename):
       # use uproot to read the tree and the branch
        print("Reading the rootfile ...")
        print(self.pathfile)
        fulluprootline = self.pathfile + ":" + treename

        my_data = uproot.concatenate([fulluprootline],filter_name=[variable1, variable2],library="pd")
        filtered_data = []
        
        # Loop over the event and cut based on 'lappdid'
        for index, row in my_data.iterrows():
            for br in row[variable2]:
                print(br)
                if br == int(stripN):
                    filtered_data.append(row[variable1][row[variable2].index(br)])

        # Moving to pandas DataFrame
        filtered_data_pd = pd.DataFrame(filtered_data, columns=[variable1])
        return filtered_data_pd


    def readVariable(self, variable, stripN, treename):

        # use uproot to read the tree and the branch
        print("Reading the rootfile ...")
        print(self.pathfile)
        fulluprootline = self.pathfile + ":" + treename

        my_data = uproot.concatenate([fulluprootline],filter_name=[variable],library="pd")
        # my_data[variable1][0:my_data[variable1].size].tolist() converst to a list
        # [subset[stripN] for subset in <list>] selects the column stripN of each element 
        filtered_data = [subset[stripN] for subset in my_data[variable1][0:my_data[variable1].size].tolist()] 
        filtered_data_pd = pd.DataFrame(filtered_data, columns=[variable1])

        return filtered_data_pd

strip_number = 50
variable1 = "StripPeak" #"pulseamp_simp"
variable2 = "pulsestrip_simp"
general_path = "/Users/marvinascenciososa/Desktop/pnfs_mrvn/ANNIE/Lab_6/LAPPD39/LAPPD39_output/new_branch/LAPPD63/SPP_LAPPD63/"

#ND4 = LAPPDAnaTree(general_path + "Analysis_2265_4ND.root")
#ND4_data = ND4.readVariable(variable1, strip_number, "ffmytree")

#ND41 = LAPPDAnaTree(general_path + "Analysis_2265_4.3ND.root")
#ND4_data1 = ND41.readVariable(variable1, strip_number, "ffmytree")

ND4 = LAPPDAnaTree(general_path + "Analysis_2215_4ND.root")
ND4_data = ND4.readVariable(variable1, strip_number, "ffmytree")

ND41 = LAPPDAnaTree(general_path + "Analysis_2240_4ND.root")
ND4_data1 = ND41.readVariable(variable1, strip_number, "ffmytree")

ND42 = LAPPDAnaTree(general_path + "Analysis_2265_4ND.root")
ND4_data2 = ND42.readVariable(variable1, strip_number, "ffmytree")

'''
ND4 = LAPPDAnaTree(general_path + "Analysis_2215_4ND.root")
ND4_data = ND4.readVariables(variable1, variable2, strip_number, "ffmytree")

ND41 = LAPPDAnaTree(general_path + "Analysis_2240_4ND.root")
ND4_data1 = ND41.readVariables(variable1, variable2, strip_number, "ffmytree")

ND42 = LAPPDAnaTree(general_path + "Analysis_2265_4ND.root")
ND4_data2 = ND42.readVariables(variable1, variable2, strip_number, "ffmytree")
'''

# Plotting stuff
fig,ax = plt.subplots()

#plt.hist(ND4_data,  bins=200,label='Strip 20, 7.5 mV t, 2265V, 30kEvents, 4.0 ND', histtype='step')
#plt.hist(ND4_data1, bins=200,label='Strip 20, 7.5 mV t, 2265V, 50kEvents, 4.3 ND', histtype='step')

plt.hist(ND4_data,  bins=200,label='Strip 20, 7.5 mV t, 2215V, 30kEvents, 4.0 ND', histtype='step')
plt.hist(ND4_data1, bins=200,label='Strip 20, 7.5 mV t, 2240V, 30kEvents, 4.0 ND', histtype='step')
plt.hist(ND4_data2, bins=80,label='Strip 20, 7.5 mV t, 2265V, 30kEvents, 4.0 ND', histtype='step')
plt.yscale('log')
plt.title('Strip Peak')
#ax.set_xlabel("Pulse Amplitude [mV]",fontsize=14)
ax.set_xlabel("Amplitude mV",fontsize=14)
ax.set_ylabel("Entries",fontsize=14)
plt.legend()
plt.show()
