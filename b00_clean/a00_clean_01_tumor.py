from pathlib import Path
import pandas as pd

#------------------------------------------------------
fd_out='./out/a00_clean_01_tumor'
f_in='./out/a00_clean_00_load/tumor.csv'
l_cat=['None', 'IC', 'Small', 'Medium', 'Large']

#------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0).fillna(0)

###################################################################
#remove duplicates (no duplicates)
df=df.loc[~df.index.duplicated()]  

#remove error
df['tmp']=df['r_tumor_size']+df['l_tumor_size']
df=df.loc[~((df['sidetumor']==0) & (df['tmp']>0)), :]   #no error
df=df.loc[~((df['sidetumor']!=0) & (df['tmp']==0)), :]   #error: 1025, 1044
df=df.drop('tmp', axis=1)

#clean
df.columns=['side', 'size_r', 'size_l']
df['side']=df['side'].replace([0, 1, 2, 3], ['None', 'Right', 'Left', 'Both'])
df['size_r']=df['size_r'].replace([0, 1, 2, 3, 4], l_cat)
df['size_l']=df['size_l'].replace([0, 1, 2, 3, 4], l_cat)
df['tumor']=(df['side']!='None').astype('int')
df['tumor']=df['tumor'].replace([0, 1], ['None', 'Tumor'])

df.to_csv(f'{fd_out}/data.csv')
