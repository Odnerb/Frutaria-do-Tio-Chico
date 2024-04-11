# O algoritmo da Frutaria do Tio Chico, simula um vendedor na qual irá atender um cliente e 
# este vai verificar o número da fruta que o usuário digitar e verificar se ainda tem quantidade
# no estoque e ao encerrar a compra, ele diz o total da compra.


print('Seja bem-vindo!')

#  Procedimento - Serve para evitar ter que repertir o menu toda vez quando for chamado.
# Não possuí parâmetros de entrada e retorno.
def recepcao():
    print('====================================================')
    print('     F R U T A R I A   D O   T I O   C H I C O      ')
    print('====================================================')
    print('----------------------------------------------------')
    print('FRUTAS')
    print('[1] - Abacaxi ____________ R$ 15,00 (und)')
    print('[2] - Ameixa _____________ R$ 2,75 (und)')
    print('[3] - Banana Nanica ______ R$ 11,20 (6 und)')
    print('[4] - Banana Prata _______ R$ 12,50 (6 und)')
    print('[5] - Goiaba _____________ R$ 1,50 (und)')
    print('[6] - Kiwi _______________ R$ 2,65 (und)')
    print('[7] - Laranja ____________ R$ 1,65 (und)')
    print('[8] - Morango ____________ R$ 16,00 (25 und)')
    print('[9] - Maracujá ___________ R$ 6,50 (und)')
    print('[10] - Melancia __________ R$ 58,00 (und)')
    print('[11] - Melão _____________ R$ 12,00 (und)')
    print('[12] - Pessego ___________ R$ 3,00 (und)')
    print('[13] - Uva _______________ R$ 17,70 (75 und)')
    print('--------------------------------------------------\n')

carrinho = []
frutas = []
continuar = 'Sim'

# Ordem -> Produto, Quantidade, unitário/quantidade, Valor
abacaxi = ['Abacaxi', 20, 1, 15]
ameixa = ['Ameixa', 700, 1, 2.75]
banana_nanica = ['Banana-Nanica', 100, 6, 11.20]
banana_prata = ['Banana-Prata', 150, 6, 12.50]
goiaba = ['Goiaba', 300, 1, 1.50]
kiwi = ['Kiwi', 50, 1, 2.65]
laranja = ['Laranja', 500, 1, 1.65]
morango = ['Morango', 1000, 25, 16]
maracuja = ['Maracujá', 360, 1, 6.50]
melancia = ['Melancia', 15, 1, 58]
melao = ['Melão', 20, 1, 12]
pessego = ['Pêssego', 25, 1, 3]
uva = ['Uva', 1050, 75, 17.70]

# Abaixo, tentei inserir embaralhadas todas as frutas
# para depois utilizar a função agregada da lista .sort() para 
# ordenar... Mas não consegui, caso alguém tenha uma solução
# para isso, fique a vontade. Fiquei sabendo no stackoverflow
# que a linguagem não tem suporte para tal solução.

frutas.extend([
    abacaxi, ameixa, banana_nanica, banana_prata, goiaba, kiwi,
    laranja, morango, maracuja, melancia, melao, pessego, uva
])

# TypeError: '<' not supported between instances of 'dict' and 'dict'
# frutas.sort()

recepcao()

# Muitas das vezes, ao testar o código ou disponibilizá-lo para outros testarem quanto tem um estrutura de repetição, onde o
# argumento para continuar seja uma string pode ocorrer uma falta de atenção e digitando um valor inválido ou algum caractere
# em caixa alta ou a primeira letra em maiúsclo. Para evitar coloquei uma condição na variável continuar para receber diferentes
# strings relacionadas ao "sim".  
while continuar == 'SIM' or continuar == 'Sim' or continuar == 'sim' or continuar == 'S' or continuar == 's': 
    opcao = int(input('Escolha a opção: '))
    if opcao == 0:
        print(f'Desculpe por não ter o que deseja, estou aqui se precisar!')
        break
    else:
        quantidade = int(input('Quantas unidades: '))
        if opcao > 0 and opcao <= 13:
            print('---------------------------------------------')
            if frutas[opcao-1][1] >= quantidade:
                frutas[opcao-1][1] = frutas[opcao-1][1] - quantidade
                carrinho.append([frutas[opcao-1][0], quantidade, (quantidade / frutas[opcao-1][2]) * frutas[opcao-1][3]])
            elif frutas[opcao-1][1] > 0:
                print(f'Só tem {frutas[opcao-1][1]} unidades restantes...\n')
            elif frutas[opcao-1][1] < quantidade:
                print(f'Não temos essa quantidade desejada, olhe novamente o menu.\n')
            else:
                print('Sinto muito, mas o produto que deseja acabou!\n')
        else:
            print('Opção errada! Escolha o valor de acordo com as posições dos produtos no menu...\n')
            recepcao()
        continuar = input('Deseja algo mais meu nobre? [Sim/Não]\n')
        recepcao()

# Gera o comprovante
if len(carrinho) != 0:
    total_quantidade, total_valor = 0, 0
    print('--------------------------------------------------------')
    print(f'PRODUTO                 |    QUANTIDADE    |  VALOR    ')
    print('--------------------------------------------------------')
    # Itera sobre a lista e mostrando todos os produtos
    for produto in carrinho:
        print(f'{str(produto[0]).ljust(23)} | {str(produto[1]).center(16)} | R$ {produto[2]:.2f}  ')
        # As variáveis abaixo armazenam o total de produtos e o valor final que o usuário deve pagar
        total_quantidade += produto[1]
        total_valor += produto[2]
    print('--------------------------------------------------------')
    print(f'TOTAL                   | {str(total_quantidade).center(16)} | R$ {total_valor:.2f}    ')
    print('--------------------------------------------------------')
    print('Agradeço a preferência, volte sempre!!!')


