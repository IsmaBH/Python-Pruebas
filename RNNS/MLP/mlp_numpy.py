import numpy as np

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
    activation = np.add(np.dot(weights,inputs),bias)
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

def forward_propagate(network,row,v2):
    #Function that makes de propagation of the data
    inputs = row
    for i in range(len(network[0]['weights'])):
        new_inputs = ()
        activation = activate(network[0]['weights'][i],network[1]['bias'][i],inputs)
        output = transfer(v2[i],activation)
        new_inputs.append(output)
        inputs = new_inputs[i]
    network['outputs'] = new_inputs
    return network

def transfer_derivative(opc,output):
    #Function that set the derivates for the given functio
    #See transfer function for the meaning of the options
    if opc == 1:
        return 1
    elif opc == 2:
        return np.dot(output,(1.0-output))
    else:
        return 1.0 - (transfer(3,output))**2

def backpropagate_error(network,expected):
    #Function that implements the backprpagation
    pass
#Test seccion
v1 = [int (x) for x in input().split()]
v2 = [int (y) for y in input().split()]
network = init_network(v1)
print(network)
