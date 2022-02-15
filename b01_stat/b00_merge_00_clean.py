from pathlib import Path
import pandas as pd

#-----------------------------------------------------------
fd_out='./out/b00_merge_00_clean'
f_tumor='./out/a00_tumor_00_clean/data_ear.csv'
f_wc='./out/a01_wordrec_00_clean/data_ear.csv'
f_ac='./out/a02_ac_00_clean/data_ear.csv'
f_bc='./out/a03_bc_00_clean/data_ear.csv'
f_symp='./out/a04_symp_00_clean/data_ear.csv'

#----------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

#load
df_tumor=pd.read_csv(f_tumor, index_col=0)
df_wc=pd.read_csv(f_wc, index_col=0).drop('tumor', axis=1)
df_ac=pd.read_csv(f_ac, index_col=0).drop('tumor', axis=1)
df_bc=pd.read_csv(f_bc, index_col=0).drop('tumor', axis=1)
df_symp=pd.read_csv(f_symp, index_col=0).drop('tumor', axis=1)

###########################################################################
#merge
df=df_tumor.merge(df_wc, left_index=True, right_index=True)
df=df.merge(df_ac, left_index=True, right_index=True)
df=df.merge(df_bc, left_index=True, right_index=True)
df=df.merge(df_symp, left_index=True, right_index=True)

df.to_csv(f'{fd_out}/data.csv')
