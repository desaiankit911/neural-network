 class Matrix:
    def __init__(self, rows, cols,add):
        self.rows = rows
        self.cols = cols
        
        print(self.rows)
        print(self.cols)
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
                ea_row.append(1)      
            self.matrix.append(ea_row)
 
    #draw the matrix
    def __repr__(self):
        outStr = ""
        for i in range(self.rows):
            outStr += 'Row %s = %s\n' % (i+1, self.matrix[i])
        return outStr
    
    #set element of the matrix
    def setitem(self, col, row, v):
        self.matrix[col-1][row-1] = v
    
    
    #get element of the matrix
    def getitem(self, col, row):
        return self.matrix[col-1][row-1]
 

    #add number to any element of the matrix
    def add_to_single_element(self, col, row,w):
        a = self.matrix[col-1][row-1]
        b = w + float(a)
        return b
  

    #add a number to matrix elements
    def add(self):
        out = ""
        print("add to matrix :")
        l = input()
        
        for i in range(self.rows):
            for j in range(self.cols):
                b = self.matrix[i][j] 
                b = float(b)+float(l)
                print(b)
                out += 'Row %s = %s\n' % ((j+1), b)
        return out
    
    #multiply matrix elements by a particular number(scalar product)
    def mul(self):
        out = ""
        print("mul to matrix :")
        l = input()
        
        for i in range(self.rows):
            for j in range(self.cols):
                b = self.matrix[i][j] 
                b = float(b)*float(l)
                print(b)
                out += 'Row %s = %s\n' % ((j+1), b)
        return out



    #matrix multiplication (dot product)
    def matrix_multiplication(self,other):
        z = self.rows
        q = self.cols
        w = other.rows
        y = other.cols
        
        if q != w:
            print("column of 1st matrix must match rows of 2nd matrix")
        else:
            print(z)
            print(q)
            print(w)
            print(y)

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
                    print('row %s.%s = %s\n' %(i+1,j+1, s))     

    
    #make the transpose of the inpute matrix
    def transpose(self):
        result = Matrix(self.cols,self.rows,0)
        for i in range(self.rows):
            for j in range(self.cols):
                a = self.matrix[i][j]
                result.matrix[j][i] = float(a)
                b = result.matrix[j][i]
                #print(b)
                print('row %s.%s = %s\n' %(j+1,i+1, b)) 
       
                
                
                    
                      
                      
a = Matrix(3,4,0)
b = Matrix(4,5,0)

print(a)
print(b)
a.setitem(2,3,'55.75')
print(a)
b.setitem(2,4,2)
print(b)

a.setitem(2,2,'19')
print(a)
b.transpose()
print (a.getitem(2,2))
print(b.add_to_single_element(2,4,5))
print(b.add())
print(b.mul())

print("items of a :")
a.getitem(b)
print("items of b:")
b.getitem()
a.matrix_multiplication(b)
print(a.transpose())
