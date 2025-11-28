# Maior idade
idade = int(input('Idade: '))

match idade:
    case i if i < 12:
        print('Criança')
    case i if 12 <= i < 18:
        print('Adolescente')
    case i if i >= 18:
        print('Adulto')
    case _:
        print('Valor Inválido')