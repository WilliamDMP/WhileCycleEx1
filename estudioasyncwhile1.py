#Primer ejercicio
'''Sumar valores de compras hasta que el usuario digite 0, en ese momento el programa finaliza, 
si las compras superan 1000 se aplica un descuento de 10%'''

sumacompra = 0
valor = float(input("Ingrese el valor de su compra: "))
while valor != 0:
    if valor < 0:
        print("Por favor ingrese su compra en numeros positivos")
    else:
        sumacompra = sumacompra + valor
    valor = float(input("Ingrese el valor de su compra: "))
if sumacompra > 1000:
    desc = sumacompra - (sumacompra*0.1)
    print(f'El valor total de su compra con descuento es de {desc}')
else:
    print(f'El valor de su compra es de {sumacompra}')
   
  
        