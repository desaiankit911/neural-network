from matrix import *

class NeuralNetwork:
    def __init__(self,input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        
        #weights for hidden layer
        self.weights_ih = Matrix(self.hidden_nodes,self.input_nodes,0)
        #weights for output layer
        self.weights_ho = Matrix(self.output_nodes,self.hidden_nodes,0)

        #bias for hidden layer
        self.bias_h = Matrix(self.hidden_nodes, 1, 0)
        #bias for output layer
        self.bias_o = Matrix(self.output_nodes, 1, 0)
        
        self.bias_h.randomise()
        #print(self.bias_h)
        self.bias_o.randomise()
        #print(self.bias_o)
        
        self.lr = 0.1
    def feedforward(self,input_array):
        
        #hidden layer
        inputs = Matrix.fromArray(input_array)
        #print(inputs)
        hidden = Matrix.matrix_multiplication(self.weights_ih, inputs)
        b = hidden.add(self.bias_h)
        #print(b)
        #activation function
        b.map(sigmoid)
        #print(b)
        
        #output layer
        output = Matrix.matrix_multiplication(self.weights_ho, hidden)
        c = output.add(self.bias_o)
        #print(c)
        #activation function
        c.map(sigmoid)
        #print(c)
        #return back to the function where it call's
        return c.toarray()
    def train(self,input_array,targets_array):
        
         #hidden layer
        inputs = Matrix.fromArray(input_array)
        #print(inputs)
        hidden = Matrix.matrix_multiplication(self.weights_ih, inputs)
        hiddens = hidden.add(self.bias_h)
        #print(b)
        #activation function
        hiddens.map(sigmoid)
        #print(hiddens)
        
        #output layer
        output = Matrix.matrix_multiplication(self.weights_ho, hidden)
        outputs = output.add(self.bias_o)
        #print(outputs)
        #activation function
        outputs.map(sigmoid)
        #print(outputs)
        
        
        #actual output
        targets =  Matrix.fromArray(targets_array)
        #print(targets)
        
        #calculate forward output error
        output_error =  Matrix.sub(targets,outputs)
        #print(output_error)
        
        #gradients
        #gradients = outputs * (1 - outputs)
        outputs.map(dsigmoid)
        #print(outputs)
        
        g = outputs.mul(output_error)
        #print(g)
        
        g = g.multiplication(self.lr)
        #print(g)
        
        #print(hiddens)
        hidden_T = hiddens.transpose()
        #print(hidden_T)
        
        weight_ho_delta = Matrix.matrix_multiplication(g, hidden_T)
        #print(weight_ho_delta)
        
        #print(self.weights_ho)
        ho = self.weights_ho.add(weight_ho_delta)
        #print(ho)
        
        #(who_t = transpose of weight_ho)
        who_t = Matrix.transpose(ho)
        
        #calculate eh (i.e error due to0 each node)
        hidden_error = Matrix.matrix_multiplication(who_t, output_error)
        #print(hidden_error)
        
        hiddens.map(dsigmoid)
        #print(hiddens)
        
        hg = hiddens.mul(hidden_error)
        #print(hg)
        
        hg = hg.multiplication(self.lr)
        #print(hg)
        
        #print(inputs)
        inputs_T = inputs.transpose()
        #print(inputs_T)
        
        ih = weight_ih_delta = Matrix.matrix_multiplication(hg, inputs_T)
        #print(ih)
        
        l = self.weights_ih.add(ih)
        #print(l)
        
        #print(outputs)
        #print(targets)
        #print(output_error)
        
nn = NeuralNetwork(2,2,1)
inputs = [1,0]
targets = [1]

nn.train(inputs, targets)

#print(outpute)

Tankyou :)
