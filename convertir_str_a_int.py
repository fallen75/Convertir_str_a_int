numero_str = "-1956.3356"
caracteres_especiales = 0
contador = 1
dir("hola")


for caracter in numero_str:
    
    print(type(caracter))
    
    if caracter.isdigit():
        int(caracter)
        print(caracter)
        
    elif caracter == "." or caracter == "-":
        caracteres_especiales += 1

    else:
        print("Cadena no válida")
        break
        
    print(f'Finalizo la interaccion numero {contador}')
    contador += 1
    
print(caracteres_especiales)    




