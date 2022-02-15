from pathlib import Path
import pandas as pd

#-------------------------------------------------------------
fd_out='./out/a00_clean_05_symp'
f_in='./out/a00_clean_00_load/symptom.csv'
l_feature=['tinnitus', 'fullness', 'shl', 'ghl']

d_symp={'symptoms___1': 'tinnitus_r', 
          'symptoms___2': 'tinnitus_l', 
          'symptoms___3': 'tinnitus_b', 
          'symptoms___4': 'dizziness',
          'symptoms___5': 'ahl_r', 
          'symptoms___6': 'ahl_l', 
          'symptoms___7': 'fullness_r', 
          'symptoms___8': 'fullness_l',
          'symptoms___9': 'shl_r', 
          'symptoms___10': 'shl_l', 
          'symptoms___11': 'ghl_r', 
          'symptoms___12': 'ghl_l',
          'symptoms___13': 'fullness_b', 
          'symptoms___14': 'shl_b', 
          'symptoms___15': 'ghl_b'}
          
#-------------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)
df.columns=[d_symp[i] for i in df.columns]

########################################################################
#clean
for feature in l_feature:
	df.loc[df[f'{feature}_b']==1, [f'{feature}_r', f'{feature}_l']]=1
	df=df.drop(f'{feature}_b', axis=1)

df=df.drop('dizziness', axis=1)
df=df.dropna()

df.to_csv(f'{fd_out}/data.csv')	


