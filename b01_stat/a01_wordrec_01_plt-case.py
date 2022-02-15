import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a01_wordrec_01_plt-case'
f_in='./out/a01_wordrec_00_clean/data_case.csv'
cmap=['#4287f5', '#48ed45', '#fc7742']
cmap=['#828282', '#828282', '#828282']

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#--------------------------------------------------------
def plt_box(df, f_out, title=None, sz=(4,3), ylbl='Abs Difference (%)', cmap=cmap, ylim=[-10, 60]):
	sns.set()
	sns.despine()
	#plot
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.boxplot(x='side', y='diff', data=df, palette=cmap, showfliers=False, linewidth=0.5)
	#adjust
	ax.set_title(title, x=0.5, fontsize=14, weight='semibold', pad=10)
	ax.set_xlabel('')
	plt.ylabel(ylbl, fontsize=12, labelpad=10, weight='semibold')
	plt.xticks(fontsize=11, rotation=0, weight='semibold')
	plt.yticks(fontsize=8)
	ax.tick_params(axis='x', which='major', pad=4)
	ax.tick_params(axis='y', which='major', pad=-1)
	plt.ylim(ylim)
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()		
	return


#####################################################################
#difference
df['diff']=df['wordrec_r']-df['wordrec_l']
df['diff']=df['diff'].abs()

#rename side
df.loc[df['side']=='Left', ['side']]='1-Side'
df.loc[df['side']=='Right', ['side']]='1-Side'
df.loc[df['side']=='Both', ['side']]='2-Side'
df['side']=pd.Categorical(df['side'], categories=['None', '1-Side', '2-Side'], ordered=True)

#plot
f_out=f'{fd_out}/diff.png'
title='Percent Difference'
plt_box(df, f_out, title=title)


