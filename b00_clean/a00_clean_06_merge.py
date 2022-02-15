import pandas as pd
from pathlib import Path

#---------------------------------------------------
fd_out='./out/a00_clean_06_merge'
f_tumor='./out/a00_clean_01_tumor/data.csv'
f_wc='./out/a00_clean_02_wordrec/data.csv'
f_symp='./out/a00_clean_05_symp/data.csv'
fd_ac='./out/a00_clean_03_ac'
fd_bc='./out/a00_clean_04_bc'

#--------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)


#################################################################
#load
df_tumor=pd.read_csv(f_tumor, index_col=0)
df_wc=pd.read_csv(f_wc, index_col=0)
df_ac0=pd.read_csv(f'{fd_ac}/acl.csv', index_col=0)
df_ac1=pd.read_csv(f'{fd_ac}/acr.csv', index_col=0)
df_bc0=pd.read_csv(f'{fd_bc}/bcl.csv', index_col=0)
df_bc1=pd.read_csv(f'{fd_bc}/bcr.csv', index_col=0)
df_symp=pd.read_csv(f_symp, index_col=0)

#merge
df=df_tumor.merge(df_wc, left_index=True, right_index=True)
df=df.merge(df_ac0, left_index=True, right_index=True)
df=df.merge(df_ac1, left_index=True, right_index=True)
df=df.merge(df_bc0, left_index=True, right_index=True)
df=df.merge(df_bc1, left_index=True, right_index=True)
df=df.merge(df_symp, left_index=True, right_index=True)

df.to_csv(f'{fd_out}/data.csv')
