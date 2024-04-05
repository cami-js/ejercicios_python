def formar_palindromo(cadena):
    # Validar longitud de la cadena
    if not (1 < len(cadena) < 1000000):
        return "Longitud de cadena inválida"

    # Validar contenido de la cadena (letras minúsculas del alfabeto inglés)
    if not all(letra.islower() for letra in cadena):
        return "La cadena debe contener solo letras minúsculas del alfabeto inglés"

    # Contar la frecuencia de cada letra en la cadena
    frecuencia = {}
    for letra in cadena:
        frecuencia[letra] = frecuencia.get(letra, 0) + 1

    # Identificar las letras con frecuencia impar
    letras_impares = [letra for letra, freq in frecuencia.items() if freq % 2 != 0]

    # Si hay más de una letra impar, no es posible formar un palíndromo
    if len(letras_impares) > 1:
        return "NO SOLUTION"

    # Construir la mitad izquierda del palíndromo
    mitad_izquierda = ""
    for letra, freq in frecuencia.items():
        mitad_izquierda += letra * (freq // 2)

    # Construir la mitad derecha reflejando la mitad izquierda
    mitad_derecha = mitad_izquierda[::-1]

    # Agregar la letra central (si existe)
    letra_central = letras_impares[0] if letras_impares else ""

    # Concatenar la mitad izquierda, la letra central y la mitad derecha
    palindromo = mitad_izquierda + letra_central + mitad_derecha

    return palindromo

cadena = input("Ingrese una cadena de caracteres que tenga una longitud mayor que 1 y menor que 1000000: ")

# Formar el palíndromo y mostrar el resultado
resultado = formar_palindromo(cadena)
print(resultado)


assert formar_palindromo("aabbc") == "abcba", "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")

