from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#-------------------------------------------------------------
prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a04_dl_00_pp'
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

#split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)

#save
np.save(f'{fd_out}/X_train', X_train)
np.save(f'{fd_out}/y_train', y_train)
np.save(f'{fd_out}/X_test', X_test)
np.save(f'{fd_out}/y_test', y_test)
