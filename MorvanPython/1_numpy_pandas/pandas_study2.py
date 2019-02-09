# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# join, ('inner', 'outer')
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
# print(df1)
# print(df2)
# res = pd.concat([df1, df2], axis=1, join='outer')
# print(res)
# res = pd.concat([df1, df2], axis=1, join='inner')
# print(res)
# res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
# print(res)


# append
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
# res = df1.append(df2, ignore_index=True)
# print(res)
# res = df1.append([df2, df3])
# print(res)
# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# res = df1.append(s1, ignore_index=True)
#
# print(res)


# import pandas as pd
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                                   'A': ['A0', 'A1', 'A2', 'A3'],
#                                   'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                                     'C': ['C0', 'C1', 'C2', 'C3'],
#                                     'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# res = pd.merge(left,right,on='key')
# print(res)


# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                             'key2': ['K0', 'K1', 'K0', 'K1'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                              'key2': ['K0', 'K0', 'K0', 'K0'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# how = ['inner','outer','left','right']
res= pd.merge(left,right,on=['key1','key2'],how='inner')
print(res)
res= pd.merge(left,right,on=['key1','key2'],how='outer')
print(res)
res= pd.merge(left,right,on=['key1','key2'],how='left')
print(res)
res= pd.merge(left,right,on=['key1','key2'],how='right')
print(res)

