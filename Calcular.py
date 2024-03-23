suma = 0
num_numeros = int(input("Por Favor Ingrese El Numero de Numeros A Ingresar")) 
for i in range(num_numeros):
    num = int(input(f"Introduce el número {i + 1}: "))
    suma += num

promedio = suma / num_numeros

print(f"El promedio de los {num_numeros} números es: {promedio}")

