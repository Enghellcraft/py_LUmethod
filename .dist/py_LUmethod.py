
# Imports
import numpy as np
import scipy
import scipy.linalg as linalg 

# Functions
## Square matrix
def my_square_matrix(A):
    A = np.array(A)
    # Revisa si el numero de Columnas es igual al de Filas
    if A.shape[0] != A.shape[1]:
        return False
    else:
        return True
    
## Inverts a matrix
def my_inverse(A):
    Am = np.matrix(A)
    # Para poder invertirse una matriz tiene por requisito ser cuadrada
    if my_square_matrix(A) == True :
            # Si es cuadrada verifica si se puede invertir
            Aa = np.array(A)
            if np.linalg.det(Am) == 0:
                return print("No es inversible")
            else:
                Ainv = np.linalg.inv(Am)
                print("La matriz inversa es: \n", Ainv)
    
## Determinant of a square matrix

def det_2x2(A): 
        diagonal_principal = A[0][0] * A[1][1] 
        diagonal_secundaria = A[0][1] * A[1][0] 
        return diagonal_principal - diagonal_secundaria 
 
def my_determinant(A): 
    N = len(A)
    if N == 2:
        det_2x2(A)
    else:     
        determinants = [] 
        for i in range(N): 
            for j in range(N): 
                submatrix = [] 
                for k in range(N): 
                    if k != i: 
                        fila = [] 
                        for l in range(N): 
                            if l != j: 
                                fila.append(A[k][l]) 
                        submatrix.append(fila) 
                determinant = det_2x2(submatrix) 
                determinants.append(determinant) 
        if determinants.__contains__(0):
            return False
        else: return True


## Zero on diagonal
def my_zero_on_diagonal(A):
    N = len(A)
    # Itera por todos los valores de la diagonal verificando si alguno es cero
    for i in range(0,N-1) :
        if (A[i][i] == 0) :
            return False
    return True
 
## LU decomposition
def my_lu_decomposition(A):
    A = np.array(A)
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A)

    for i in range(n):
        U[i, i:] = A[i, i:] - L[i, :i] @ U[:i, i:]
        L[i + 1:, i] = (A[i + 1:, i] - L[i + 1:, :i] @ U[:i, i]) / U[i, i]

    print(f"La matriz A es: \n {L @ U}")
    print(f"La matriz L es: \n {L}")
    print(f"La matriz U es: \n {U}")
   
## LU method
def my_lu(A):
    if my_zero_on_diagonal(A) == False:
        return print("Algun Elemento en la diagonal es 0 y no puede resolverse por LU")
    else:
         if my_square_matrix(A) == False:
            print("La matriz debe ser una matriz cuadrada para resolverse por LU")
         else:
            if my_determinant(A) == False:
                print("La determinante de la matriz y submatrices debe ser distinta a cero \npara resolverse por LU")
            else:
                LU = linalg.lu_factor(A)         
                #x = linalg.lu_solve(LU, B) 
                my_lu_decomposition(A)
                #print ("La solucion es:\n",x )

## Operations count
def lu_decomposition_count(A):
    N = len(A)
    op_count_L = N**2 - N
    op_count_U = N**2
    op_count_A = op_count_L + op_count_U
        
    return op_count_A, op_count_L, op_count_U

## Print matrix
def print_matrix(A):
    a = np.array(A)
    for line in a:
        print ('  '.join(map(str, line)))

# Dataset
matrix_zero_in_diag =  ([[1,2,3],
                         [4,0,2],
                         [2,2,3]])

non_square_matrix = ([[1,2,3],
                     [2,2,3]])

zero_determinant_matrix = ([[3,1,4],
                           [-1,2,1],
                           [3,2,1]])

doable_matrix = ([[1,2,3],
                 [2,3,1],
                 [-2,3,-2]])

doable_matrix_2 = ([[1,1,1],
                 [3,1,-3],
                 [1,-2,-5]])

doable_matrix_3 = ([[1,2],
                    [2,2]])

# Prints
## null) Task + Pres
print("                                                                                  ")
print("**********************************************************************************")
print("*                  METODOS NUMERICOS - 2023 - TP METODO LU                       *")
print("**********************************************************************************")
print("    • Alumna: Denise Martin")
print("                                                                                  ")
print("**********************************************************************************")
print("*                                    CONSIGNA                                    *")
print("**********************************************************************************")
print("  Para resolver la ecuación matricial Ax = b, el método LU, cuando es factible, lleva tres etapas.")
print("  Tomamos aquí sólo las dos últimas, y pedimos que para estas calculen cuántas operaciones ")
print("  elementales serán necesarias en el peor caso, dada A una matriz de nxn y dado b un vector de nx1.")

