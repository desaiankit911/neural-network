import math
import random

#sigmoid function
def sigmoid(x):
    return 1/(1+math.exp( -x ))

def dsigmoid(y):
    return y * (1 - y)
class Matrix:
    def __init__(self, rows, cols,add):
        self.rows = rows
        self.cols = cols
        
        self.matrix = []
        print()
        #z = input()
        for i in range(rows):
            ea_row = []
            for j in range(cols):
               # if (add==""):
                   # ea_row.append(z)
               # else:
                   #  ea_row.append(int(z))
                
                ea_row.append(0)      
            self.matrix.append(ea_row)
 
    #draw the matrix
    def __repr__(self):
        outStr = ""
        for i in range(self.rows):
            outStr += 'Row %s = %s\n' % (i+1, self.matrix[i])
        return outStr
    
    #giving the random numbers for matrix
    def randomise(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.random()
        return self
    
    #set element of the matrix
    def setitem(self, col, row, v):
        self.matrix[col-1][row-1] = v
    
    
    #get element of the matrix
    def getitem(self, col, row):
        return self.matrix[col-1][row-1]
 

    #add number to any element of the matrix
    def addition(self, col, row,w):
        a = self.matrix[col-1][row-1]
        b = float(w) + float(a)
        return b
    
    #add number to any element of the matrix
    def pluse(self,w):
        #a = self.matrix[][row-1]
        result = Matrix(self.rows,self.cols,0)
        for i in range(self.rows):
            for j in range(self.cols):
                a = self.matrix[i][j]
                b = float(w) + float(a)
                result.matrix[i][j] = b
        return result
    
    #multiply number to any element of the matrix
    def multiplication(self,w):
         #a = self.matrix[][row-1]
        result = Matrix(self.rows,self.cols,0)
        for i in range(self.rows):
            for j in range(self.cols):
                a = self.matrix[i][j]
                b = float(w) * float(a)
                result.matrix[i][j] = b
        return result
    
    @staticmethod
    def sub(self,other):
        result = Matrix(self.rows,other.cols,0)
        for i in range(self.rows):
            for j in range(self.cols):
                a = self.matrix[i][j]
                b = other.matrix[i][j]
                c = float(a) - float(b)
                result.matrix[i][j] = c
        return result
  
  #add a number to matrix elements
    def add(self,other):
        result = Matrix(self.rows,other.cols,0)
        for i in range(self.rows):
            for j in range(self.cols):
                a = self.matrix[i][j]
                b = other.matrix[i][j]
                c = float(a)+float(b)
                result.matrix[i][j] = c
        return result

   #hadamard multiplication of matrix
    def mul(self,other):
        result = Matrix(self.rows,other.cols,0)
        for i in range(self.rows):
            for j in range(self.cols):
                a = self.matrix[i][j]
                b = other.matrix[i][j]
                c = float(a) * float(b)
                result.matrix[i][j] = c
        return result
    
    @staticmethod
    def map(mat,func):
        result = Matrix(self.rows,other.cols,0)
        for i in range(self.rows):
            for j in range(self.cols):
                val = mat.matrix[i][j]
                result.matrix[i][j] = func(val)
        
        
    
    #converting input matrix to the form of vector
    @staticmethod
    def fromArray(array):
        m = Matrix(len(array),1,0)
        for i in range(len(array)):
            m.matrix[i][0] = array[i]
        return m
    
    
    def toarray(self):
        arr = []
        #a = self.rows
        #b = self.cols
        #print(a)
        #print(b)
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.matrix[i][j])
                #print(arr)
        return arr
        
    #matrix multiplication (dot product)
    @staticmethod
    def matrix_multiplication(self,other):
        z = self.rows
        q = self.cols
        w = other.rows
        y = other.cols
        
        if q != w:
            print("column of 1st matrix must match rows of 2nd matrix")
        else:
            result = Matrix(self.rows,other.cols,0)
            for i in range(z):
                for j in range(y):
                    s = 0
                    e = 0
                    for k in range(w):
                        a = self.matrix[i][k]
                        b = other.matrix[k][j] 

                        c = float(a) * float(b)
                        #print(c)
                        s += c
                        
                    result.matrix[i][j] = s
            return result
  
    #make the transpose of the inpute matrix
    #@staticmethod
    def transpose(self):
        result = Matrix(self.cols,self.rows,0)
        for i in range(self.rows):
            for j in range(self.cols):
                #print(self.matrix[i][j])
                result.matrix[j][i] = self.matrix[i][j]
        return result
                
    #mapping the sigmoid function            
    def map(self,func): 
        for i in range(self.rows):
            for j in range(self.cols):
                val =  self.matrix[i][j]
                self.matrix[i][j] = func(val)

#a = Matrix(3,4,0)
#b = Matrix(4,5,0)
#print(a)
#print(b)

#Matrix.mult(a,b)

#z = b.randomise()
#print(z)

#a.setitem(2,3,5.75)
#print(a)
#b.setitem(2,4,2)
#print(b)
#a.setitem(2,2,19)
#print(a)

#a = a.transpose()
#print(a)

#print("items of a :")
#print (a.getitem(2,2))
#print("items of b :")
#print (b.getitem(2,2))

#print(b.add_to_single_element(2,4,5))

#c = Matrix(3,1,0)
#d = Matrix(3,1,0)
#print(c)
#print(d)
#z = Matrix.sub(c,d)
#print(z)

#z = a.pluse(1)
#print(z)

#y = a.add(b)
#print(y)

#c = a.multiplication(2)
#print(c)
#y = a.mul(b)
#print(y)

#array =[1,2,3]
#print(array)
#Matrix.fromArray(array)

#Matrix.matrix_multiplication(a, b)
#print(z)

#b.map(sigmoid)
#print(b)
