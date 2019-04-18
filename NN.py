from matrix import *

class NeuralNetwork:
    def __init__(self,input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        
        self.weights_ih = Matrix(self.hidden_nodes,self.input_nodes,0)
        self.weights_ho = Matrix(self.output_nodes,self.hidden_nodes,0)
        
        self.bias_h = Matrix(self.hidden_nodes, 1, 0)
        self.bias_o = Matrix(self.output_nodes, 1, 0)
        
        self.bias_h.randomise()
        #print(self.bias_h)
        self.bias_o.randomise()
        #print(self.bias_o)
    def feedforward(self,input_array):
        inputs = Matrix.fromArray(input_array)
        #print(inputs)
        hidden = Matrix.matrix_multiplication(self.weights_ih, inputs)
        b = hidden.add(self.bias_h)
        print(b)
        b.map(sigmoid)
        print(b)
        
        output = Matrix.matrix_multiplication(self.weights_ho, hidden)
        c = output.add(self.bias_o)
        print(c)
        c.map(sigmoid)
        print(c)
        return c.toarray()
        
        
nn = NeuralNetwork(2,4,1)
inpute = [1,2]
outpute = nn.feedforward(inpute)

print(outpute)
