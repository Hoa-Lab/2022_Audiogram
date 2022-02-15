import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a02_ac_01_plt-case'
f_in='./out/a02_ac_00_clean/data_case.csv'
l_freq=['250', '500', '1000', '2000', '3000', '4000', '6000', '8000']
cmap=['#4287f5', '#48ed45', '#fc7742']

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#--------------------------------------------------------
def plt_box(df, f_out, title=None, sz=(8,3), cmap=cmap, ylbl='Abs Difference (Db)'):
	sns.set()
	sns.despine()
	#plot
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.boxplot(x='freq', y='diff', hue='side', data=df, palette=cmap, showfliers=False, linewidth=0.5)
	#adjust
	ax.set_title(title, x=0.5, fontsize=13, weight='semibold', pad=10)
	ax.set_xlabel('')
	plt.ylabel(ylbl, fontsize=10, labelpad=8, weight='semibold')
	plt.xticks(fontsize=10, rotation=0, weight='semibold')
	plt.yticks(fontsize=8)
	ax.tick_params(axis='x', which='major', pad=4)
	ax.tick_params(axis='y', which='major', pad=-1)
	plt.ylim([-10,80])
	plt.legend(loc=2, fontsize=3, frameon=True, prop=dict(weight='semibold', size=8))
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()	
	return

#####################################################################
#clean side
df.loc[df['side']=='Left', ['side']]='1-Side'
df.loc[df['side']=='Right', ['side']]='1-Side'
df.loc[df['side']=='Both', ['side']]='2-Side'
df['side']=pd.Categorical(df['side'], categories=['None', '1-Side', '2-Side'], ordered=True)

#stack df
l_df=[]
for freq in l_freq:
	dfi=df.loc[:, ['side', f'acr_{freq}', f'acl_{freq}']].copy()
	dfi['diff']=dfi[f'acr_{freq}']-dfi[f'acl_{freq}']
	dfi['diff']=dfi['diff'].abs()
	dfi=dfi.loc[:, ['side', 'diff']]
	dfi['freq']=f'ac_{freq}'
	l_df.append(dfi)
df=pd.concat(l_df)
df.to_csv(f'{fd_out}/data.csv')

#plot
f_out=f'{fd_out}/db.png'
title='Difference of Db (Air Conduct)'
plt_box(df, f_out, title=title)




