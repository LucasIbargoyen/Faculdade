import random #importado a biblioteca Randon qua fará o sorteamento das decisões no jogo

"""
ATUALIZAÇÃO 25/03 (Lucas): Arrumei alguns erros de identação do código e arrumei as estruturas sequenciais
que estavam bugando e deixando o código desnecessáriamente complexo, antes dentro dos laços haviam 2 estruturas sequenciais,
agora tá com apenas uma estrutura sequencial dentro de cada laço do while. Na parte da capivara menor a gente já pode pensar no 
combate, tava pensando em criar uma lista de d1 até d20 sendo d1 o ataque fraco e d20 o ataque forte, o código escolheria aleatoriamente
algum dessas 20 opções dentro da lista
"""

'''
ATUALIZAÇÃO 02/04 (Juliano): Fiz a segunda fase (somente a lógica, falta incluir os textos da fase 2). 
Também adicionei imagens de:
 - um guerreiro para a fase 1 e outro para a fase 2
 - uma Capivara mãe para a fase 1 e uma capivara filha para a fase 2
Obs: Falta incluir a história na fase 2, não tenho muita idéia para isto
'''
#--- Opções do Menu ---
print("\nBem vindo ao Jogo: Homem x Capivara!!!\n")
print("Pressione a tecla Q para sair ou a tecla I para iniciar")
menu = input().upper()  # Converte a entrada para maiúsculas para facilitar a comparação
while menu != "Q":
    if menu == "I":

