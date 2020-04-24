import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            # return the value of the only element in the Matrix
            return self.g[0][0]
        else:
            # return the calculated determinant
            return (self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0]) 

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        # initializing a new variable for the sum operation
        sum = 0
        for i in range(self.h):
            # summing the diagonal elements of the Matrix as (M)i = j for a diagonal element
            sum += self.g[i][i]
        
        return sum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        # initializing a Matrix for perfoming over it the different operations
        new_grid = zeroes(self.h,self.w)
        
        if(self.h > 1):
            #Calculating the determinant
            determinant = self.determinant()
            
            #Transposing the Matrix
            new_grid = self.T()
            
            #Applying changes to the new_grid to make it ready for the last operation 
            new_grid.prepare_matrix()

            new_grid = (1 / determinant) * new_grid

            return new_grid
        
        else:
            return Matrix([[1 / self[0][0]]])
    
    def prepare_matrix(self):
        ''' 
            Changing the Matrix from this form ([ a  b ]    to this form ([ d  -c ]
                                                [ c  d ])                 [ -b  a ])
        '''
        grid = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                grid[i][j] = self.g[i][j]
                    
        self.g[0][0] = grid[1][1]
        self.g[1][1] = grid[0][0]
        self.g[0][1] = -1 * grid[1][0]
        self.g[1][0] = -1 * grid[0][1]            
        
        return self

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        # initializing a Matrix for perfoming over it the different operations
        new_grid = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                # Assigning the new_grid elements ---- (M)ij --> (M)ji
                new_grid.g[i][j] = self.g[j][i]
         
        
        return new_grid

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # initializing a Matrix for perfoming over it the sum operation
        new_grid = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                # Adding the corresponding elements of the 2 Matrices
                new_grid.g[i][j] = self.g[i][j] + other[i][j]
        
        
        return new_grid
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        # initializing a Matrix for perfoming over it the negative operation
        neg_grid = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                 neg_grid.g[i][j] = -1 * self.g[i][j]
        
        return neg_grid

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # initializing a Matrix for perfoming over it the difference operation
        new_grid = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                # Subtracting the corresponding elements of the 2 Matrices
                new_grid.g[i][j] = self.g[i][j] - other[i][j]
    
        
        return new_grid

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "Matrices can not be Multiplicated") 
        #   
        # TODO - your code here
        #
        # initializing a Matrix for perfoming over it the multiplication operation
        new_grid = zeroes(self.h,other.w)
        
        for i in range(self.h):
            for j in range(other.w):
                # third loop for summing the product of the single row with single column
                for k in range(self.w):
                    # summing the product of the row's elements with the column's elements
                    new_grid.g[i][j] += self.g[i][k] * other[k][j]
               
        
        return new_grid
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            # initializing a Matrix for perfoming over it the integer multiplication operation
            new_grid = zeroes(self.h,self.w)
            
            for i in range(self.h):
                for j in range(self.w):
                    # Multiplicating each element in the Matrix with that integer ( other )
                     new_grid.g[i][j] = other * self.g[i][j]
            
        return new_grid