# -*- coding: utf-8 -*-


'''
如果用 python 的列表和字典来作比较,
那么可以说 Numpy 是列表形式的，没有数值标签，
而 Pandas 就是字典形式。Pandas是基于Numpy构建的，
让Numpy为中心的应用变得更加简单。

.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
'''


import pandas as pd
import numpy as np

dates = pd.date_range('20180206', periods=6)

df = pd.DataFrame(
    np.arange(24).reshape(6, 4),
    index=dates,
    columns=[
        'A',
        'B',
        'C',
        'D'])
print(df)

# print(df.loc['20180208'])
#
# print(df.loc['20180208', ['A', 'B']])
#
# print(df.iloc[3:5, 1:3])
#
# print(df.ix[:3, ['A', 'C']])

df.iloc[1,2] = 111
df.loc['20180208','C']= 222
df.A[df.A>4] = 0

df['F'] = np.nan
print(df)

