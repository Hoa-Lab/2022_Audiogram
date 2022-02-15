import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

#---------------------------------------------------------
fd_out='./out/b00_plt_00_pp'
fd_random='./out/a00_random_01_score'
fd_logreg='./out/a01_logreg_00_mod'
fd_rf='./out/a02_rf_00_mod'
fd_svm='./out/a03_svm_00_mod'
fd_dl='./out/a04_dl_02_score'

#---------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

######################################################################
#load dl
df_train=pd.read_csv(f'{fd_dl}/score_train.csv', index_col=0)
df_test=pd.read_csv(f'{fd_dl}/score_test.csv', index_col=0)

df0_train=pd.DataFrame({'avg': df_train['f1']})
df0_train['std']=0
df0_train.index=df0_train.index.map(lambda x: f'{x}-train')
df0_test=pd.DataFrame({'avg': df_test['f1']})
df0_test['std']=0
df0_test.index=df0_test.index.map(lambda x: f'{x}-test')

df1_train=pd.DataFrame({'avg': df_train['accu']})
df1_train['std']=0
df1_train.index=df1_train.index.map(lambda x: f'{x}-train')
df1_test=pd.DataFrame({'avg': df_test['accu']})
df1_test['std']=0
df1_test.index=df1_test.index.map(lambda x: f'{x}-test')


#-------------------------f1-----------------------------
#load
df0_random=pd.read_csv(f'{fd_random}/f1_score.csv', index_col=0)
df0_logreg=pd.read_csv(f'{fd_logreg}/f1_score.csv', index_col=0)
df0_rf=pd.read_csv(f'{fd_rf}/f1_score.csv', index_col=0)
df0_svm=pd.read_csv(f'{fd_svm}/f1_score.csv', index_col=0)

df0=pd.concat([df0_random, df0_logreg, df0_rf, df0_svm, df0_train, df0_test])
df0=df0.drop('param', axis=1)
df0.to_csv(f'{fd_out}/f1.csv')

#-------------------------accurac-------------------------
#load
df1_random=pd.read_csv(f'{fd_random}/accu_score.csv', index_col=0)
df1_logreg=pd.read_csv(f'{fd_logreg}/accu_score.csv', index_col=0)
df1_rf=pd.read_csv(f'{fd_rf}/accu_score.csv', index_col=0)
df1_svm=pd.read_csv(f'{fd_svm}/accu_score.csv', index_col=0)

df1=pd.concat([df1_random, df1_logreg, df1_rf, df1_svm, df1_train, df1_test])
df1=df1.drop('param', axis=1)
df1.to_csv(f'{fd_out}/accu.csv')












