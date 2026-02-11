def create():
    '''
    Função para criar um agente novo com todas os dados iniciais
    '''

    agent = {'position': [0,0],
             'lives': 3,
             'arrow': 1,
             'gold': False,
             'history': []}
    
    return agent

def new_position(agent, direction):
    '''
    Função para alterar a posição do agente no mapa do jogo
    :param agent: é o agente criado pelo método create()
    :param direction: é a direção que se deseja ir
    '''
    
    # limitações de 'cantos', não deixar o jogador sair do 4x4 por cima, por baixo,
    # pela esquerda ou pela direita

    if agent['position'][1] == 0 and direction == 'O': #não vaza pela esquerda
        print('Não é possível ir para a direção oeste na posição atual.')
    if agent['position'][1] == 3 and direction == 'L': #não vaza pela direita
        print('Não é possível ir para a direção leste posição atual.')
    if agent['position'][0] == 0 and direction == 'N': #não vaza por cima
        print('Não é possível ir para a direção leste na posição atual.')
    if agent['position'][0] == 3 and direction == 'S': #não vaza por baixo
        print('Não é possível ir para a direção leste na posição atual.')


    if direction == 'L':
        agent['position'][1] += 1

    if direction == 'O':
        agent['position'][1] -= 1

    if direction == 'S':
        agent['position'][0] += 1

    if direction == 'N':
        agent['position'][0] -= 1