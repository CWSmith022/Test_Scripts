# %%
# Secret file used for loading data, masking data source from github.
import pandas as pd

class secret_data:
    def __init__(self, data = '', remember_path = True):
        
        self.data = data
        self.count = 0
        self.remember_path = remember_path
    
    def load_data(self):
        
        if (self.remember_path == True and self.count == 0):
            data_path = input('Please insert data file path: ')
            self.count = self.count + 1
        elif (self.remember_path == True and self.count > 0):
            pass
        else:
            data_path = input('Please insert data file path: ')
            
        self.data_path = data_path
        df_path_sub = self.data_path[1:-1].replace('//', '\\\\')
        df = pd.read_csv(df_path_sub)
        return df

# %%
