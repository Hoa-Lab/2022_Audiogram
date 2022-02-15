from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------
fd_out='./out/b00_ratio_01_plt-line'
fd_in='./out/b00_ratio_00_avg'
cmap=['#4287f5', '#f56f42']

#---------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#---------------------------------------------------
#def plt_main(df, f_out, title=None, sz=(6,4)):  #this is using 1 y axis
#	#plot
#	sns.set()
#	fig, ax=plt.subplots(figsize=sz)
#	ax=sns.lineplot(data=df, x='x', y='data', hue='hue', palette=cmap)
#	#adjust
#	ax.set_title(title, x=0.5, fontsize=18, weight='semibold', pad=15)
#	plt.xlabel('Ratio Threshold', fontsize=12, labelpad=8, weight='semibold')
#	plt.ylabel('Percent', fontsize=12, labelpad=8, weight='semibold')
#	plt.legend(loc='best', fontsize=6, frameon=True, prop=dict(weight='semibold'))
#	#save
#	plt.tight_layout()
#	plt.savefig(f_out, dpi=300)
#	plt.close()	
#	return

def plt_main(df0, df1, f_out, title=None, sz=(6,4)):
	#plot
	fig, ax0=plt.subplots(figsize=sz)
	ax0=sns.lineplot(data=df0, x='x', y='data', color=cmap[0])
	#adjust
	ax0.set_title(title, x=0.5, fontsize=18, weight='semibold', pad=15)
	plt.xlabel('Ratio Threshold', fontsize=12, labelpad=8, weight='semibold')
	ax0.set_ylabel('Accuracy %', fontsize=12, labelpad=8, weight='semibold', color=cmap[0])
	plt.ylim([-5, 105])
	#ax1
	ax1=ax0.twinx()
	ax1=sns.lineplot(data=df1, x='x', y='data', color=cmap[1])
	ax1.set_ylabel('Tumor Identified %', fontsize=12, labelpad=8, weight='semibold', color=cmap[1])
	plt.ylim([-5, 105])
	#save
	plt.tight_layout()
	plt.savefig(f_out, dpi=300)
	plt.close()	
	return


def mainf(fname, n=10):
	name=Path(fname).stem
	df=pd.read_csv(fname, index_col=0)
	df['tumor']=(df['tumor']=='Tumor').astype('int')
	
	#make df
	l_val=list(np.arange(1, n, 0.1))
	l_data=[]
	for val in l_val:
		#true pos
		dfi=df.loc[df['ratio']>=val, :].copy()
		tp=dfi['tumor'].mean()
		#tumor identified %
		n=dfi['tumor'].sum()/df['tumor'].sum()
		l_data.append((val, tp, n))	
	df=pd.DataFrame(l_data, columns=['x', 'tp', 'n']).fillna(0)	
	
	#pp
	df0=df.loc[:, ['x', 'tp']]
	df0.columns=['x', 'data']
	#df0['hue']='Accuracy %'
	df0['data']=df0['data']*100
	
	df1=df.loc[:, ['x', 'n']]
	df1.columns=['x', 'data']
	#df1['hue']='Tumor Identified %'	
	df1['data']=df1['data']*100
	
	#plot
	f_out=f'{fd_out}/{name}.png'
	plt_main(df0, df1, f_out, title='Ratio Test')	
	return
	
	
################################################################
for fname in l_fname:
	mainf(fname)







