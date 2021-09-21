import math

''' Define the Function here '''
def f(x):
    return 3*x + math.sin(x) - math.exp(x)


#Tolerance Value 
global tol
tol = 0.0000001

''' -------------------------------------------The Algorithm ---------------------------------------------------------'''
'''------------------To determine the root of f(x), we begin with x1 being closer to the root than x0-----------------'''

''' The idea is to take the last two computed points to draw secant which intersects the x - axis closer to the point where
the actual root lies'''

def secant(x0, x1, tol,counter):
    if (abs(f(x0)) < abs(f(x1))):
        
        #Swapping the values of x0 and x1
        x0 = x0 + x1
        x1 = x0 - x1
        x0 = x0 - x1
        
    x2 = x1 - f(x1)*((x0-x1)/(f(x0)-f(x1))) #Calculate the secant point of intersection
    
    ##---------------------------Display-------------------------------##
    print('Iteration no.', counter)
    counter += 1
    print("X0: ", x0 ,"  X1: ", x1 ,"  X2: " , x2 ,"  f(x2): " , f(x2))
    print('\n')
    #------------------------------------------------------------------##
    
    x0 = x1 #x1 was closer to the root, now we expect x2 to be closer 
    x1 = x2 #Therfore closer one is chosen as x2.
    
    if abs(f(x2))<tol:
        print(x2)
        print('The Best approximated root')
    else:
        secant(x0,x1,tol,counter) #iterative step 
'''------------------------------------------------End of Algorithm-------------------------------------------------'''        
             
#Test the algorithm
x0 = 1
x1 = 0
counter = 1
secant(x0,x1,tol,counter)
