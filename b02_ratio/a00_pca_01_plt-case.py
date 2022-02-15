import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

#----------------------------------------------------
fd_out='./out/a00_pca_01_plt-case'
f_in='./out/a00_pca_00_pp-case/data.csv'
cmap=['#4287f5', '#de8a35', '#38de35', '#eb3434']

#----------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#----------------------------------------------------
def plt_pca(df, f_out, title=None, sz=(5.5, 4), hue='side', cmap=cmap):
	sns.set()
	fig, ax=plt.subplots(figsize=sz)	
	sns.scatterplot(data=df, x='x', y='y', hue=hue, alpha=0.7, palette=cmap, s=15)
	#adjust
	ax.set_title(title, x=0.5, fontsize=15, weight='semibold', pad=15)
	plt.xlabel('PC 1')
	plt.ylabel('PC 2')
	plt.xticks([])
	plt.yticks([])
	plt.legend(loc=(1.0, 0), frameon=False, prop={'size': 12, 'weight': 'semibold'})
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()		
	return

##################################################################
f_out=f'{fd_out}/pca.png'
title='PCA (case)'
plt_pca(df, f_out, title=title)
