from pathlib import Path
import pandas as pd

#--------------------------------------------------------
prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a00_clean_00_load'
f_in=f'{prj}/a00_raw/data/KaylieAcousticNeurom-Include_DATA_2021-01-11_1323.csv'

l_feature=['tumor', 'symptom', 'wordrec', 'acr_', 'acl_', 'bcr_', 'bcl_']

#------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

####################################################################
l_all=df.columns.unique().tolist()

for feature in l_feature:
	l_col=[i for i in l_all if feature in i]
	df_tmp=df.loc[:, l_col].copy()
	df_tmp.to_csv(f'{fd_out}/{feature.strip("_")}.csv')



