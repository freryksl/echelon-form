def swap_rows(matrix,r,c,rows): # this function swaps rows, if pivot column is zero
    for i in range(r,rows):
        if(matrix[i][c] != 0.0 and matrix[r][c] == 0.0):
            matrix[r], matrix[i] = matrix[i], matrix[r]  

def simplify(matrix,r,c,columns): # it simplifies columns
    n = matrix[r][c]
    if(n != 0.0):
        for l in range(columns):
            matrix[r][l] /= n
    else:
        if(c+1 <= columns-1):
            simplify(matrix,r,c+1,columns)        

def r_echelon(matrix,r,c,rows,columns): # this function makes row reduction
    if(matrix[r][c] != 0.0): # if pivot column is not zero, make row reduction
        simplify(matrix,r,c,columns)
        for a in range(r+1,rows):
            n = -(matrix[a][c]/matrix[r][c])
            for d in range(columns):
                matrix[a][d] += n*matrix[r][d]     
        if(r+1 < rows-1 and c+1 <= columns-1):
            r_echelon(matrix,r+1,c+1,rows,columns)         
    else: # if pivot column is zero, swap rows. if it's still zero, increase column number.
        swap_rows(matrix,r,c,rows)
        if(matrix[r][c] == 0.0):
            if(c+1 <= columns-1):
                c += 1          
        r_echelon(matrix,r,c,rows,columns)
    simplify(matrix,rows-1,c,columns)      

def rr_echelon(matrix,r,c,rows,columns): # almost same as the previous function, except couple of changes. 
    if(matrix[r][c] != 0.0):
        for a in range(r):
            n = -(matrix[a][c]/matrix[r][c])
            for d in range(columns):
                matrix[a][d] += n*matrix[r][d]
        if(r+1 < rows and c+1 <= columns-1):
            rr_echelon(matrix,r+1,c+1,rows,columns)
    else:
        if(c+1 <= columns-1):
            c += 1
            rr_echelon(matrix,r,c,rows,columns)      

class generator:
    def __init__(self, matrix):
        self.matrix = matrix     
    def rowEchelon(self):
        matrix = self.matrix
        swap_rows(matrix,0,0,len(matrix))
        r_echelon(matrix,0,0,len(matrix),len(matrix[0]))
        return matrix
    def reducedRowEchelon(self):
        matrix = self.matrix
        swap_rows(matrix,0,0,len(matrix))
        r_echelon(matrix,0,0,len(matrix),len(matrix[0]))
        rr_echelon(matrix,0,0,len(matrix),len(matrix[0]))
        return matrix
    