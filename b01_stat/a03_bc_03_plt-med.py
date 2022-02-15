import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a03_bc_03_plt-med'
f_in='./out/a03_bc_01_plt-case/data.csv'
l_freq=['500', '1000', '2000', '4000']
cmap=['#4287f5', '#48ed45', '#fc7742']

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#--------------------------------------------------------
def plt_line(df, f_out, title=None, cmap=cmap, sz=(4.5,3), ylbl='Abs Difference (Db)'):
	sns.set()
	sns.despine()
	#plot
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.lineplot(data=df, x='freq', y='diff', hue='side', markers=['o', 's', 'D'], style='side', palette=cmap, ci=None)
	#adjust
	ax.set_title(title, x=0.5, fontsize=13, weight='semibold', pad=10)
	ax.set_xlabel('')
	plt.ylabel(ylbl, fontsize=10, labelpad=8, weight='semibold')
	plt.xticks(fontsize=10, rotation=0, weight='semibold')
	plt.yticks(fontsize=8)
	ax.tick_params(axis='x', which='major', pad=4)
	ax.tick_params(axis='y', which='major', pad=-1)
	plt.ylim([-5,40])
	plt.legend(loc=2, fontsize=3, frameon=True, prop=dict(weight='semibold', size=8))
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()		
	return
	

#########################################################################
#plot
f_out=f'{fd_out}/bc.png'
title='Median Difference of Db (Bone Conduct)'
plt_line(df, f_out, title=title)


