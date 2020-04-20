import numpy as np
import pandas as pd

class NeoDataFrame(pd.DataFrame):
    def __init__(self, data):
        super().__init__(data=data)

    def power_up(self):
        print('POWERRRRRRRRRRR')


x = np.random.normal(size=300)
df = NeoDataFrame(x.reshape((60, 5)))
print(type(df))
