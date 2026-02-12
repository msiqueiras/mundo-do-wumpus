import useful as useful 
import agent

useful.intro()
hero = agent.create_agent()

flow_game = True
while flow_game:
    try:
        agent.actual_status(hero)

        useful.action_menu()

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

