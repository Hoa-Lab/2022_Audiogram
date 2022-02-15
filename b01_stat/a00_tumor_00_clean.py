from pathlib import Path
import pandas as pd

#------------------------------------------------------
prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a00_tumor_00_clean'
f_in=f'{prj}/b00_clean/out/a00_clean_06_merge/data.csv'

l_col=['tumor', 'side', 'size_r', 'size_l']

#------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

#load
df=pd.read_csv(f_in, index_col=0)
df=df.loc[:, l_col].copy()

####################################################################
#by case
df.to_csv(f'{fd_out}/data_case.csv')

#by ear --- concat
df0=df.loc[:, ['size_r']].copy()
df0.columns=['size']
df0.index=df0.index.map(lambda x: f'{x}_r')

df1=df.loc[:, ['size_l']].copy()
df1.columns=['size']
df1.index=df1.index.map(lambda x: f'{x}_l')

df=pd.concat([df0, df1])

#by ear --- add cols
df['tumor']='None'
df.loc[df['size']!='None', ['tumor']]='Tumor'

df.to_csv(f'{fd_out}/data_ear.csv')

