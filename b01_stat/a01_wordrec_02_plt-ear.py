import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a01_wordrec_02_plt-ear'
f_in='./out/a01_wordrec_00_clean/data_ear.csv'
cmap=['#4287f5', '#f56f42']
cmap=['#828282', '#828282']

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#-------------------------------------------------------
def plt_box(df, f_out, title=None, sz=(3,3), cmap=cmap, ylbl='Percent (%)'):
	sns.set()
	sns.despine()
	#plot
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.boxplot(x='tumor', y='wordrec', data=df, palette=cmap, showfliers=False, linewidth=0.5)
	#adjust
	ax.set_title(title, x=0.5, fontsize=14, weight='semibold', pad=10)
	ax.set_xlabel('')
	plt.ylabel(ylbl, fontsize=12, labelpad=10, weight='semibold')
	plt.xticks(fontsize=11, rotation=0, weight='semibold')
	plt.yticks(fontsize=8)
	ax.tick_params(axis='x', which='major', pad=4)
	ax.tick_params(axis='y', which='major', pad=-1)
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()		
	return

#########################################################################
#plot
df['tumor']=pd.Categorical(df['tumor'], categories=['None', 'Tumor'], ordered=True)
f_out=f'{fd_out}/pct.png'
title='WordRec Percent'

plt_box(df, f_out, title=title)
