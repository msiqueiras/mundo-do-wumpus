import util 
import agent

print(25*'=', 'Mundo do Wumpus', 25*'=')
print('Características iniciais do herói:')
print('Posição: (0,0) \nVidas: 3 \nFlechas: 1 \nSem ouro \nSem histórico')        
print(67*'=')

flow_game = True
while flow_game:
    try:
        hero = agent.create()

        util.action_menu()

        action = int(input('Digite o código da ação:'))

        if action == 4: #4 é opção de sair
            flow_game = False

        if action == 1: #1 é opção de movimento
            flow_move = True
            while flow_move:
                move = str(input('Direção [N, S, L, O]:')).strip().upper()[0]
                if move in ['N', 'S', 'L', 'O']:
                    flow_move = False
                    hero = agent.new_position(hero, move)
                else:
                    print('Código de direção inválido. Digite novamente')

    except ValueError:
        print('Código de ação inválido. Digite novamente')

