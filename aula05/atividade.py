nota = float(input('Digite a nota: '))

if nota >= 8:
    print('APROVADO')
elif nota >= 5 or nota < 8:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')