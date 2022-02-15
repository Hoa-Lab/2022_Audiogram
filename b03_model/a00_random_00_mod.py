from pathlib import Path
import pandas as pd
import numpy as np

#-----------------------------------------------------------
n=5

prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a00_random_00_mod'
f_in=f'{prj}/b00_clean/out/a00_clean_06_merge/data.csv'

#-----------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

##########################################################################
#clean df
df=df.loc[:, ['tumor']].copy()
df['tumor']=(df['tumor']=='Tumor').astype('int')  #21% tumor

#random predict
for i in range(n):
	col=f'r{i}'
	df[col]=np.random.randint(1, 101, size=df.shape[0])
	
df.to_csv(f'{fd_out}/data.csv')
