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
        purelin = np.diag(output[0])
        return purelin
    elif opc == 2:
        x,y = output.shape
        output.shape = (y,x)
        aux = output[0]*(1.0 - output[0])
        sigmoid = diag(aux)
        return sigmoid
    else:
        x,y = output.shape
        output.shape = (y,x)
        aux = 1-(transfer(output[0])**2)
        tansig = np.diag(aux)
        return tansig

def backpropagate_error(network,expected,v2):
    #Function that implements the backprpagation of the error
    #to get the sensitivities of the network
    sensitivities = list()
    count = 0
    for i in reversed(range(len(network[2]))):
        if i == len(network[2]):
            derivate = transfer_derivative(v2[i],network[2][i])
            error = expected - network[2][i]
            sens = ((-2)*derivate)*error
            sensitivities.append(sens)
        else:
            for j in range(len(network[2])):
                derivate = transfer_derivative(v2[i],network[2][i])
                sens = (derivate*np.transpose(network[0][i]))*sensitivities[j+count]
                sensitivities.append(sens)
                count += 1
                break
    network['sens'] = sensitivities
    return network

def learning_rule(network,l_rate):
    #This function updates the weights and biases according to
    #the sensitivities got in the backpropagate function
    pass
#Test seccion
v1 = [int (x) for x in input().split()]
v2 = [int (y) for y in input().split()]
dataset = np.random.randint(1,10,(4,1))
#dataset = np.array([1,2,4,5])
#dataset.shape = (4,1)
network = init_network(v1)
network = forward_propagate(network,v2,dataset)
print(network)
