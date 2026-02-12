def create_agent():
    '''
    Função para criar um agente novo com todas os dados iniciais
    '''

    agent = {'position': [0,0],
             'lives': 3,
             'arrow': 1,
             'gold': False,
             'perceptions': []}
    
    return agent

def new_position(agent, direction):
    '''
    Função para alterar a posição do agente no mapa do jogo
    :param agent: é o agente criado pelo método create_agent()
    :param direction: é a direção que se deseja ir
    '''
    
    if direction == 'N':
        if agent['position'][0] == 0:
            print('Não é possível ir para o NORTE na posição atual. Você esbarrou em uma barreira para cima.')
        else:
            agent['position'][0] -= 1
    
    elif direction == 'S':
        if agent['position'][0] == 3:
            print('Não é possível ir para o SUL na posição atual. Você esbarrou em uma barreira para baixo.')
        else:
            agent['position'][0] += 1
    
    elif direction == 'O':
        if agent['position'][1] == 0:
            print('Não é possível ir para o OESTE na posição atual. Você esbarrou em uma barreira à esquerda')
        else:
            agent['position'][1] -= 1
    
    elif direction == 'L':
        if agent['position'][1] == 3:
            print('Não é possível ir para o LESTE na posição atual. Você esbarrou em uma barreira à direita')
        else:
            agent['position'][1] += 1

    return agent

def actual_status(agent):
    '''
    Função para mostrar para o jogador os status do agente naquele momento    
    :param agent: é o agente criado pelo método create_agent()
    '''

    agent_pt_br = {'Posição': agent['position'],
                 'Vidas': agent['lives'], 
                 'Flecha': agent['arrow'], 
                 'Ouro': agent['gold'], 
                 'Percepções': agent['perceptions']}
    print(26*'-','Status agente', 26*'-')
    for key, value in agent_pt_br.items():
        print(f'{key}: {value}')

