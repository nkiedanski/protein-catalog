print("---------------Ejercicio 1-----------------------")

def max(a, b, c):
 result = None
 if a >= b and a >= c:
    result = a
 elif b >= a and b >= c:
    result = b
 elif c >= a and c >= b:
    result = c
 return result

mi_maximo = max(5,2,89)
print(mi_maximo)

print("---------------Ejercicio 2-----------------------")
