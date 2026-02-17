import random


# Definição dos mapas (Com Wumpus e Sem Wumpus)
# Estrutura: {id: {'full': map, 'clean': map_clean}}

# Mapa 1
map1_full = [('V', 'B', 'P', 'B'),
             ('F', 'V', 'B', 'P'), 
             ('W', 'F', 'V', 'B'), 
             ('F', 'V', 'V', 'O')]

map1_clean = [('V', 'B', 'P', 'B'),
              ('V', 'V', 'B', 'P'), 
              ('V', 'V', 'V', 'B'), # Wumpus virou V, Fedores viraram V
              ('V', 'V', 'V', 'O')]

# Mapa 2
map2_full = [('V', 'F', 'W', 'F'),
             ('B', 'V', 'F', 'V'),
             ('P', 'B', 'V', 'V'),
             ('B', 'V', 'V', 'O')]

map2_clean = [('V', 'V', 'V', 'V'),
              ('B', 'V', 'V', 'V'),
              ('P', 'B', 'V', 'V'),
              ('B', 'V', 'V', 'O')]

# Mapa 3
map3_full = [('V', 'V', 'B', 'O'),
             ('V', 'B', 'P', 'B'),
             ('F', 'V', 'B', 'V'),
             ('W', 'F', 'V', 'V')]

map3_clean = [('V', 'V', 'B', 'O'),
              ('V', 'B', 'P', 'B'),
              ('V', 'V', 'B', 'V'),
              ('V', 'V', 'V', 'V')]

start_maps = {
    1: map1_full,
    2: map2_full,
    3: map3_full
}

clean_maps = {
    1: map1_clean,
    2: map2_clean,
    3: map3_clean
}

def create_world():
    '''
    Função para gerar aleatoriamente, dentro dos mapas possíveis, um mundo novo
    para o jogador
    Retorna uma tupla (world, map_id)
    '''
    
    map_id = random.choice(list(start_maps.keys()))
    world = start_maps[map_id]

    return world, map_id


def get_clean_map(map_id):
    '''
    Retorna a versão do mapa sem o Wumpus e sem fedor
    '''
    return clean_maps.get(map_id)


def create_wumpus():
    '''
    Função para criar o Wumpus
    '''
    wumpus = {'Life': 1}


def show_map(world, agent):
    print(26*'-', 'Mapa Atual', 26*'-')
    
    # Identificar células visitadas com base nas percepções
    # agent['perceptions'] contém [[linha, coluna], 'type']
    visited = [p[0] for p in agent['perceptions']]
    
    # Considera o ponto de partida (0,0)
    if [0, 0] not in visited:
        visited.append([0, 0])

    # Percorre as linhas (0 a 3)
    for i in range(len(world)):
        row_display = [] # Lista para guardar os simbolos desta linha
        
        # Percorre as colunas (0 a 3)
        for j in range(len(world[i])):
            
            # Verifica se o agente está nesta posição
            if agent['position'] == [i, j]:
                row_display.append('[ A ]') # A de Agente
            elif [i, j] in visited:
                # Mostra o conteúdo da célula se já foi explorada, formatado com colchetes e espaços
                if world[i][j] == 'O' and agent['gold']:
                    row_display.append('[ V ]')
                else:
                    row_display.append(f'[ {world[i][j]} ]') 
            else:
                # Mostra '?' se não foi explorado
                row_display.append('[ ? ]')

        # Imprime a linha inteira formatada
        print(''.join(row_display))
    print(65*'-')