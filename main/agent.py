def create_agent():
    '''
    Função para criar um agente novo com todas os dados iniciais
    '''

    # adicionei um histórico de posições pq ele pediu no pdf

    agent = {'position': [0,0],
             'lives': 2,
             'arrow': 1,
             'gold': False,
             'perceptions': [],
             'history': []}
    
    return agent


def shoot_arrow(agent, world, direction):
    '''
    Função para atirar uma flecha na direção especificada
    :param agent: agente do jogo
    :param world: mapa do jogo
    :param direction: direção do tiro (N, S, O, L)
    :return: True se matou o Wumpus, False caso contrário
    '''
    
    if agent['arrow'] > 0:
        agent['arrow'] -= 1
        print('Você atirou uma flecha!')
        
        row, col = agent['position']
        target_pos = None
        
        if direction == 'N':
            target_pos = [row - 1, col]
        elif direction == 'S':
            target_pos = [row + 1, col]
        elif direction == 'L':
            target_pos = [row, col + 1]
        elif direction == 'O':
            target_pos = [row, col - 1]
            
        # Verificar limites do mapa (assumindo 4x4)
        if target_pos and 0 <= target_pos[0] < 4 and 0 <= target_pos[1] < 4:
            tr, tc = target_pos
            if world[tr][tc] == 'W':
                print('Você ouviu um grito terrível! O Wumpus foi morto!')
                return True
            else:
                print('A flecha atingiu a parede ou o chão, mas não houve grito.')
        else:
            print('A flecha atingiu a parede.')
            
    else:
        print('Você não tem mais flechas!')
        
    return False


def new_position(agent, direction):
    '''
    Função para alterar a posição do agente no mapa do jogo
    :param agent: agente criado pelo método create_agent()
    :param direction: direção que se deseja ir
    '''


    moved = False
    
    if direction == 'N':
        if agent['position'][0] == 0:
            print('Não é possível ir para o NORTE na posição atual. Você esbarrou em uma barreira para cima.')
        else:
            agent['position'][0] -= 1
            moved = True
    
    elif direction == 'S':
        if agent['position'][0] == 3:
            print('Não é possível ir para o SUL na posição atual. Você esbarrou em uma barreira para baixo.')
        else:
            agent['position'][0] += 1
            moved = True
    
    elif direction == 'O':
        if agent['position'][1] == 0:
            print('Não é possível ir para o OESTE na posição atual. Você esbarrou em uma barreira à esquerda')
        else:
            agent['position'][1] -= 1
            moved = True
    
    elif direction == 'L':
        if agent['position'][1] == 3:
            print('Não é possível ir para o LESTE na posição atual. Você esbarrou em uma barreira à direita')
        else:
            agent['position'][1] += 1
            moved = True

    if moved:
        agent['history'].append(tuple(agent['position']))

    return agent


def current_status(agent):
    '''
    Função para mostrar para o jogador os status do agente naquele momento    
    :param agent: agente criado pelo método create_agent()
    '''

    print(26*'-','Status agente', 26*'-')
    print(f"Posição: {agent['position']}")
    print(f"Vidas: {agent['lives']}")
    print(f"Flecha: {agent['arrow']}")
    if agent['gold'] == True:
        print("Ouro: Já pego")
    else:
        print('Ouro: Ainda não foi pego')
    
    print("Percepções:")
    if not agent['perceptions']:
        print("  Nenhuma")
    else:
        current_row, current_col = agent['position']
        for p in agent['perceptions']:
            perc_pos = p[0]
            perc_type = p[1]
            perc_row, perc_col = perc_pos
            
            # Calcular diferença relativa
            dr = perc_row - current_row
            dc = perc_col - current_col
            
            dirs = []
            if dr < 0: dirs.append("Norte")
            elif dr > 0: dirs.append("Sul")
            
            if dc < 0: dirs.append("Oeste")
            elif dc > 0: dirs.append("Leste")
            
            if not dirs:
                direction = "Aqui"
            else:
                direction = "-".join(dirs)

            print(f"  [{direction}] -> {perc_type}")


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

    elif world_cell == 'W':
        print('Você foi devorado pelo Wumpus!')
        new_perception = [[row, column], 'Wumpus']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)
        agent = lose_life(agent)
        
    elif world_cell == 'P':
        print('Você caiu em um POÇO.')
        new_perception = [[row, column], 'Poço']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)
        agent = lose_life(agent)
        try:
            if agent['lives'] != 0:
                print('Você retornou para a posição inicial (0,0)')
        except TypeError:
            pass

    elif world_cell == 'O':
        print('Percepção do ambiente: Brilho. \nHá ouro nesta sala!')
        new_perception = [[row, column], 'Brilho']
        if new_perception not in agent['perceptions']:
            agent['perceptions'].append(new_perception)

    return agent


def pick_gold(agent, world):
    '''
    Função para o agente pegar o ouro
    :param agent: agente do jogo
    :param world: mapa do jogo
    :return: True se pegou o ouro, False caso contrário
    '''
    row, col = agent['position']
    if world[row][col] == 'O':
        if not agent['gold']:
            agent['gold'] = True
            print('Você pegou o ouro!')
            return True
        else:
            print('Você já pegou o ouro!')
            return False
    else:
        print('Não há ouro aqui para pegar.')
        return False
    

def lose_life(agent):
    '''
    Função para retirar uma unidade de vida do agente
    :param agent: agente criado pelo método create_agent()
    '''

    agent['lives'] -= 1
    agent['position'] = [0,0]
    if agent['lives'] == 0:
        print('\033[31mVOCÊ PERDEU!! Talvez da próxima vez você tenha mais sorte.\033[m')
        return False #para parar o ciclo do jogo - break.
    
    return agent
