def missing_number(n, l):
    suma_total = n * (n + 1) // 2 
    suma_real = sum(l) 
    return suma_total - suma_real 


l = [] 
n = 0 

#Se utiliza un bucle "while" para solicitar al usuario que ingrese un valor entero mayor que uno y verificar que esa condición se cumpla
while n < 1:
    try:
        n = int(input("Ingrese la longitud del arreglo (un número entero mayor que 1): "))
        if n <= 1:
            print("Por favor, ingrese un número entero mayor que 1")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido")

#Se utiliza un bucle "for-in" para iterar sobre los índices dentro del rango de 0 hasta "n-1" (porque falta un número en la secuencia)
for i in range(n - 1):
    m = 0 
    #Se utiliza un bucle "while" para solicitar al usuario que ingrese un valor entero mayor que cero y se lo almacena en la variable "m", validando que el valor ingresado sea válido. Esto se repite mientras "m" sea menor o igual que 0
    while m <= 0:
        try:
            m = int(input("Ingrese el elemento (un número entero mayor que 0): "))
            if m <= 0:
                print("Por favor, ingrese un número entero mayor que 0.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
    l.append(m) 

numero_faltante = missing_number(n, l) 
print("El número faltante es: {}".format(numero_faltante)) 

#Se realiza una aserción para verificar si el número faltante calculado para el caso de prueba coincide con el valor esperado. Si esta falla, se imprime un mensaje de error
#Si no falla, se imprime un mensaje indicando que los casos de prueba han pasado correctamente
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")