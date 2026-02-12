def intro():
    '''
    Função para mostrar a introdução ao jogo.
    '''

    print(25*'=', 'Mundo do Wumpus', 25*'=')
    print('Bem-vindo (ou não) ao mundo do Wumpus. Seu objetivo é simples:')
    print('Pegue o ouro com o menor número de passos pelo mapa possível')
    print('e retorne para o início. Porém, cuidado para não cair em um poço')
    print('ou ser capturado por Wumpus. Use sua percepção: brisas e fedores')
    print('indicam que poços e Wumpus estão em algum ambiente ao seu lado.')
    print('Boa sorte. Você vai precisar.')


def action_menu():
    '''
    Função para mostrar o menu de ações do jogo. Conta com as ações de:
    movimentar-se pelo cenário, atirar flechas 
    '''

    print(67*'=')
    actions = {'[1]':'Mover-se (N, S, L, O)',
               '[2]': 'Atirar flecha',
               '[3]': 'Pegar ouro',
               '[4]': 'Sair do jogo'}

    for key, value in actions.items():
        print(key, '..........', value)




