from pathlib import Path
import pandas as pd

#----------------------------------------------------------
prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/b00_ratio_00_avg'
f_in=f'{prj}/b00_clean/out/a00_clean_06_merge/data.csv'

d_meta={'low': ['250', '500'],
        'high_0': ['2000', '3000', '4000'],
        'high_1': ['2000', '3000', '4000', '6000', '8000'],
        'high_2': ['1000', '2000', '3000', '4000', '6000', '8000']
        }

#----------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#----------------------------------------------------------
def mainf(name):
	l=d_meta[name]
	l_r=[f'acr_{i}' for i in l]
	l_l=[f'acl_{i}' for i in l]
	
	#avg
	df_r=df.loc[:, l_r].copy()
	df_r['r']=df_r.mean(axis=1)
	df_r=df_r.loc[:, ['r']]

	df_l=df.loc[:, l_l].copy()
	df_l['l']=df_l.mean(axis=1)
	df_l=df_l.loc[:, ['l']]
	
	#merge
	dfi=df.loc[:, ['tumor']].merge(df_r, left_index=True, right_index=True)
	dfi=dfi.merge(df_l, left_index=True, right_index=True)
	
	#ratio
	dfi['r']=dfi['r']+0.1
	dfi['l']=dfi['l']+0.1
	dfi['ratio']=dfi['r']/dfi['l']
	dfi['ratio']=dfi['ratio'].apply(lambda x: x if x>=1 else 1/x)
	return dfi
	

#########################################################################
for name in d_meta.keys():
	df_tmp=mainf(name)
	df_tmp.to_csv(f'{fd_out}/{name}.csv')

