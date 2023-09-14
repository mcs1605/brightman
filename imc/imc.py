import os

print("##############################################################################")
print("############################## CÁLCULO DE IMC ################################")
print("##############################################################################")

def calcula_imc():

    print("------------------------------------------------------------------------------\n")
    opcao = str(input("""Você gostaria de calcular seu IMC?\n
    Digite 1 para SIM
    Digite 0 para encerrar o programa\n
    Opção escolhida: """))
    
    if opcao == '1':
        massa = float(input("\n\tEntre com sua massa (Kg): ").replace(",","."))
        altura = float(input("\tEntre com sua altura (m): ").replace(",","."))
        
        imc = massa / (altura ** 2)
        imc = round(imc)
        print("\n\tRESULTADO: ", end ="")
        
        if imc <= 18.5:
            print(f"IMC = {imc} --> Magreza")
        elif imc < 25:
            print(f"IMC = {imc} --> Peso normal")
        elif imc < 30:
            print(f"IMC = {imc} --> Sobrepeso")
        elif imc < 35:
            print(f"IMC = {imc} --> Obesidade grau I")
        elif imc < 40:
            print(f"IMC = {imc} --> Obesidade grau II")
        else:
            print(f"IMC = {imc} --> Obesidade grau III")
        calcula_imc()
    
    elif not opcao == '0':
        print("Tente novamente. As opções são apenas 0 ou 1.")
        calcula_imc()

    else:
        opcao == 0
        print("Fim do programa!")
     
calcula_imc()

os.system('pause')