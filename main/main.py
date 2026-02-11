import util 
import agent

print(25*'=', 'Mundo do Wumpus', 25*'=')

flow_game = True
while flow_game:
    try:
        agent = agent.create()
        util.action_menu()
        world = [('V', 'B', 'P', 'B'),
            ('F', 'V', 'B', 'V'), 
            ('W', 'F', 'V', 'B'), 
            ('F', 'V', 'B', 'O')]
        action = int(input('Digite o código da ação:'))

        if action == 4: #4 é opção de sair
            flow_game = False

        if action == 1: #1 é opção de movimento
            try:
                move = str(input('Direção [N, S, L, O]:')).strip().upper()[0]
            except ValueError:
                print('Código de direção inválido. Digite novamente')

    except ValueError:
        print('Código de ação inválido. Digite novamente')

