def func1(a, b, c, d):


    A = []
    for i in range(0, a):
        B = []
        for n in range(1, b + 1):
            B.append(n)
        A.append(B)

    for j in range(0, a):
        for k in range(0, b):
            A[j][k] = (k + 1) + (j * 5)

    print(A)
    print(A[c][0:d])
    
    

for i in range(2):
    x = int(input())
    y = int(input())
    z = int(input())
    w = int(input())


    func1(x, y, z, w)


