def secuencia(n):
    try:
    #Se verifica si el valor ingresado no es mayor que 1 y menor que 1000000. Si no lo es, se genera una excepción "ValueError" de forma manual con la palabbra reservada "raise" incluyendo un mensaje de error
        if not (1 < n) or not (n < 1000000):
            raise ValueError("Error: Debe ingresar un número mayor que 1 y menor que 1000000")
        
    
    #Se captura las excepciones de tipo "ValueError" y se las almacena en la variable "e"
    #Se imprime en la consola la variable "e" que contiene la excepción
    except ValueError as e:    
        return
    
    secuencia_valores = [n] 

    while n != 1:
    #Se verifica si "n" es par utilizando el operador módulo que devuelve el resto de la división entre "n" y 2, y evaluando si es igual a 0. Si es par, se divide "n" por 2 y actualiza "n"
        if (n % 2) == 0:
            n //= 2
#Sino, quiere decir que "n" es impar. En ese caso se multiplica "n" por 3, se le suma 1 y actualiza "n"            
        else:
            n = n * 3 + 1
        secuencia_valores.append(n)

    return secuencia_valores


#Se realiza una aserción para verificar si la secuencia generada para el caso de prueba coincide con lo que se espera. Si esta falla, se imprime un mensaje de error
#Si no falla, se imprime un mensaje indicando que los casos de prueba han pasado correctamente
assert secuencia(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"  
assert secuencia(0) == None, "Error en el caso de prueba"
assert secuencia(1000000) == None, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")