import numpy as np
from sklearn import preprocessing
import os

def init_network(v1):
    #Function that initialize the network parameters
    w_network = list()
    b_network = list()
    network = {}
    layers = len(v1)
    for i in range(layers-1):
        w_layer = np.random.random((v1[i+1],v1[i]))
        w_network.append(w_layer)
    for i in range(layers-1):
        b_layer = np.random.random((v1[i+1],1))
        b_network.append(b_layer)
    network['weights'] = w_network
    network['bias'] = b_network
    return network

def activate(weights,bias,inputs):
    #Function that makes the activation operation
    activation = np.dot(weights,inputs) + bias
    return activation

def transfer(opc,activation):
    #This function apply one of the functions built for the network
    #in this case 1 is for linear funtion, 2 is for sigmoid
    #and 3 is for tansig, in the future may be more funtions
    if opc == 1:
        return activation
    elif opc == 2:
        return 1.0/(1.0 + np.exp(-activation))
    else:
        return (np.exp(activation) - np.exp(-activation))/(np.exp(activation) + np.exp(-activation))

def forward_propagate(network,v2,row):
    #Function that makes de propagation of the data
    inputs = row
    new_inputs = []
    for i in range(len(network['weights'])):
        activation = activate(network['weights'][i],network['bias'][i],inputs)
        output = transfer(v2[i],activation)
        new_inputs.append(output)
        inputs = new_inputs[i]
    network['outputs'] = new_inputs
    return network

def transfer_derivative(opc,output,v1):
    #Function that set the derivates for the networok
    #See transfer function for the meaning of the options
    if opc == 1:
        aux = np.ones(v1)
        purelin = np.diag(aux)
        return purelin
    elif opc == 2:
        x,y = output.shape
        output = output.reshape(y,x)
        aux = output[0]*(1 - output[0])
        sigmoid = np.diag(aux)
        return sigmoid
    else:
        x,y = output.shape
        output = output.reshape(y,x)
        aux = 1 - np.power(transfer(3,output[0]),2)
        tansig = np.diag(aux)
        return tansig

def backpropagate_error(network,expected,v2,v1):
    #Function that implements the backprpagation of the error
    #to get the sensitivities of the network
    sensitivities = list()
    count = 0
    for i in reversed(range(len(network['outputs']))):
        if i == len(network['outputs'])-1:
            derivate = transfer_derivative(v2[i],network['outputs'][i],v1[i])
            error = expected - network['outputs'][i]
            sens = np.dot(((-2)*derivate),error)
            sensitivities.append(sens)
        else:
            for j in range(len(network['outputs'])):
                derivate = transfer_derivative(v2[i],network['outputs'][i],v1[i])
                sens = np.dot(np.dot(derivate,np.transpose(network['weights'][i])),sensitivities[j+count])
                sensitivities.append(sens)
                count += 1
                break
    network['sens'] = sensitivities
    return network

def learning_rule(network,l_rate):
    #This function updates the weights and biases according to
    #the sensitivities got in the backpropagate function
    new_weights = list()
    new_bias = list()
    for i in range(len(network['weights'])):
        aux1 = l_rate*network['sens'][i]
        aux2 = aux1*np.transpose(network['outputs'][i])
        new_weight = network['weights'][i] - aux2
        new_weights.append(new_weight)
    for j in range(len(network['bias'])):
        aux = l_rate*network['sens'][j]
        new_b = network['bias'][j] - aux
        new_bias.append(new_b)
    network['weights'] = new_weights
    network['bias'] = new_bias
    return network

def train_network(network,dataset,l_rate,n_epoch,validation_round,expected_error,v2,v1):
    #This function starts the training of the network for
    #a given number of epoch and return the ideal values for 
    #the weights and biases
    prev_error = 0
    early_stop = 0
    for epoch in range(n_epoch):
        if (epoch % validation_round) == 0:
            n_dataset = len(dataset['val_inputs'])
            iter_errors = []
            for i in range(n_dataset):
                network = forward_propagate(network,v2,dataset['val_inputs'][i])
                errors = dataset['val_outputs'][i] - network['outputs'][len(v2)-1]
                x,y = errors.shape
                error = errors.sum()/x
                iter_errors.append(error)
            aux = sum(iter_errors)
            epoch_error = aux/len(dataset['val_outputs'][len(v2)-1])
            print("Error de la epoca de validacion: ",epoch_error)
            if epoch_error >= prev_error:
                early_stop += 1
                prev_error = epoch_error
                if early_stop > 3:
                    print("Choose another arch")
                    break
            else:
                early_stop = 0
        else:
            n_dataset = len(dataset['train_inputs'])
            iter_errors = []
            for i in range(n_dataset):
                network = forward_propagate(network,v2,dataset['train_inputs'][i])
                network = backpropagate_error(network,dataset['train_outputs'][i],v2,v1)
                network = learning_rule(network,l_rate)
                errors = dataset['train_outputs'][i] - network['outputs'][len(v2)-1]
                x,y = errors.shape
                error = errors.sum()/x
                iter_errors.append(error)
            aux = sum(iter_errors)
            epoch_error = aux/len(dataset['train_outputs'][len(v2)-1])
            if epoch_error < expected_error:
                print("Error de entrenamiento: ",epoch_error)
                break
            else:
                continue
    return network

