'''Ingresar numeros enteros por teclado e identificar cuantos de ellos son pares o impares, el programa finaliza al escribir 0 '''
numeros = int(input('Ingrese numeros enteros para saber cuales son pares e impares '))
numeropar = 0
numeroimpar = 0
while numeros > 0:
    if numeros%2==0:
        numeropar = numeropar+1
    else:
        numeroimpar = numeroimpar+1
    numeros = int(input('Ingrese numeros enteros para saber cuales son pares e impares '))
    
print(f'la cantidad de numeros pares es {numeropar} y la cantidad de numeros impares es {numeroimpar}')