#://stats.stackexchange.com/questions/375950/how-to-calculate-the-p-value-of-a-test-that-checked-for-a-binary-property

import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import fisher_exact

#-----------------------------------------------
fd_out='./out/c00_symp_00_fisher'
f_in='./out/a04_symp_00_clean/data_ear.csv'
l_symp=['tinnitus', 'fullness', 'shl', 'ghl']

#---------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#################################################################
l_data=[]
for symp in l_symp:
    #clean
    df_ctrl=df.loc[df['tumor']=='None', [symp]].copy()
    df_tumor=df.loc[df['tumor']=='Tumor', [symp]].copy()
    #prepare
    l_ctrl=[df_ctrl.shape[0], df_ctrl[symp].sum()]
    l_tumor=[df_tumor.shape[0], df_tumor[symp].sum()]
    obs=np.array([l_ctrl, l_tumor])
    
    #Fisher Exact
    oddsr, pval=fisher_exact(obs)
    l_data.append((symp, oddsr, pval))
	
df=pd.DataFrame(l_data, columns=['symptom', 'odds_ratio', 'pval'])
df.to_csv(f'{fd_out}/data.csv', index=False)
