import numpy as np
import pandas as pd

class DataFrame2(pd.DataFrame):
    def __init__(self, data):
        super().__init__(data=data)

    def do_something(self):
        print('do_something')


x = np.random.normal(size=300)
df = DataFrame2(x.reshape((60, 5)))
print(type(df))
