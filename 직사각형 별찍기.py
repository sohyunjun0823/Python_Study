a, b = map(int, input().strip().split(' '))

for n in range(1, b + 1, 1):
    str = ''
    for m in range(1, a + 1, 1):
        str += '*'
    print(str)
    
