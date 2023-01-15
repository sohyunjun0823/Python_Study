# input : 3 5
#
# A
# [[1  2  3  4  5], 
#  [6  7  8  9  10],
#  [11 12 13 14 15]]

# input 1 3
# [6, 7, 8]

a = int(input())
b = int(input())

#B[a][b]
A = []
for i in range(0, a):
    B = []
    for n in range(1, b + 1):
        B.append(n)
    A.append(B)

for j in range(0, a):
    for k in range(0, b):
        A[j][k] = (k + 1) + (j * 5)

c = int(input())
d = int(input())

print(A[c][0:d])

    
        