def get_dataset(filename1,filename2,filename3):
    #This function takes the name of 3 files and charge it into 3 numpy array
    #then divide it in three segments (train,validate,testi)
    #PD: The way to get the dataset will change according to the problem, for my particular exercise this was the best way I found but this function needs to change once the problem change.
    dataset = {}
    inputs_train = list()
    outputs_train = list()
    inputs_val = list()
    outputs_val = list()
    inputs_test = list()
    outputs_test = list()
    train_dataset = np.loadtxt(filename1,dtype=np.int8,delimiter=',',skiprows=0)
    validation_dataset = np.loadtxt(filename2,dtype=np.int8,delimiter=',',skiprows=0)
    test_dataset = np.loadtxt(filename3,dtype=np.int8,delimiter=',',skiprows=0)
    for i in range(len(train_dataset)-1):
        outputs_train.append(preprocessing.normalize(train_dataset[i].reshape(1,-1)))
        inputs_train.append(preprocessing.normalize(train_dataset[i+1].reshape(1,-1)))
    for i in range(len(validation_dataset)-1):
        outputs_val.append(preprocessing.normalize(validation_dataset[i].reshape(1,-1)))
        inputs_val.append(preprocessing.normalize(validation_dataset[i+1].reshape(1,-1)))
    for i in range(len(test_dataset)-1):
        outputs_test.append(preprocessing.normalize(test_dataset[i].reshape(1,-1)))
        inputs_test.append(preprocessing.normalize(test_dataset[i+1].reshape(1,-1)))
    dataset['train_inputs'] = inputs_train
    dataset['train_outputs'] = outputs_train
    dataset['val_inputs'] = inputs_val
    dataset['val_outputs'] = outputs_val
    dataset['test_inputs'] = inputs_test
    dataset['test_outputs'] = outputs_test
    """
    n_train = len(dataset['train_inputs'])
    n_val = len(dataset['val_inputs'])
    n_test = len(dataset['test_inputs'])
    for i in range(n_train):
        x = dataset['train_inputs'][i].shape
        dataset['train_inputs'][i] = dataset['train_inputs'][i].reshape(x[0],1)
        dataset['train_outputs'][i] = dataset['train_outputs'][i].reshape(x[0],1)
    for i in range(n_val):
        x = dataset['val_inputs'][i].shape
        dataset['val_inputs'][i] = dataset['val_inputs'][i].reshape(x[0],1)
        dataset['val_outputs'][i] = dataset['val_outputs'][i].reshape(x[0],1)
    for i in range(n_test):
        x = dataset['test_inputs'][i].shape
        dataset['test_inputs'][i] = dataset['test_inputs'][i].reshape(x[0],1)
        dataset['test_outputs'][i] = dataset['test_inputs'][i].reshape(x[0],1)
    """
    return dataset

def set_network(opc,network):
    #This function sets the weights and bias from a file or
    #writes the weights and bias of a network in a file
    if opc == 1:
        #If opc is one then we load the weights and bias from a file
        layers = len(network['weights'])
        for i in range(layers):
            s1 = "weights{}.txt"
            s2 = "bias{}.txt"
            network['weights'][i] = np.loadtxt(s1.format(i))
            network['bias'][i] = np.loadtxt(s2.format(i))
        return network
    else:
        #If opc is another number then we save the weights and biases
        #of the given network in a file
        layers = len(network['weights'])
        for i in range(layers):
            s1 = "weights{}.txt"
            s2 = "bias{}.txt"
            if os.path.exists(s1.format(i)):
                os.remove(s1.format(i))
            else:
                print("File not found")
        for i in range(layers):
            np.savetxt(s1.format(i),network['weights'][i],delimiter=",")
            np.savetxt(s2.format(i),network['bias'][i],delimiter=",")
        return network


#Test seccion
print("MLP_1.0")
v1 = [int (x) for x in input().split()]
v2 = [int (y) for y in input().split()]
print("Select option")
print("1.- Train the network")
print("2.- Continue a previous training")
print("3.- Use a trained network")
opc = int(input())
if opc == 1:
    filename = [ str (z) for z in  input().split()]
    dataset = get_dataset(filename[0],filename[1],filename[2])
    print("Learning rate: ",end="")
    l_rate = float(input())
    print("Epocas de entrenamiento: ",end="")
    n_epoch = int(input())
    print("Error esperado: ",end="")
    e_error = float(input())
    print("Ronda de validacion: ",end="")
    v_r = int(input())
    print()
    print("Train data: ",len(dataset['train_inputs']))
    print("Train_outputs: ",len(dataset['train_outputs']))
    print("Validation_data: ",len(dataset['val_inputs']))
    print("Validation outputs: ",len(dataset['val_outputs']))
    print("Test data: ",len(dataset['test_inputs']))
    print("Test outputs: ",len(dataset['test_outputs']))
    network = init_network(v1)
    print(network)
    print(dataset['train_inputs'][0])
"""
    network = train_network(network,dataset,l_rate,n_epoch,v_r,e_error,v2,v1)
    print(network)
    print("Do you want to save the values of weights and bias? (Y/N): ",end="")
    a = input()
    if a == "Y":
        set_network(2,network)
elif opc == 2:
    network = init_network(v1)
    network = set_network(1,network)
    print("Learning rate: ",end="")
    l_rate = float(input())
    print("Epocas de entrenamiento: ",end="")
    n_epoch = int(input())
    print("Error esperado: ",end="")
    e_error = float(input())
    print("Ronda de validacion: ",end="")
    v_r = int(input())
    print()
    filename = [str(z) for z in input().split()]
    dataset = get_dataset(filename[0],filename[1],filename[2])
    network = train_network(network,dataset,l_rate,n_epoch,v_r,e_error,v2,v1)
    print("Do you want to save the values of weights and bias? (Y/N): ",end="")
    a = input()
    if a == "Y":
        set_network(2,network)
else:
    network = init_network(v1)
    print("Input vector: ",end="")
    dataset = [int(i) for i in input().split()]
    x,y = dataset.shape
    dataset.shape = (y,x)
    network = set_network(1,network)
    network = forward_propagate(network,v2,dataset)
    print(network['outputs'])
"""
