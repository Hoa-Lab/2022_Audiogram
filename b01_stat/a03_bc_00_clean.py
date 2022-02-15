from pathlib import Path
import pandas as pd

#------------------------------------------------------
prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a03_bc_00_clean'
f_in=f'{prj}/b00_clean/out/a00_clean_06_merge/data.csv'
l_freq=['500', '1000', '2000', '4000']

#------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

###################################################################
#load
l0=[f'bcr_{i}' for i in l_freq]
l1=[f'bcl_{i}' for i in l_freq]
l_col=['side']+l0+l1
df=df.loc[:, l_col].copy()

#by case
df.to_csv(f'{fd_out}/data_case.csv')

#by ear --- clean
df0=df.loc[:, ['side']+l0].copy()
df0.columns=['side']+[f'bc_{i}' for i in l_freq]

df1=df.loc[:, ['side']+l1].copy()
df1.columns=['side']+[f'bc_{i}' for i in l_freq]

#by ear --- clean tumor info
df0['tumor']='None'
df0.loc[df0['side']=='Both', ['tumor']]='Tumor'
df0.loc[df0['side']=='Right', ['tumor']]='Tumor'
df0.index=df0.index.map(lambda x: f'{x}_r')

df1['tumor']='None'
df1.loc[df1['side']=='Both', ['tumor']]='Tumor'
df1.loc[df1['side']=='Left', ['tumor']]='Tumor'
df1.index=df1.index.map(lambda x: f'{x}_l')

#by ear --- concat
df=pd.concat([df0, df1])
df=df.drop('side', axis=1)

df.to_csv(f'{fd_out}/data_ear.csv')
