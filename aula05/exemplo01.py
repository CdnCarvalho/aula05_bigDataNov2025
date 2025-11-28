# # Área de acesso
# codigo = int(input('Digite o código: '))

# match codigo:
#     case 1:
#         print('Acesso Academia')
#     case 2:
#         print('Piscina')
#     case 3:
#         print('Vip')
#     case 4 | 5:
#         print('Estacionamento')
#     case 6 | 7 | 8:
#         print('Área Comum')
#     case 9:
#         print('Área Técnico')
#     case _:
#         print('Opção Inválida')



# # Área de acesso
# codigo = int(input('Digite o código: '))

# match codigo:
#     case 1:
#         print('Acesso Academia')
#     case 2:
#         print('Piscina')
#     case 3:
#         print('Vip')
#     case num if num == 4 or num == 5:
#         print('Estacionamento')
#     case num if 6 <= num <= 8:
#         print('Área Comum')
#     case 9:
#         print('Área Técnico')
#     case _:
#         print('Opção Inválida')


# Maior idade
idade = int(input('Idade: '))

if idade >= 0:
    match idade:
        case i if i < 12:
            print('Criança')
        case i if 12 <= i < 18:
            print('Adolescente')
        case i if i >= 18:
            print('Adulto')
        case _:
            print('Valor Inválido')