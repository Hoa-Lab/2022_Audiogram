from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, accuracy_score

#----------------------------------------------------------
l_pct=[0, 20, 50, 80, 100]
n=5
fd_out='./out/a00_random_01_score'
f_in='./out/a00_random_00_mod/data.csv'

#-----------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#-----------------------------------------------------------
def get_f1(df, name):
	#pp
	y_true=df['tumor']
	df_tmp=df.drop('tumor', axis=1).copy()
	#get score
	l_data=[]
	for pct in l_pct:
		df_pred=(df_tmp>pct).astype('int')  #20 means 80% predict tumor
		l_score=[f1_score(y_true, df_pred[col]) for col in df_pred.columns]
		avg=np.array(l_score).mean()
		std=np.array(l_score).std()
		l_data.append((f'{name}-{pct}', avg, std))
	df_tmp=pd.DataFrame(l_data, columns=['mod', 'avg', 'std'])
	return df_tmp

	
def get_accu(df, name):
	#pp
	y_true=df['tumor']
	df_tmp=df.drop('tumor', axis=1).copy()	
	#get score
	l_data=[]
	for pct in l_pct:
		df_pred=(df_tmp>pct).astype('int')  #20 means 80% predict tumor
		l_score=[accuracy_score(y_true, df_pred[col]) for col in df_pred.columns]
		avg=np.array(l_score).mean()
		std=np.array(l_score).std()
		l_data.append((f'{name}-{pct}', avg, std))
	df_tmp=pd.DataFrame(l_data, columns=['mod', 'avg', 'std'])
	return df_tmp


############################################################################
#score
name='random'
df_f1=get_f1(df, name)
df_accu=get_accu(df, name)

#save
df_f1.to_csv(f'{fd_out}/f1_score.csv', index=False)
df_accu.to_csv(f'{fd_out}/accu_score.csv', index=False)

print(df_f1)
print(df_accu)





