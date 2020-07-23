import numpy as np

n = int(input("Enter number of resistors ")) #no of resistors
m = int(input("Enter number of voltage+current sources "))

resis_neighbors = [[0 for x in range(n+m+1)]for y in range(n+m+1)]
B =np.zeros(shape=(n+2,m+1))

#for every line till n take input of resistors and values and its ends
# Take note of current flow 
# Flows toward the node connected to the first lead

print("Input the numbers in a given format")
component_name = []
component_type = []
component_value = []
component_firstnode = []
component_secondnode = []

t = 1

for i in range(0,n+m):
    inp1,inp2,inp3,inp4,inp5 = input().split()

    if inp2=="R":
        resis_neighbors[int(inp4)][int(inp5)] = int(inp3)
        resis_neighbors[int(inp5)][int(inp4)] = int(inp3)

    if inp2=="E":
        if inp4!="1":
            B[int(inp4)][t] = 1

        if inp5!="1":    
            B[int(inp5)][t] = -1
        t+=1

    component_name.append(inp1)
    component_type.append(inp2)
    component_value.append(inp3)
    component_firstnode.append(inp4)
    component_secondnode.append(inp5)

ground = 1
G = np.zeros(shape=(n,n)) #Resistance Matrix done

for i in range(0,n):
    for j in range(1,n+2):
        if(resis_neighbors[i+2][j] != 0):
            conductance = 1/resis_neighbors[i+2][j]
            G[i][i] += conductance

            if(j!=ground):
                G[i][j-2] -= conductance

B = B[2:,1:]
C = B.transpose()
D = np.zeros(shape=(m,m))

final_matrix = np.zeros(shape=(n+m,n+m))

for i in range(n):
    for j in range(n):
        final_matrix[i][j] = G[i][j]

for i in range(n):
    for j in range(m):
        final_matrix[i][j+n] = B[i][j]

for i in range(m):
    for j in range(n):
        final_matrix[i+n][j] = C[i][j]

for i in range(m):
    for j in range(m):
        final_matrix[i+n][j+n] = D[i][j]

print(final_matrix)
