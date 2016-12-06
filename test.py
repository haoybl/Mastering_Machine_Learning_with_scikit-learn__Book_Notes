
import numpy as np
import pandas as pd

dates = pd.date_range("1/2/2000", periods = 8)

df = pd.DataFrame(np.random.rand(8, 4), index = dates, columns = ["A", "B", "C", "D"])

print (df)