# --- Código do Game ---
        print(
            'Depois de muito tempo vivendo sob domínio tirânico das capivaras que ganharam consciência,\n'
            'a resistência humana vive sob constante ameaça do exército capivara que ronda quase todos os lugares,\n'
            'esses rebeldes humanos vivem em bunkers subterrâneos espalhados por vários lugares, eles funcionam como um grande sistema metroviário,\n'
            'mas diferente de um metrô normal, são usados trens manuais, normalmente feito artesanalmente de restos de metais e materiais do gênero, \n'
            'a comida e água é escassa, requerendo cooperação entre as partes rebeldes para se manterem, os coletores, como são chamadas as pessoas que \n'
            'vão para a superfície são essênciais na sobrevivência rebelde, e você é um desses coletores, que foi pego por guardas capivaras enquanto buscava por\n'
            'suprimentos. Você acorda dentro de uma cela suja e com um cheiro forte de sangue, você não sabe de onde vem esse cheiro, mas ouve barulhos de\n'
            'batidas e algo se partindo, você percebe que as condições do portão que prende você são precárias e decide arrombar a fechadura com uns\n'
            'grampos que escondeu no seu calçado, após algumas tentativas, você consegue escapar, tem dois caminhos, direita e esquerda...\n'
        )

        while True:
            escolha_corredor = input('Para qual lado você vai?  ').lower()

            if escolha_corredor == 'direita':
                print(
                    '\nVocê vai pela direita passando pelas outras celas e não vê nada além de corpos em decomposição, no final a sua esquerda você vê uma entrada\n'
                    'ao espiar pela entrada você vê uma capivara grande, de uns 2 metros, usando um avental sujo de sangue e na mesa há pedaços de carne fresca,\n'
                    'como ela está de costas para você, você pode tentar se esgueirar por trás dela, mas claro que há uma chance de dar errado  ')
            elif escolha_corredor == 'esquerda':
                print(
                    '\nVocê decide ir para a esquerda e encontra uma porta de metal, infelizmente ela está trancada e é impossível de abrir usando grampos\n'
                    ' sua única opção é ir pela direita, você vai pela direita passando pelas outras celas e não vê nada além de corpos em decomposição, no final a sua esquerda você vê uma entrada\n'
                    'ao espiar pela entrada você vê uma capivara grande, de uns 2 metros, usando um avental sujo de sangue e na mesa há pedaços de carne fresca,\n'
                    'como ela está de costas para você, você pode tentar se esgueirar por trás dela, mas claro que há uma chance de dar errado  ')
            else:
                print('Opção inválida, apenas direita ou esquerda.')
                continue

            print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou...   ')

            while True:
                escolha_açougueiro = input('O que você decide fazer?   ').lower()
                if escolha_açougueiro == 'esgueirar':
                    luck = random.random()  # Gera um numero entre 0 e 1
                    if luck < 0.3:
                        print(
                            '\nVocê tenta se esgueirar, mas o açougueiro percebe e joga o cutelo em você acertando a sua cabeça te matando instântaneamente')
                        print(
                            '⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              \n'
                            '⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            \n'
                            '⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀         \n'
                            '⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀           \n'
                            '⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀            \n'
                            '⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⠠⣀⠱⠘⣧⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡈⠀⢄⢸⡄             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡀⠃⠘⠂⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⡈⢘⡇             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡑⠣⠰⠀⢁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣸⠁             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠂⡀⢨⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⣾⡄⠀⠀⠀⠀⣀⠐⠁⡴⠁⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡈⡀⢠⣧⣤⣀⣀⡀⢀⡀⠀⠀⢀⣼⣀⠉⡟⠀⢀⡀⠘⢓⣤⡞⠁⠀⠀          \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡁⢁⣸⡏⠀⠀⠀⠀⠁⠀⠉⠉⠁⠹⡟⢢⢱⠀⢸⣷⠶⠻⡇⠀⠀⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠈⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠁⠀⠻⣧⠀⠀⣹⠁⠀⠀⠀             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠚⠃⣰⣥⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠼⢙⡷⡻⠀⡼⠁⠀⠀⠀⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠿⡿⠕⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⠉⣹⣷⣟⣚⣁⡼⠁⠀⠀⠀⠀⠀           \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠁⠀⠀                          \n')
                        break
                    elif luck >= 0.3:
                        print(
                            '\nVocê consegue se esgueirar pelo açougueiro, abrindo a porta você encontra uma escada e decide subir, chegando no andar de cima\n'
                            'você percebe que está numa casa antiga no meio de uma cidade, está de noite e está tudo silencioso, você vê a porta da frente\n'
                            'e tenta abrir, mas está trancada, nisso você ouve passos vindo da direita, você se esconde debaixo de uma mesa e espera, e então \n'
                            'surge uma capivara menor, ela está desarmada e desatenta, parece estar procurando por algo, você pode imobilizar ela\n'
                            'com a sua panela...')
                    #vai para a fase 2....
                        print(
                            '████████████████████████████████████████████████████`▄▀▀███████████████████▓████\n'
                            '███████████▓█▌███████████████████████████████████████╙██▄▀██████████████████████\n'
                            '██████████████████████████████████████▀▀▄██████▄▄▄▄▀██▐███▄▀████████████████████\n'
                            '████████████████████████████████████▓▄███████████████▄"╙███▌╙████████████████▌██\n'
                            '██████████████████████████████████▀▄███████████████████ ╙███▄▀██████████████████\n'
                            '█████████████████████████████████▌▐████████████████████▌j▐███C▀█████████████████\n'
                            '█████████████████████████████████▌██████████████████████]▌▀███⌐█████████████████\n'
                            '█████████████████████████████████▌██▀███████████████████]█ ████▐████████████████\n'
                            '██████████████████████████████████▐███▀██▀▀███████╝▓█▐█▄╙██▐███~████████████████\n'
                            '█████████████████████████████████╙████▐████% ███╙m███▐██▌▐█.███▀└███████████████\n'
                            '████████████████████████████████▀▄▓████████▄▄█▄▄▄▄▄▄████]██\▄████m▀█████████████\n'
                            '█████████████████████████████████╙████████████████████▀█r█⌐╠████ ▄ █████████████\n'
                            '████████████████████████████████ ███████████████████████⌐█▌▄╙███⌐██ ████████████\n'
                            '████████████████████████████████ ███████████████████████\█▄▀ ▄▄██▄▌ ████████████\n'
                            '█████████████████████████████████Γ,█▀,▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀`▐▀█▐███████▐████████████\n'
                            '█████████████████████████████████ █j██████████████████████ ▌███▀▀▄▄█████████████\n'
                            '████████████████████████████████ ██▄▀█████████████████████ ██└██▀▀▌████████████\n'
                            '███████████████████████████████ █████▄▄▀▀▀████████████▀▀▀▀▄▄▀ ▀████▌▐███████████\n'
                            '██████████████████████████████"▄███████▀▓▀▄▄▐▄▄▄▌╓▐████▌]████"▄█▄▄▄█████████████\n')
                    
                    # Inicio da fase 2
                    print('texto apresentação nivel 2')
                    while True:
                        escolha_corredor = input('Para qual lado você vai? - Nivel 2 ').lower()

                        if escolha_corredor == 'direita':
                            print('Texto apresentação direita - Nivel 2 ')
                        elif escolha_corredor == 'esquerda':
                            print('Texto apresentação esquerda - Nivel 2')
                        else:
                            print('Opção inválida, apenas direita ou esquerda.')
                            continue

                        print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou... Nivel 2 ')

                        while True:
                            escolha_açougueiro = input('O que você decide fazer? Nivel 2').lower()
                            if escolha_açougueiro == 'esgueirar':
                                luck = random.random()  # Gera um numero entre 0 e 2
                                if luck < 0.8:
                                    print('\nTexto que morreu ao esgueirar - Nivel 2 ')
                                    print(
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                        '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')                                    
                                    break
                                elif luck >= 0.8:
                                    print('\nTexto que conseguiu esgueirar - Nivel 2 ')
                                    #vai para a fase 3 ou finaliza....
                                    print('vai para a fase 3 ou VOCÊ GANHOU!!!!')
                                    print(                                                                                
                                        '                     ╢▓█▓                                                       \n'
                                        ''     
                                        '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                        ''
                                        '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                        ''
                                        '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                        ''
                                        '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                        ''
                                        '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                        ''
                                        '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                        ''
                                        '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                        ''
                                        '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                        ''
                                        '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                        ''
                                        '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                        ''
                                        '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                        ''
                                        '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                        ''
                                        '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                        ''
                                        '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                        ''
                                        '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                        ''
                                        '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                        ''
                                        '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                        ''
                                        '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                        ''
                                        '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                        ''
                                        '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                        ''
                                        '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                        ''
                                        '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                        ''
                                        '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                        ''
                                        '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                        ''
                                        '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                        ''
                                        '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                    break
                                break
                            elif escolha_açougueiro == 'imobilizar':
                                luck = random.random()
                                if luck <= 0.7:
                                    print('\nTexto que morreu ao imobilizar - Nivel 2 ')  
                                    print(
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                        '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
                                    break
                                    
                                elif luck > 0.7:
                                    print('\nTexto que conseguiu imobilizar - Nivel 2 ')
                                    #vai para a fase 3 ou finaliza....
                                    print('vai para a fase 3 ou  VOCÊ GANHOU!!!!')
                                    print(                                                                                
                                        '                     ╢▓█▓                                                       \n'
                                        ''     
                                        '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                        ''
                                        '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                        ''
                                        '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                        ''
                                        '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                        ''
                                        '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                        ''
                                        '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                        ''
                                        '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                        ''
                                        '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                        ''
                                        '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                        ''
                                        '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                        ''
                                        '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                        ''
                                        '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                        ''
                                        '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                        ''
                                        '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                        ''
                                        '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                        ''
                                        '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                        ''
                                        '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                        ''
                                        '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                        ''
                                        '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                        ''
                                        '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                        ''
                                        '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                        ''
                                        '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                        ''
                                        '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                        ''
                                        '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                        ''
                                        '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                        ''
                                        '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                    break

                                break
                        break
                    break# Fase 1
    
                # FASE 1 IMOBILIZAR
                elif escolha_açougueiro == 'imobilizar':

                    luck = random.random()

                    if luck <= 0.7:
                            print(
                                '\nVocê tenta imobilizar o açougueiro mas ele é muito mais forte que você, jogando você no chão, pegando-lhe pelo pescoço e golpeando-lhe\n'
                                'na barriga, fazendo suas entranhas cair no chão enquanto você morre de dor e agonia')
                            print(
                                '⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              \n'
                                '⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            \n'
                                '⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀         \n'
                                '⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀           \n'
                                '⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀            \n'
                                '⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⠠⣀⠱⠘⣧⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡈⠀⢄⢸⡄             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡀⠃⠘⠂⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⡈⢘⡇             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡑⠣⠰⠀⢁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣸⠁             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠂⡀⢨⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⣾⡄⠀⠀⠀⠀⣀⠐⠁⡴⠁⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡈⡀⢠⣧⣤⣀⣀⡀⢀⡀⠀⠀⢀⣼⣀⠉⡟⠀⢀⡀⠘⢓⣤⡞⠁⠀⠀          \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡁⢁⣸⡏⠀⠀⠀⠀⠁⠀⠉⠉⠁⠹⡟⢢⢱⠀⢸⣷⠶⠻⡇⠀⠀⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠈⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠁⠀⠻⣧⠀⠀⣹⠁⠀⠀⠀             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠚⠃⣰⣥⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠼⢙⡷⡻⠀⡼⠁⠀⠀⠀⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠿⡿⠕⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⠉⣹⣷⣟⣚⣁⡼⠁⠀⠀⠀⠀⠀           \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠁⠀⠀                          \n')
                            break
                                  
                    elif luck > 0.7:
                        print(
                            '\nvocê conseguiu imobilizar o açougueiro, assim conseguindo pegar o seu cutelo, você percebe que esse cutelo é muito afiado e é\n'
                            'uma opção perfeita para se defender de inimigos, abrindo a porta ao lado você encontra uma escada e decide subir, chegando no andar de cima\n'
                            'você percebe que está numa casa antiga no meio de uma cidade, está de noite e está tudo silencioso, a iluminação é mais amena, ficando perfeito para se esconder no escuro, você vê a porta da frente\n'
                            'e tenta abrir, mas está trancada, nisso você ouve passos vindo da direita, você se esconde debaixo de uma mesa e espera, e então \n'
                            'surge uma capivara menor, ela está desarmada e desatenta, parece estar procurando por algo, você pode matar ela\n'
                            ' com o seu cutelo...')
                        #vai para a fase 2....
                        print('vai para a fase 2')
                        print(
                            '████████████████████████████████████████████████████`▄▀▀███████████████████▓████\n'
                            '███████████▓█▌███████████████████████████████████████╙██▄▀██████████████████████\n'
                            '██████████████████████████████████████▀▀▄██████▄▄▄▄▀██▐███▄▀████████████████████\n'
                            '████████████████████████████████████▓▄███████████████▄"╙███▌╙████████████████▌██\n'
                            '██████████████████████████████████▀▄███████████████████ ╙███▄▀██████████████████\n'
                            '█████████████████████████████████▌▐████████████████████▌j▐███C▀█████████████████\n'
                            '█████████████████████████████████▌██████████████████████]▌▀███⌐█████████████████\n'
                            '█████████████████████████████████▌██▀███████████████████]█ ████▐████████████████\n'
                            '██████████████████████████████████▐███▀██▀▀███████╝▓█▐█▄╙██▐███~████████████████\n'
                            '█████████████████████████████████╙████▐████% ███╙m███▐██▌▐█.███▀└███████████████\n'
                            '████████████████████████████████▀▄▓████████▄▄█▄▄▄▄▄▄████]██\▄████m▀█████████████\n'
                            '█████████████████████████████████╙████████████████████▀█r█⌐╠████ ▄ █████████████\n'
                            '████████████████████████████████ ███████████████████████⌐█▌▄╙███⌐██ ████████████\n'
                            '████████████████████████████████ ███████████████████████\█▄▀ ▄▄██▄▌ ████████████\n'
                            '█████████████████████████████████Γ,█▀,▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀`▐▀█▐███████▐████████████\n'
                            '█████████████████████████████████ █j██████████████████████ ▌███▀▀▄▄█████████████\n'
                            '████████████████████████████████ ██▄▀█████████████████████ ██└██▀▀▌████████████\n'
                            '███████████████████████████████ █████▄▄▀▀▀████████████▀▀▀▀▄▄▀ ▀████▌▐███████████\n'
                            '██████████████████████████████"▄███████▀▓▀▄▄▐▄▄▄▌╓▐████▌]████"▄█▄▄▄█████████████\n')

                        print('texto apresentação nivel 2')
                        while True:
                            escolha_corredor = input('Para qual lado você vai? - Nivel 2 ').lower()

                            if escolha_corredor == 'direita':
                                print('Texto apresentação direita - Nivel 2 ')
                            elif escolha_corredor == 'esquerda':
                                print('Texto apresentação esquerda - Nivel 2')
                            else:
                                print('Opção inválida, apenas direita ou esquerda.')
                                continue

                            print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou... Nivel 2 ')

                            while True:
                                escolha_açougueiro = input('O que você decide fazer? Nivel 2').lower()
                                if escolha_açougueiro == 'esgueirar':
                                    luck = random.random()  # Gera um numero entre 0 e 2
                                    if luck < 0.3:
                                        print('\nTexto que morreu ao esgueirar - Nivel 2 ')
                                        print(
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                        '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
                                        break
                                    elif luck >= 0.3:
                                        print('\nTexto que conseguiu esgueirar - Nivel 2 ')
                                    #vai para a fase 3 ou finaliza....
                                    print('vai para a fase 3 ou  VOCÊ GANHOU!!!!')
                                    print(                                                                                
                                        '                     ╢▓█▓                                                       \n'
                                        ''     
                                        '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                        ''
                                        '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                        ''
                                        '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                        ''
                                        '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                        ''
                                        '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                        ''
                                        '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                        ''
                                        '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                        ''
                                        '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                        ''
                                        '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                        ''
                                        '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                        ''
                                        '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                        ''
                                        '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                        ''
                                        '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                        ''
                                        '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                        ''
                                        '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                        ''
                                        '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                        ''
                                        '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                        ''
                                        '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                        ''
                                        '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                        ''
                                        '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                        ''
                                        '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                        ''
                                        '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                        ''
                                        '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                        ''
                                        '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                        ''
                                        '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                        ''
                                        '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                    break
                                elif escolha_açougueiro == 'imobilizar':
                                    luck = random.random()
                                    if luck <= 0.7:
                                        print('\nTexto que morreu ao imobilizar - Nivel 2 ') 
                                        print(
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                        '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
                                        break
                                        
                                    elif luck > 0.7:
                                        print('\nTexto que conseguiu imobilizar - Nivel 2 ')
                                        #vai para a fase 3 ou finaliza....
                                        print('vai para a fase 3 ou  VOCÊ GANHOU!!!!')
                                        print(                                                                                
                                        '                     ╢▓█▓                                                       \n'
                                        ''     
                                        '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                        ''
                                        '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                        ''
                                        '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                        ''
                                        '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                        ''
                                        '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                        ''
                                        '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                        ''
                                        '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                        ''
                                        '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                        ''
                                        '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                        ''
                                        '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                        ''
                                        '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                        ''
                                        '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                        ''
                                        '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                        ''
                                        '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                        ''
                                        '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                        ''
                                        '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                        ''
                                        '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                        ''
                                        '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                        ''
                                        '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                        ''
                                        '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                        ''
                                        '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                        ''
                                        '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                        ''
                                        '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                        ''
                                        '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                        ''
                                        '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                        ''
                                        '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                    break
                            break
                        break
            break

    print("\nPressione a tecla Q para sair ou a tecla I para iniciar")
    menu = input().upper()
    

print("Você saiu do jogo")