## I) Theory
print("                                                                                  ")
print("**********************************************************************************")
print("*                                      TEORIA                                    *")
print("**********************************************************************************")
print("  El Método de descomposición LU, también es conocido como factorización matricial.")
print("  Consiste en descomponer la matriz A en el producto de dos matrices:              ") 
print("    • una L (de Lower) triangular inferior,                                        ")
print("    • y otra U (de Upper) triangular superior.                                     ")
print("  Las matrices L y U pueden ser usadas para calcular el determinante de la matriz A")
print("  porque det(A) = det(L) det (U). Donde los determinantes de matrices triangulares ")
print("  son el producto de los elementos de sus diagonales. Como L posse todos 1 en su   ")
print("  diagonal, su determinante es 1, por lo que: det(A) = det(U)                      ")
print("                                                                                   ")
print("  Requisitos:                                                                      ")
print("    • La matriz principal debe ser cuadrada.                                      ")
print("    • No deben encontrarse ceros en su diagonal.                                   ")
print("    • La matriz principal y sus submatrices deben tener determinante distinto a cero.")
print("    • Si la matriz es inversible, podria haber mas de una descomposición posible. ")
print("    • Si la matriz no es singular existe una sola descomposición posible.         ")
print("                                                                                  ")
print("  *** Ejemplo Teorico de Calculode Operaciones en Matriz A de 3x3:           ***  ")
print("                                                                                  ")
print("**********************************************************************************")
print("                                                                                  ")
print(" CONSIGNA a):Determinar en función de n cuántas operaciones elementales lleva en  ")
print("             el peor caso despejar el vector y en la ecuación matricial Ly = b.   ")
print("                                                                                  ")
print("  Calculo de Operaciones de L (Lx = b):                                           ")
print("    • Cuando A es factorizable, la matriz L tiene la diagonal con 1 → Lii = 1      ")
print("    [ [1     0     0]           [Y1        [b1                                    ")
print("      [L21   1     0]      x     Y2    =    b2                                    ")
print("      [L31   L32   1] ]          Y3]        b3]                                   ")
print("    • Esta ecuación matricial la podemos expresar de la siguiente manera:         ")
print("    y1 * 1 = b1                          ---> 0 Operaciones                       ")
print("    y1 * L21 + y2 * 1 = b2               ---> 2 Operaciones                       ")
print("    y1 * L31 + y2 * L32 + y3 * 1 = b3    ---> 4 Operaciones                       ")
print("      Puede expresarse aqui entonces como: 2 * i - 2 por cada fila                ")
print("      En una matriz se puede expresar el total como: n^2 - n                      ")
print("    • Se comprueba para cada fila:                                                ")
print("    y1 = 2. 1 - 2 = 0                                                             ")
print("    y2 = 2. 2 - 2 = 2                                                             ")
print("    y3 =  2. 3 - 2 = 4                                                            ")
print("    • Se comprueba el total de operaciones:                                       ")
print("    total de operaciones en L = 3^2 - 3 = 9 - 3 = 6                               ")
print("                                                                                  ")
print("**********************************************************************************")
print("                                                                                  ")
print(" CONSIGNA b):Determinar en función de n cuántas operaciones elementales lleva en  ")
print("             el peor caso despejar el vector x en la ecuación matricial Ux = y.   ")
print("                                                                                  ")
print("  Calculo de Operaciones de U (Ux = y):                                           ")
print("    • Cuando A es factorizable, la matriz U puede tener o no unos en su diagonal  ")
print("    [ [U11  U12  U13]           [X1        [Y1                                    ")
print("      [0    U22  U23]      x     X2    =    Y2                                    ")
print("      [0    0    U33] ]          X3]        Y3]                                   ")
print("    • Esta ecuación matricial la podemos expresar de la siguiente manera:         ")
print("    x1 * U11 + x2 * U12 + x3 * U13 = y1  ---> 5 Operaciones                       ")
print("    x2 * U22 + x3 * U23 = y2             ---> 3 Operaciones                       ")
print("    x3 * U33 = y3                        ---> 1 Operacion                         ")
print("      Puede expresarse entonces como:  2.(n + 1 - i) - 1 por cada fila            ")
print("      En una matriz se puede expresar el total como: n^2                          ")
print("    x1 =  2. (3 + 1 - 1) - 1 = 5                                                  ")
print("    x2 =  2. (3 + 1 - 2) - 1 = 3                                                  ")
print("    y3 =  2. (3 + 1 - 3) - 1 = 1                                                  ")
print("    • Se comprueba el total de operaciones:                                       ")
print("    total de operaciones en U = 3^2 = 9                                           ")
print("                                                                                  ")
print("**********************************************************************************")
print("                                                                                  ")
print(" CONSIGNA c):Concluir respondiendo cuántas operaciones elementales requieren en   ")
print("             el peor caso las dos etapas (a) y (b) del método LU.                 ")
print("                                                                                  ")
print("  Suponiendo el peor caso donde U no tenga unos en sus diagonales, se requieren:  ")
print("  Total de operaciones L + Total de operaciones U = n^2 - 2 + n^2 = 2 * n^2 -n    ")
print("    • Se comprueba el total de operaciones para esta matriz de 3x3:               ")
print("    total de operaciones: 2 * 3^2 - 3 = 15 operaciones                            ")

