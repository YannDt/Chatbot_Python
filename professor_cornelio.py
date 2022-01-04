#Função para somar
def soma(a, b):
    print('\nO resultado de', a, '+', b, 'é:', a + b, '\n')


#Função para subtrair
def subtracao(a, b):
    print('\nO resultado de', a, '-', b, 'é:', a - b, '\n')


#Função para dividir
def divisao(a, b):
    print('\nO resultado de', a, '/', b, 'é:', a / b, '\n')


#Função para multiplicar
def multiplicacao(a, b):
    print('\nO resultado de', a, '*', b, 'é:', a * b, '\n')


def processar_resposta(resposta, nome):
    if resposta == '1':
        a = float(input('\nDigite o primeiro valor:\n'))
        b = float(input('Digite o segundo valor:\n'))
        soma(a,b)  
    elif resposta == '2':
        a = float(input('\nDigite o primeiro valor:\n'))
        b = float(input('Digite o segundo valor:\n'))
        subtracao(a, b)
    elif resposta == '3':
        a = float(input('\nDigite o primeiro valor:\n'))
        b = float(input('Digite o segundo valor:\n'))
        divisao(a, b)
    elif resposta == '4':
        a = float(input('\nDigite o primeiro valor:\n'))
        b = float(input('Digite o segundo valor:\n'))
        multiplicacao(a, b)
    else:
        print('\nHmmm, não entendi. Digite apenas 1, 2, 3 ou 4\n')


def start():
    # Apresentar o chatbot
    print(
        'Olá! Sou o professor Cornélio e vou resolver algumas operações simples de matemática para você!'
    )
    # pedir o nome
    nome = input('\nQual o seu nome?\n')
    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'{os.linesep}{nome}, que tipo de operação você quer que eu realize?{os.linesep}{os.linesep}[1] - SOMA{os.linesep}[2] - SUBTRAÇÃO{os.linesep}[3] - DIVISÃO{os.linesep}[4] - MULTIPLICAÇÃO{os.linesep}'
        )
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()