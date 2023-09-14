import random
import os

print('ESCONDE-ESCONDE')

def continuar_jogo():
    vazio = ''
    
    print('Tecle 1 para continuar ou 0 para encerrar:')
    print('1 --> CONTINUE')
    print('0 --> FECHAR')
    escolha = (input('ESCOLHA: '))
    
    if escolha == vazio:
        continuar_jogo()
    elif escolha == '1':
        acertar_coordenadas()
    elif escolha == '0':
        print('\nFIM DE JOGO!\n')
        quit()
    elif escolha != '0' or escolha != '1':
        os.system('cls')
        print('Opção inválida. Escolha apenas 0 ou 1.')
        continuar_jogo()
    else:
        os.system('cls')
        continuar_jogo()


def acertar_coordenadas():
    coords_possiveis = ('11','12','13','21','22','23','31','32','33')
    x = [11,12,13,21,22,23,31,32,33]
    numero_aleatorio = random.choice(x)
    vazio = ''
    
    linha_1 = ['🔲','🔲','🔲']
    linha_2 = ['🔲','🔲','🔲']
    linha_3 = ['🔲','🔲','🔲']
    mapa = [linha_1, linha_2, linha_3]

    print(numero_aleatorio) #TRAPAÇA
    
    coordenadas = input('''Entre com as coordenadas possíveis:
    11  12  13
    🔲  🔲  🔲
    21  22  23
    🔲  🔲  🔲
    31  32  33
    🔲  🔲  🔲\n\nCoordenada = ''')   
    
    
    if coordenadas == vazio or coordenadas != :
        os.system('cls')
        print('Opção inválida. Tente novamente.')
        acertar_coordenadas()
    else:    
        coordenadas = int(coordenadas)
           
    os.system('cls')
    
    # if coordenadas == vazio or coordenadas != conjunto_de_possibilidades_2:
    #     acertar_coordenadas()
    # if coordenadas == conjunto_de_possibilidades_2:
    #     linha = int(coordenadas[0])
    #     coluna = int(coordenadas[1])
    #     coordenada_int = [linha][coluna]
    #     if coordenada_int == numero_aleatorio:
    #         mapa[linha - 1][coluna - 1] = '😁'
    #         print(f'Uiiii!!! Me achou.\n')
    #         print(f'{linha_1}\n{linha_2}\n{linha_3}')
    #         continuar_jogo()
    #     else:
    #         acertar_coordenadas()  
    # else:
    #     acertar_coordenadas()
    
    if coordenadas == 11 and numero_aleatorio == 11:
        mapa[0][0] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
        
    elif coordenadas == 12 and numero_aleatorio == 12:
        mapa[0][1] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
        
    elif coordenadas == 13 and numero_aleatorio == 13:
        mapa[0][2] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
                
    elif coordenadas == 21 and numero_aleatorio == 21:
        mapa[1][0] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
                    
    elif coordenadas == 22 and numero_aleatorio == 22:
        mapa[1][1] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
                        
    elif coordenadas == 23 and numero_aleatorio == 23:
        mapa[1][2] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
                            
    elif coordenadas == 31 and numero_aleatorio == 31:
        mapa[2][0] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
                                
    elif coordenadas == 32 and numero_aleatorio == 32:
        mapa[2][1] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
                                            
    elif coordenadas == 33 and numero_aleatorio == 33:
        mapa[2][2] = '😁'
        print(f'Uiiii!!! Me achou.')
        print(f'  11    12    13\n{linha_1}\n  21    22    23\n{linha_2}\n  31    32    33\n{linha_3}\n')
    
    else:
        os.system('cls')
        print('Coordenada errada. Tente novamente.')
        acertar_coordenadas()
            
    continuar_jogo()

acertar_coordenadas()