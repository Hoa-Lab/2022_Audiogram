import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------
fd_out='./out/a00_tumor_01_plt-case'
f_in='./out/a00_tumor_00_clean/data_case.csv'

#--------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

#load
df=pd.read_csv(f_in, index_col=0)
df['side']=pd.Categorical(df['side'], categories=['None', 'Left', 'Right', 'Both'], ordered=True)

#--------------------------------------------------------
def plt_cnt(dfi, f_out, title=None, sz=(5,3), y='cnt', cmap='grey', ylbl='Count', ylim=[0, 320]):
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
		text_y=dfi[y][i]+10
		text=str(dfi[y][i])
		plt.text(text_x, text_y, text, weight='semibold', fontsize=10, ha='center')	
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()	
	return


##################################################################
#cnt side
dfi=df.copy()
dfi['cnt']=1
dfi=dfi.groupby('side').agg({'cnt': 'count'})

#plot
f_out=f'{fd_out}/cnt.png'
title='Case Numbers'
plt_cnt(dfi, f_out, title=title)


