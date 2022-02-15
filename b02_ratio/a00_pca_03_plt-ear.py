import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

#----------------------------------------------------
fd_out='./out/a00_pca_03_plt-ear'
f_in='./out/a00_pca_02_pp-ear/data.csv'
l_cat=['None', 'IC', 'Small', 'Medium', 'Large']
cmap=['#4287f5', '#de8a35', '#38de35', '#eb3434', '#cc34eb']

#----------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)
df['size']=pd.Categorical(df['size'], categories=l_cat, ordered=True)

#----------------------------------------------------
def plt_pca(df, f_out, title=None, sz=(5.5, 4), hue='size', cmap=cmap):
	sns.set()
	fig, ax=plt.subplots(figsize=sz)	
	sns.scatterplot(data=df, x='x', y='y', hue=hue, alpha=0.7, palette=cmap, s=10)
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
#f_out=f'{fd_out}/pca.png'
#title='PCA (ear)'
#plt_pca(df, f_out, title=title)

df['size']=df['size'].astype('str')
df.loc[df['size']!='None', ['size']]='Tumor'
df['size']=pd.Categorical(df['size'], categories=['None', 'Tumor'], ordered=True)

f_out=f'{fd_out}/pca_2.png'
title='PCA (ear)'
plt_pca(df, f_out, title=title, cmap=['#4287f5', '#eb3434'])
