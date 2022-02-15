import pandas as pd
from pathlib import Path

#-----------------------------------------------------------
fd_out='./out/a00_clean_04_bc'
fd_in='./out/a00_clean_00_load'
l_freq=['500', '1000', '2000', '4000']

#------------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)


#######################################################################
for name in ['bcr', 'bcl']:
	df=pd.read_csv(f'{fd_in}/{name}.csv', index_col=0)
	
	#filter col
	l_col=[f'{name}_{i}' for i in l_freq]
	df=df.loc[:, l_col]
	
	#filter row
	df=df.loc[df.min(axis=1)>=0, :]
	df=df.loc[df.max(axis=1)<=120, :]
	
	df.to_csv(f'{fd_out}/{name}.csv')
	print(df.shape)
