import numpy as np
import pickle
from pathlib import Path
import tensorflow.keras as keras

#--------------------------------------------------------
fd_out='./out/a04_dl_01_mod'
fd_in='./out/a04_dl_00_pp'
fd_mod=f'{fd_out}/mod_2'  #mod0 - {0: 0.2, 1: 0.8}, 1 - {0: 0.5, 1: 0.5}, 2 - {0: 0.8, 1: 0.2}
fd_log=f'{fd_out}/log_2'

d_weight={0: 0.8, 1: 0.2}

#---------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

#---------------------------------------------------------    
def build_mod():
	model=keras.models.Sequential([
		keras.layers.Input((36,)),
		keras.layers.Dropout(0.1),
		keras.layers.Dense(300, activation='swish', kernel_initializer='he_normal', kernel_regularizer=keras.regularizers.L1(0.001)),
		keras.layers.Dropout(0.1),
		keras.layers.Dense(300, activation='swish', kernel_initializer='he_normal', kernel_regularizer=keras.regularizers.L1(0.001)),
		keras.layers.Dense(2, activation='softmax')	
		])
	#compile
	opt=keras.optimizers.Adam(learning_rate=0.0001)
	model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['binary_crossentropy'])
	print(model.summary())
	return model

####################################################################
#load
X=np.load(f'{fd_in}/X_train.npy')
y=np.load(f'{fd_in}/y_train.npy')
y=keras.utils.to_categorical(y)

#build mode
model=build_mod()

#train
cb_checkpoint=keras.callbacks.ModelCheckpoint(fd_mod, save_best_only=True)
cb_tensorboard=keras.callbacks.TensorBoard(fd_log)

history=model.fit(X, y, epochs=50, batch_size=16, callbacks=[cb_checkpoint, cb_tensorboard], validation_split=0.1, class_weight=d_weight)


