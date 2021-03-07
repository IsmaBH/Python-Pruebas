import numpy as np
from sklearn.neural_network import MLPRegressor

def get_dataset(filename1):
    #This function load the dataset from a file
    dataset = {}
    x = list()
    y = list()
    raw_data = np.loadtxt(filename1,dtype=np.int8,delimiter=',',skiprows=0)
    for i in range(len(raw_data)-1):
        x.append(raw_data[i])
        y.append(raw_data[i])
    dataset['X'] = x
    dataset['Y'] = y
    return dataset

#Test section
print("Nombre del archivo de entrenamiento: ",end="")
filename = input()
dataset = get_dataset(filename)
print("Valores a probar despues del entrenamiento: ",end="")
aux = np.array([int(i) for i in input().split()])
data = aux.reshape(1,-1)
print("Tamaño de la red: ",end="")
layer_size = tuple(int(x) for x in input().split())
print("Numero de epocas: ",end="")
epoch = int(input())
regr = MLPRegressor(hidden_layer_sizes=layer_size,activation='logistic',solver='adam',alpha=1.0,batch_size='auto',learning_rate='constant',learning_rate_init=0.001,max_iter=epoch,random_state=1,verbose=True,early_stopping=True,validation_fraction=0.1)
regr.fit(dataset['X'],dataset['Y'])
print(regr.predict(data))
