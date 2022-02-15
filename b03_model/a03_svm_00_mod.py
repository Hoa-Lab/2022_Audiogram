from pathlib import Path
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler

#------------------------------------------------------------
l_k=['poly', 'rbf', 'sigmoid']
l_r=['scale', 'auto']

prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a03_svm_00_mod'
f_in=f'{prj}/b00_clean/out/a00_clean_06_merge/data.csv'

#-------------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)
df=df.sample(frac=1)
scaler=MinMaxScaler()

############################################################################
#pp X and y
y=(df['tumor']=='Tumor').astype('int').values

df=df.drop(['side', 'size_r', 'size_l', 'tumor'], axis=1)
X=df.values
X=scaler.fit_transform(X)

#f1 score
l_data=[]
for k in l_k:
	for r in l_r:
		clf=SVC(kernel=k, gamma=r, C=500)
		s=cross_val_score(clf, X, y, cv=3, scoring='f1')
		avg=s.mean()
		std=s.std()
		l_data.append((f'{k}-{r}', avg, std))				
df=pd.DataFrame(l_data, columns=['param', 'avg', 'std'])
df['mod']=[f'svm-{i}' for i in range(1, df.shape[0]+1)]
df=df.set_index('mod')
df.to_csv(f'{fd_out}/f1_score.csv')

#accuracy score
l_data=[]
for k in l_k:
	for r in l_r:
		clf=SVC(kernel=k, gamma=r, C=500)
		s=cross_val_score(clf, X, y, cv=3, scoring='accuracy')
		avg=s.mean()
		std=s.std()
		l_data.append((f'{k}-{r}', avg, std))				
df=pd.DataFrame(l_data, columns=['param', 'avg', 'std'])
df['mod']=[f'svm-{i}' for i in range(1, df.shape[0]+1)]
df=df.set_index('mod')
df.to_csv(f'{fd_out}/accu_score.csv')


