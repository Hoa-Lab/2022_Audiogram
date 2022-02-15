import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np

#----------------------------------------------------
fd_out='./out/b00_plt_01_bar'
fd_in='./out/b00_plt_00_pp'

#---------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
df0=pd.read_csv(f'{fd_in}/f1.csv', index_col=0)
df1=pd.read_csv(f'{fd_in}/accu.csv', index_col=0)

#--------------------------------------------------
def plt_bar(df, f_out, title=None, sz=(4,8)):
	#plot
	sns.set()
	fig, ax=plt.subplots(figsize=sz)
	ax=sns.barplot(data=df, x='avg', y=df.index, color='grey')
	ax.errorbar(df['avg'], np.arange(df.shape[0]), xerr=[np.zeros(df.shape[0]), df['std']], linestyle='none', color='Grey')
	#adjust
	ax.set_title(title, x=0.5, fontsize=18, weight='semibold', pad=15)	
	plt.xlabel('Score', fontsize=12, labelpad=8, weight='semibold')
	plt.ylabel('', fontsize=12, labelpad=8, weight='semibold')
	plt.ylim([28.5, -0.5])
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()	
	return


############################################################
#f1
f_out=f'{fd_out}/f1.png'
title='f1 Score'
plt_bar(df0, f_out, title=title)

#accuracy
f_out=f'{fd_out}/accu.png'
title='Accuracy Score'
plt_bar(df1, f_out, title=title)
