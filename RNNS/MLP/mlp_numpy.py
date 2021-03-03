import numpy as np
import os

def init_network(v1):
    #Function that initialize the network parameters
    w_network = list()
    b_network = list()
    network = {}
    layers = len(v1)
    for i in range(layers-1):
        w_layer = np.random.randint(1,3,(v1[i+1],v1[i]))
        w_network.append(w_layer)
    for i in range(layers-1):
        b_layer = np.random.randint(1,3,(v1[i+1],1))
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

def transfer_derivative(opc,output):
    #Function that set the derivates for the networok
    #See transfer function for the meaning of the options
    if opc == 1:
        x,y = output.shape
        output.shape = (y,x)
        purelin = np.diag(output)
        return purelin
    elif opc == 2:
        x,y = output.shape
        output.shape = (y,x)
        aux = output[0]*(1.0 - output)
        sigmoid = diag(aux)
        return sigmoid
    else:
        x,y = output.shape
        output.shape = (y,x)
        aux = 1-(transfer(output)**2)
        tansig = np.diag(aux)
        return tansig

def backpropagate_error(network,expected,v2):
    #Function that implements the backprpagation of the error
    #to get the sensitivities of the network
    sensitivities = list()
    count = 0
    for i in reversed(range(len(network['outputs']))):
        if i == len(network['outputs']):
            derivate = transfer_derivative(v2[i],network['outputs'][i])
            error = expected - network['outputs'][i]
            sens = ((-2)*derivate)*error
            sensitivities.append(sens)
        else:
            for j in range(len(network['outputs'])):
                derivate = transfer_derivative(v2[i],network['outputs'][i])
                sens = (derivate*np.transpose(network['weights'][i]))*sensitivities[j+count]
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
        aux = l_rate*network['sens'][i]
        new_b = network['bias'][j] - aux
        new_bias.append(new_b)
    network['weights'] = new_weights
    network['bias'] = new_bias
    return network

def train_network(network,dataset,l_rate,n_epoch,validation_round,expected_error):
    #This function starts the training of the network for
    #a given number of epoch and return the ideal values for 
    #the weights and biases
    prev_error = 0
    for epoch in range(n_epoch):
        if (epoch % validation_round) == 0:
            n_dataset = len(dataset['val_inputs'])
            iter_errors = []
            for i in range(n_dataset):
                val_network = forward_propagate(network,v2,dataset['val_inputs'][i])
                errors = dataset['val_outputs'][i] - val_network['outputs']
                x,y = errors.shape
                error = errors.sum()/x
                iter_errors.append(error)
            aux = iter_errors.sum()
            epoch_error = aux/len(dataset['val_outputs'])
            print("Error de la epoca de validacion: ",epoch_error)
            if epoch_error > prev_error:
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
                network = backpropagate_error(network,dataset['train_outputs'][t_index])
                network = learning_rule(network,l_rate)
                errors = dataset['train_inputs'][i] - network['outputs']
                x,y = errors.shape
                error = errors.sum()/x
                iter_errors.append(error)
            aux = iter_errors.sum()
            epoch_error = aux/len(dataset['train_outputs'])
            if epoch_error < expected_error:
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
        outputs_train.append(train_dataset[i])
        inputs_train.append(train_dataset[i+1])
    for i in range(len(validation_dataset)-1):
        outputs_val.append(validation_dataset[i])
        inputs_val.append(validation_dataset[i+1])
    for i in range(len(test_dataset)-1):
        outputs_test.append(test_dataset[i])
        inputs_test.append(test_dataset[i+1])
    dataset['train_inputs'] = inputs_train
    dataset['train_outputs'] = outputs_train
    dataset['val_inputs'] = inputs_val
    dataset['val_outputs'] = outputs_val
    dataset['test_inputs'] = inputs_test
    dataset['test_outputs'] = outputs_test
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
v1 = [int (x) for x in input().split()]
v2 = [int (y) for y in input().split()]
#filename = [ str (z) for z in  input().split()]
#dataset = get_dataset(filename[0],filename[1],filename[2])
#dataset = np.array([1,2,4,5])
#dataset.shape = (4,1)
#print("Train data: ",len(dataset['train_inputs']))
#print("Train outputs: ",len(dataset['train_outputs']))
#print("Validation data: ",len(dataset['val_inputs']))
#print("Validation outputs: ",len(dataset['val_outputs']))
#print("Test data: ",len(dataset['test_inputs']))
#print("Test_outputs: ",len(dataset['test_outputs']))
#---------------------------------------------------------
network = init_network(v1)
