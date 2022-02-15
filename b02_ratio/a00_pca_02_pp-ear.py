from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA

#-----------------------------------------------------
prj='/mnt/c/Users/gus5/Desktop/a01_proj/a04_audiogram'
fd_out='./out/a00_pca_02_pp-ear'
f_in=f'{prj}/b01_stat/out/b00_merge_00_clean/data.csv'

#----------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

################################################################
#pca
df_pca=df.drop(['size', 'tumor'], axis=1).copy()
pca=PCA(n_components=2)
X=pca.fit_transform(df_pca.values)
df_pca=pd.DataFrame(X, index=df_pca.index, columns=['x', 'y'])

#save
df=df.loc[:, ['size']].merge(df_pca, left_index=True, right_index=True)
df.to_csv(f'{fd_out}/data.csv')
