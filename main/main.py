import useful as useful 
import agent
import worldmap

useful.intro()
hero = agent.create_agent()
world, map_id = worldmap.create_world()

flow_game = True
while flow_game:
    try:
        print('\n')
            
        agent.current_status(hero)

        useful.action_menu()

        action = int(input('Digite o código da ação:'))

        worldmap.show_map(world, hero)

        if action == 4: #4 é opção de sair
            flow_game = False

        if action == 1: #1 é opção de movimento
            flow_move = True
            while flow_move:
                move = str(input('''nem
                        N               
Direção (N,S,O,L):    O     L
                        S
                ''')).strip().upper()[0]
                if move in ['N', 'S', 'L', 'O']:
                    flow_move = False
                    hero = agent.new_position(hero, move)
                    hero = agent.room_perception(hero, world)
                    if hero == False: #herói morto
                        flow_game = False
                    
                    elif hero['gold'] == True and hero['position'] == [0,0]:
                        print('\033[32mPARABÉNS !! Você conseguiu pegar o ouro e voltar a salvo!!\033[m')
                        flow_game = False
                        
                else:
                    print('Código de direção inválido. Digite novamente')

        elif action == 2: #2 é opção de atirar flecha
            flow_arrow = True
            while flow_arrow:
                direcao_flecha = str(input('''
                                   N               
Direção da flecha (N,S,O,L):    O     L
                                   S
                ''')).strip().upper()[0]
                if direcao_flecha in ['N', 'S', 'L', 'O']:
                    flow_arrow = False
                    wumpus_killed = agent.shoot_arrow(hero, world, direcao_flecha)
                    if wumpus_killed:
                         # Troca o mapa atual pelo mapa sem wumpus e sem fedor
                         world = worldmap.get_clean_map(map_id)
                else:
                    print('Código de direção inválido. Digite novamente')

        elif action == 3: #3 é opção de pegar ouro
            agent.pick_gold(hero, world)

    except ValueError:
        print('Código de ação inválido. Digite novamente')

