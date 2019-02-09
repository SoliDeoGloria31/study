# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
# data.plot()
# plt.show()

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list('ABCD'))
data = data.cumsum()
print(data.head())

# plot method:
# bar, hist, box, kde, area, scatter, hexbin, pie

ax = data.plot.scatter(x='A',y='B',c='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',c='DarkGreen',label='Class 2',ax=ax)
plt.show()


