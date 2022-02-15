from pathlib import Path
import pandas as pd

#------------------------------------------------------------
fd_out='./out/a00_clean_02_wordrec'
f_in='./out/a00_clean_00_load/wordrec.csv'

#------------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

########################################################################
#only keep pct
df=df.loc[:, ['wordrec_r_1_pct', 'wordrec_l_1_pct']]
df.columns=['wordrec_r', 'wordrec_l']

#filter
df=df.loc[df['wordrec_r']>=0, :]
df=df.loc[df['wordrec_l']>=0, :]

df=df.loc[df['wordrec_r']<=100, :]
df=df.loc[df['wordrec_l']<=100, :]

df.to_csv(f'{fd_out}/data.csv')
