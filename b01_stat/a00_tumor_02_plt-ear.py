import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a00_tumor_02_plt-ear'
f_in='./out/a00_tumor_00_clean/data_ear.csv'

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, index_col=0)

#--------------------------------------------------------
def plt_cnt(dfi, f_out, title=None, sz=(5,3), y='cnt', cmap='grey', ylbl='Count', ylim=[0, 45]):
	sns.set()
	sns.despine()
	#plot
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.barplot(x=dfi.index, y=y, data=dfi, color=cmap)
	#adjust
	ax.set_title(title, x=0.5, fontsize=14, weight='semibold', pad=10)
	ax.set_xlabel('')
	plt.ylabel(ylbl, fontsize=12, labelpad=10, weight='semibold')
	plt.xticks(fontsize=11, rotation=0, weight='semibold')
	plt.yticks(fontsize=8)
	ax.tick_params(axis='x', which='major', pad=4)
	ax.tick_params(axis='y', which='major', pad=-1)
	plt.ylim(ylim)
	#add text
	for i in range(dfi.shape[0]):
		text_x=i
		text_y=dfi[y][i]+1
		text=str(dfi[y][i])
		plt.text(text_x, text_y, text, weight='semibold', fontsize=10, ha='center')	
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()	
	return
	

########################################################################
#cnt size
dfi=df.copy()
dfi=dfi.loc[dfi['size']!='None', :]
dfi['cnt']=1

dfi['size']=pd.Categorical(dfi['size'], categories=['IC', 'Small', 'Medium', 'Large'], ordered=True)
dfi=dfi.groupby('size').agg({'cnt': 'count'})

#plot
f_out=f'{fd_out}/cnt.png'
title='Tumor Numbers'
plt_cnt(dfi, f_out, title=title)






