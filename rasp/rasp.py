import os,cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split

from keras import backend as K
K.set_image_dim_ordering('tf')

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D

PASTA_DE_DADOS = 'Imagens_SHM'
SENSOR_NUMERO = 'S1'
REDUZIR_IMAGEM_PARA = 128
NUMERO_EPOCAS = 2

data_path = os.getcwd() + '//' + PASTA_DE_DADOS + '//' + SENSOR_NUMERO
data_dir_list = os.listdir(data_path)
num_channel=1
linhas_img = REDUZIR_IMAGEM_PARA
colunas_img = REDUZIR_IMAGEM_PARA

lista_imgs=[]                                                                   

def image_to_feature_vector(image, size=(linhas_img, colunas_img)):
    return cv2.resize(image, size).flatten()

for classe in data_dir_list:
    classe_path = data_path+'/'+ classe
    img_list=os.listdir(classe_path)
    for img in img_list:
        input_img=cv2.imread(data_path + '/'+ classe + '/'+ img )
        input_img = input_img[49:585, 114:792]
        input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        input_img_flatten=image_to_feature_vector(input_img,(linhas_img,colunas_img))
        lista_imgs.append(input_img_flatten)
from sklearn.preprocessing import scale

np_lista_imgs = np.array(lista_imgs)
np_lista_imgs = np_lista_imgs.astype('float32')
imgs_padronizadas = scale(np_lista_imgs)
imgs_padronizadas= imgs_padronizadas.reshape(np_lista_imgs.shape[0],linhas_img,colunas_img,num_channel)

num_classes = 4

num_amostras = imgs_padronizadas.shape[0]
labels = np.ones((num_amostras,),dtype='int64')

labels[0:60]=0
labels[60:120]=1
labels[120:180]=2
labels[180:]=3

names = ['d1','d2','d3','integro']

Y = np_utils.to_categorical(labels, num_classes)

input_shape=imgs_padronizadas[0].shape

model = Sequential()

model.add(Convolution2D(filters = 32,kernel_size = (3,3), padding = 'same',input_shape = input_shape))
model.add(Activation('relu'))

model.add(Convolution2D(filters = 32,kernel_size = (3, 3)))
model.add(Activation(activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(rate = 0.5))

model.add(Convolution2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

'''
model.summary()
model.get_config()
model.layers[0].get_config()
model.layers[0].input_shape
model.layers[0].output_shape
model.layers[0].get_weights()
np.shape(model.layers[0].get_weights()[0])
model.layers[0].trainable
'''

x,y = shuffle(imgs_padronizadas,Y, random_state=2)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=2)

model.fit(x = X_train,y = y_train,batch_size=16,epochs=NUMERO_EPOCAS,verbose=1,validation_data=(X_test, y_test))

'''
#################### Avaliar uma imagem ############################

IMAGEM_TESTADA_PATH = 'Imagens_SHM/S2/Dano2_S2/d3.jpg'

#       Descomente para avaliar todas as imagens no bloco de validação.

#score = model.evaluate(X_test, y_test, True, 0)
#print('Test Loss:', score[0])
#print('Test accuracy:', score[1])
#test_image = X_test
#model.predict_classes(test_image, batch_size=8, verbose=1)
#print(y_test[0:1])



test_image = cv2.imread(IMAGEM_TESTADA_PATH)
test_image = test_image[49:585, 114:792]

test_image=cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
test_image=cv2.resize(test_image,(linhas_img,colunas_img))
test_image = np.array(test_image)
test_image = test_image.astype('float32')
test_image /= 255


test_image= np.expand_dims(test_image, axis=3)
test_image= np.expand_dims(test_image, axis=0)


print((model.predict(test_image)))
print(model.predict_classes(test_image))


####################################################################
'''

from keras.models import model_from_json
from keras.models import load_model

model_json = model.to_json()

with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")
print("Modelo salvo no disco.")

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Modelo carregado do disco.")

model.save('model.hdf5')
loaded_model=load_model('model.hdf5')