## II) Examples
print("                                                                                  ")
print("**********************************************************************************")
print("*                                    EJEMPLOS                                    *")
print("**********************************************************************************")
print("    • Se comprueba si la matriz tiene algun cero en su diagonal:                 ")
print_matrix(matrix_zero_in_diag)
my_lu(matrix_zero_in_diag)
print_matrix([[2,1], [2,1]])
print("    es la submatriz que tiene determinante cero: 2*1 - 2*1 = 0                    ")
print("                                                                                  ")
print("    • Se comprueba si la matriz es cuadrada:                                      ")
print_matrix(non_square_matrix)
my_lu(non_square_matrix)
print("                                                                                  ")
print("    • Se comprueba si la matriz tiene determinante = 0: (en matriz y submatrices) ")
print_matrix(zero_determinant_matrix)
my_lu(zero_determinant_matrix)
print("                                                                                  ")
print("    • Se emiten las matrices L y U de una matriz que cumple los requisitos:       ") 
print_matrix(doable_matrix)
my_lu(doable_matrix)
count_A, count_L, count_U = lu_decomposition_count(doable_matrix)
print(f"    • y se calcula la cantidad de operaciones totales que llevo: {count_A}       ") 
print(f"    • la cantidad de operaciones en L: {count_L}, y en U: {count_U}              ")
print("                                                                                  ")
print("    • Se emiten las matrices L y U de una matriz que cumple los requisitos:       ") 
print_matrix(doable_matrix_2)
my_lu(doable_matrix_2)
count_A, count_L, count_U = lu_decomposition_count(doable_matrix_2)
print(f"    • y se calcula la cantidad de operaciones totales que llevo: {count_A}       ") 
print(f"    • la cantidad de operaciones en L: {count_L}, y en U: {count_U}              ")
print("                                                                                  ")
print("    • Se emiten las matrices L y U de una matriz que cumple los requisitos:       ") 
print_matrix(doable_matrix_3)
my_lu(doable_matrix_3)
count_A, count_L, count_U = lu_decomposition_count(doable_matrix_3)
print(f"    • y se calcula la cantidad de operaciones totales que llevo: {count_A}       ") 
print(f"    • la cantidad de operaciones en L: {count_L}, y en U: {count_U}              ")

## III) Conclusions
print("                                                                                  ")
print("**********************************************************************************")
print("*                                  CONCLUSIONES                                  *")
print("**********************************************************************************")
print(" • El Método de descomposición LU, también es es un método semi-numérico, que no ")
print("   tiene criterio de convergencia y no requiere aproximación inicial, sin embargo es") 
print("   aplicable cuando las matrices se pueden resolver por el método de Gauss sin    ")
print("   intercambio de renglones.                                                      ")
print("                                                                                  ")
print(" • Es un método inestable ya que si alguno o varios elementos de la diagonal principal ")
print("   son cero, se debe premultiplicar la matriz por alguna elemental de permutación, ") 
print("   para poder aplicar la factorización.                                           ") 
print("                                                                                  ")
print(" • Se utiliza principalmente por su facilidad en resolucionde matrices triangulares ")
print("                                                                                  ")
