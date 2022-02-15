import pandas as pd
import numpy as np
import pickle
import tensorflow.keras as keras
from sklearn.metrics import f1_score, accuracy_score
from pathlib import Path
from sklearn.metrics import confusion_matrix

#--------------------------------------------------------
fd_out='./out/a04_dl_02_score'
fd_mod='./out/a04_dl_01_mod'
fd_in='./out/a04_dl_00_pp'

#-------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

#-------------------------------------------------------
def get_score(X, y, model):
	#pred
	y_pred=model.predict(X)
	y_pred=np.argmax(y_pred, axis=1)
	df_mtx=pd.DataFrame(confusion_matrix(y, y_pred, labels=None), columns=['None_p', 'Tumor_p'], index=['None_t', 'Tumor_t'])
	#score
	f1=f1_score(y, y_pred)
	accu=accuracy_score(y, y_pred)
	return df_mtx, f1, accu

####################################################################
#train
X=np.load(f'{fd_in}/X_train.npy')
y=np.load(f'{fd_in}/y_train.npy')

l_data=[]
for i in range(3):
	#pp
	model=keras.models.load_model(f'{fd_mod}/mod_{i}')
	#get score
	df, f1, accu=get_score(X, y, model)
	df.to_csv(f'{fd_out}/train_{i}.csv')
	l_data.append((f'dl-{i}', f1, accu))
df=pd.DataFrame(l_data, columns=['mod', 'f1', 'accu'])	
df.to_csv(f'{fd_out}/score_train.csv', index=False)

#---------------------------------------------------------
#test
X=np.load(f'{fd_in}/X_test.npy')
y=np.load(f'{fd_in}/y_test.npy')

l_data=[]
for i in range(3):
	#pp
	model=keras.models.load_model(f'{fd_mod}/mod_{i}')
	#get score
	df, f1, accu=get_score(X, y, model)
	df.to_csv(f'{fd_out}/test_{i}.csv')
	l_data.append((f'dl-{i}', f1, accu))
df=pd.DataFrame(l_data, columns=['mod', 'f1', 'accu'])	
df.to_csv(f'{fd_out}/score_test.csv', index=False)








