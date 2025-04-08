def decimal_to_roman(numero):

    if not 1 <= numero <= 3999:
        raise ValueError("El número debe estar entre 1 y 3999")
    
    
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    

    resultado = ''
    
   
    for i in range(len(valores)):
        while numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i]
    
    return resultado