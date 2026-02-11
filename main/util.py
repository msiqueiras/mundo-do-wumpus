def action_menu():
    '''
    Função para mostrar o menu de ações do jogo. Conta com as ações de:
    movimentar-se pelo cenário, atirar flechas 
    '''

    actions = {'[1]':'Mover-se (N, S, L, O)',
               '[2]': 'Atirar flecha',
               '[3]': 'Pegar ouro',
               '[4]': 'Sair do jogo'}

    for key, value in actions.items():
        print(key, '..........', value)


