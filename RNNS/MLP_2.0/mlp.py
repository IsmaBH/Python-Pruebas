import numpy as np
from sklearn.neural_network import MLPRegressor

def get_dataset(filename1):
    #This function load the dataset from a file
    dataset = {}
    x = list()
    y = list()
    raw_data = np.loadtxt(filename1,dtype=np.int8,delimiter=',',skiprows=0)
    for i in range(len(raw_data)-1):
        y.append(raw_data[i])
        x.append(raw_data[i+1])
    dataset['X'] = np.asarray(x)
    dataset['Y'] = np.asarray(y)
    return dataset

#Test section
print("Nombre del archivo de entrenamiento: ",end="")
filename = input()
dataset = get_dataset(filename)
print("Valores a probar despues del entrenamiento: ",end="")
aux = np.array([int(i) for i in input().split()])
data = aux.reshape(-1,1)
print("Tamaño de la red: ",end="")
layer_size = tuple(int(x) for x in input().split())
print("Numero de epocas: ",end="")
epoch = int(input())
print("Activacion (identity,logistic,tanh,relu): ",end="")
act = input()
regr = MLPRegressor(hidden_layer_sizes=layer_size,activation=act,solver='adam',alpha=1.0,batch_size='auto',learning_rate='constant',learning_rate_init=0.001,max_iter=epoch,random_state=1,verbose=True,early_stopping=True,validation_fraction=0.1)
regr.fit(dataset['X'].reshape(-1,1),dataset['Y'].reshape(-1,1))
print(regr.predict(data))
