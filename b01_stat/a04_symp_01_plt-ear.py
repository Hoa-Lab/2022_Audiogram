import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a04_symp_01_plt-ear'
f_in='./out/a04_symp_00_clean/data_ear.csv'
l_feature=['tinnitus', 'fullness', 'shl', 'ghl']
cmap=['#4287f5', '#f56f42']

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)
df['tumor']=pd.Categorical(df['tumor'], categories=['None', 'Tumor'], ordered=True)

#-------------------------------------------------------
def plt_bar(df, f_out, title=None, sz=(4,3), cmap=cmap, ylbl='Percent (%)'):
	sns.set()
	sns.despine()
	#plot
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.barplot(x='feature', y='pct', hue='tumor', data=df, palette=cmap)
	#adjust
	ax.set_title(title, x=0.5, fontsize=13, weight='semibold', pad=10)
	ax.set_xlabel('')
	plt.ylabel(ylbl, fontsize=10, labelpad=8, weight='semibold')
	plt.xticks(fontsize=10, rotation=0, weight='semibold')
	plt.yticks(fontsize=8)
	ax.tick_params(axis='x', which='major', pad=4)
	ax.tick_params(axis='y', which='major', pad=-1)
	plt.ylim([-5, 105])
	plt.legend(loc=2, fontsize=4, frameon=True, prop=dict(weight='semibold', size=8))
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()	
	return
	
	
####################################################################
#stack df
l_df=[]
for col in l_feature:
	dfi=df.loc[:, [col, 'tumor']].copy()
	dfi.columns=['data', 'tumor']
	dfi['feature']=col
	l_df.append(dfi)
df=pd.concat(l_df)	

#pp
df_sum=df.groupby(['tumor', 'feature']).sum()
df_cnt=df.groupby(['tumor', 'feature']).count()
df=df_sum.merge(df_cnt, left_index=True, right_index=True)
df['pct']=(df['data_x']/df['data_y'])*100
df=df.loc[:, ['pct']].reset_index()
df['feature']=pd.Categorical(df['feature'], categories=l_feature, ordered=True)

#plot
f_out=f'{fd_out}/symp.png'
title='Symptoms'
plt_bar(df, f_out, title=title)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		

















