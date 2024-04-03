def espiral_numerico(fila, columna): 
    if fila > columna: 
        if fila % 2 == 0: #Se verifica si la fila es par
            total_fila = (fila**2 - columna + 1) #Se almacena en una variable el resultado de multiplicar la fila por si misma, restar la columna y sumarle 1
            return total_fila 
        else: 
            total_fila = ((fila-1)**2 + columna) #Se almacena en la variable el resultado de restar la fila menos 1, multiplicarla por si misma y sumar la columna
            return total_fila 
    else:
        if columna % 2 == 0: #Se verifica si la columna es par
            total_columna = ((columna-1)**2 + fila) #Se almacena en una variable el resultado de restar la columna menos 1, multiplicarla por si misma y sumarle la fila
            return total_columna 
        else:
            total_columna = (columna**2 - fila + 1) #Se almacena en la variable el resultado de multiplicar la columna por si misma, restarle la fila y sumarle 1
            return total_columna 
        

assert espiral_numerico(2, 2) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")

