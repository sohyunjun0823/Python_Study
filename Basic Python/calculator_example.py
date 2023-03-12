a = int(input("첫 번째 숫자를 입력하세요. : "))
b = int(input("두 번째 숫자를 입력하세요. : "))
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b
h = a % b
i = int(input("1. (+) | 2. (-) | 3. (*) | 4. (/) | 5. (//) | 6. (%) "))
if i == 1:
    print(a, "+", b, "=", c)
elif i == 2:
    print(a, "-", b, "=", d)
elif i == 3:
    print(a, "*", b, "=", e)
elif i == 4:
    print(a, "/", b, "=", f)
elif i == 5:
    print(a, "//", b, "=", g)
elif i == 6:
    print(a, "%", b, "=", h)
    
