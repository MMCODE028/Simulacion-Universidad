
import random


# for i in range(0,5):
#     print(ListaBaloto[i])



# for i in range(0,5):
#     print(ListaUsuario[i])



Controlador = 0

while(Controlador<=10):

    print("I-->",Controlador)

    #Generamos los numeros aleatorios tanto de baloto como los de usuario    
    NumeroBaloto_1 = random.randint(1,43)
    NumeroBaloto_2 = random.randint(1,43)
    NumeroBaloto_3 = random.randint(1,43)
    NumeroBaloto_4 = random.randint(1,43)
    NumeroBaloto_5 = random.randint(1,43)

        
    NumeroUsuario_1 = random.randint(1,43)
    NumeroUsuario_2 = random.randint(1,43)
    NumeroUsuario_3 = random.randint(1,43)
    NumeroUsuario_4 = random.randint(1,43)
    NumeroUsuario_5 = random.randint(1,43)


    #Creamos las listas para guardar los numeros aleatorios
    ListaBaloto = []
    ListaUsuario = []

    


    #Agregamos los numeros aleatorios a la lista
        
    ListaBaloto.append(NumeroBaloto_1)
    ListaBaloto.append(NumeroBaloto_2)
    ListaBaloto.append(NumeroBaloto_3)
    ListaBaloto.append(NumeroBaloto_4)
    ListaBaloto.append(NumeroBaloto_5)

    
    ListaUsuario.append(NumeroBaloto_1)
    ListaUsuario.append(NumeroBaloto_2)
    ListaUsuario.append(NumeroBaloto_3)
    ListaUsuario.append(NumeroBaloto_4)
    ListaUsuario.append(NumeroBaloto_5)

    contador = 0
    for i in range(0,5):
        for j in range(0,5):
            if(ListaUsuario[i] == ListaBaloto[j]):
                print("Encontrado")
                contador = contador + 1

            

    print(contador)

    Controlador = Controlador + 1







