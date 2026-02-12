def create_agent():
    '''
    Função para criar um agente novo com todas os dados iniciais
    '''

    agent = {'position': [0,0],
             'lives': 2,
             'arrow': 1,
             'gold': False,
             'perceptions': []}
    
    return agent


def new_position(agent, direction):
    '''
    Função para alterar a posição do agente no mapa do jogo
    :param agent: agente criado pelo método create_agent()
    :param direction: direção que se deseja ir
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
    :param agent: agente criado pelo método create_agent()
    '''

    agent_pt_br = {'Posição': agent['position'],
                 'Vidas': agent['lives'], 
                 'Flecha': agent['arrow'], 
                 'Ouro': agent['gold'], 
                 'Percepções': agent['perceptions']}
    print(26*'-','Status agente', 26*'-')
    for key, value in agent_pt_br.items():
        print(f'{key}: {value}')


def room_perception(agent, world):
    '''
    Função para associar as posições do agente com as percepções dadas pelo ambiente do mapa
    :param agent: agente criado pelo método create_agent
    :param world: mapa do mundo criado no módulo worldmap.py pelo método create_world()
    '''

    row = agent['position'][0]
    column = agent['position'][1]
    world_cell = world[row][column]
    new_perception = [0, 0]

    if world_cell == 'V':
        print('Percepção do ambiente: Vazio')
        new_perception = [[row, column], 'Vazio']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)
        
    elif world_cell == 'B':
        print('Percepção do ambiente: Brisa. \nHá algum poço por perto')
        new_perception = [[row, column], 'Brisa']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)
        
    elif world_cell == 'F':
        print('Percepção do ambiente: Fedor. \nWumpus está perto')
        new_perception = [[row, column], 'Fedor']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)
        
    elif world_cell == 'P':
        print('Você caiu em um POÇO.')
        new_perception = [[row, column], 'Poço']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)
        agent = lose_life(agent)

    return agent
    

def lose_life(agent):
    '''
    Função para retirar uma unidade de vida do agente
    :param agent: agente criado pelo método create_agent()
    '''

    agent['lives'] -= 1
    agent['position'] = [0,0]
    if agent['lives'] == 0:
        print('Você perdeu!')
        return False #para parar o ciclo do jogo - break.
    
    return agent
