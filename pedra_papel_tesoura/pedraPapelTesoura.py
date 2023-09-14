import random

def pedraPapelTesoura():
    pedra = '''
         ______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

    '''

    papel = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    tesoura = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    
    vazio = ''
    computador = random.randint(0,2)
    h = 0
          
    print("Qual a sua escolha.\n0 para pedra\n1 para papel\n2 para tesoura\n")
    humano = input("0, 1 ou 2: ")
    print("\n")
    
    if humano == vazio:
        print("Opção inválida. Tente 0, 1 ou 2")
        pedraPapelTesoura()
    elif humano != '0' or humano != '1' or humano != '2':
        print("Opção inválida. Tente 0, 1 ou 2")
        pedraPapelTesoura()
    else:
        h = int(humano)
        c = computador

    if (h == 0 and c == 0):
        print(f"Escolha do computador:{pedra}\nSua escolha:{pedra}\nEMPATE")
    elif (h == 1 and c == 1):
        print(f"Escolha do computador:{papel}\nSua escolha:{papel}\nEMPATE")
    elif (h == 2 and c == 2):
        print(f"Escolha do computador:{tesoura}\nSua escolha:{tesoura}\nEMPATE")


    elif (h == 0 and c == 1):
        print(f"Escolha do computador:{papel}\nSua escolha:{pedra}\nVOCÊ PERDEU!")
    elif (h == 0 and c == 2):
        print(f"Escolha do computador:{tesoura}\nSua escolha:{pedra}\nVOCÊ VENCEU!")

    elif (h == 1 and c == 0):
        print(f"Escolha do computador:{pedra}\nSua escolha:{papel}\nVOCÊ VENCEU!")
    elif (h == 1 and c == 2):
        print(f"Escolha do computador:{tesoura}\nSua escolha:{papel}\nVOCÊ PERDEU!")

    elif (h == 2 and c == 0):
        print(f"Escolha do computador:{pedra}\nSua escolha:{tesoura}\nVOCÊ PERDEU!")
    elif (h == 2 and c == 1):
        print(f"Escolha do computador:{papel}\nSua escolha:{tesoura}\nVOCÊ VENCEU")
    else:
        print("Opção inválida. Tente 0, 1 ou 2")
        pedraPapelTesoura()

pedraPapelTesoura()