print("Saludos querido cliente")
print("Bienvenido")
print("al supermecado")
print("EL SUPERMAKETOOON")

Arroz=10
Chocolate=8
Pastas=25
Carne=12
Pollo=15

print("Por favor Ingresar tu nombre")
nombre=input()
print("Por favor escribe tu apellido")
apellido=input()

nombre_completo=nombre+" "+apellido

print("Gracias por la información,",nombre_completo)

def mostrar_menu():
    print("Selecciona la opción que deseas")
    print("1: Conocer los productos en existencia")
    print("2: Comprar productos")
    print("3: Salir")

def mostrar_inventario():
    print("\nActualmente contamos con:\n")
    print("\nArroz:",Arroz,"\nChocolate:", Chocolate, "\nPastas:",Pastas,"\nCarne",Carne, "\nPollo",Pollo)
    

def comprar_productos():
    print("¿Que producto deseas comprar:")
    producto=input()
    print("¿Que cantidad deseas comprar:")
    cantidad_producto=int(input())
    print("Has comprado",cantidad_producto,"de",producto,)
    
    
    #codigo de domicilios fallido
    """
    print("¿Como deseas recibir tu compra:")
    
    print("Opción 1: solicitar domicilio")
    
    print("Opción 2:Recoger en tienda")
    
    confirmación_envio= input()
    
    if confirmación_envio== 1:
        print("Su pedido será enviado a esta dirección",direccion, "¿Es correcta la dirección dada? (Si) o (No):")
        input("Escriba (Si) o (No)")
    
    elif confirmación_envio==2:
        print("Usted puede recoger su pedido cuando desee")
    
    else:
        print("Ingrese una opción valida")
    
    direccion=input("Por favor indicanos la dirección:")
     """   
    
    
    """"
        elif confirmación_envio== 2: 
            print("Ingrese la dirección a la que ",direccion)
        else:
            print("Información solciitada incorrecta. Por favor ingrese un opción valida")
        break
    
    
    print("¿Cual es la dirección de envio?")
    dirección= input()
    print("¿Que producto deseas comprar:")
    producto=input()
    print("¿Que cantidad deseas comprar:")
    cantidad_producto=int(input())
    print("Has comprado",producto," ","con",cantidad_producto," ","unidad/unidades")
    print("¿Desea enviar su pedido a esta direccion (si) o (no)?")
    """

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    
    elif respuesta == 2:
        comprar_productos()
        
    elif respuesta == 3: 
        print("Acabaste")
        break
    else:
        print("Ingrese una opción valida")

print("Compra terminada")
