def create_world():
    '''
    Função para gerar aleatoriamente, dentro dos mapas possíveis, um mundo novo
    para o jogador
    '''

    world = [('V', 'B', 'P', 'B'),
            ('F', 'V', 'B', 'P'), 
            ('W', 'F', 'V', 'B'), 
            ('F', 'V', 'V', 'O')]

    return world


def create_wumpus():
    '''
    Função para criar o Wumpus
    '''

    wumpus = {'Life': 1}