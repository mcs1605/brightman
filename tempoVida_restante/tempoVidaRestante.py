idade = input("What is your current age?")

horas_restante = (365 * 24 * 80) - (int(idade) * 365 * 24)
dias_restante = (80 * 365) - (int(idade) * 365)
semanas_restante = (80 * 52) - (int(idade) * 52)
meses_restante = (80 * 12) - (int(idade) * 12)
anos_restantes = (80 - int(idade))

print(f'Você tem {horas_restante} horas, {dias_restante} dias, {semanas_restante} semanas, {meses_restante} meses e {anos_restantes} anos restando.')