# Mundo do Wumpus - Projeto da disciplina de Prog1

## Breve contexto

"Mundo do Wumpus" é um jogo de raciocínio lógico, que muitas vezes é utilizado para explicação introdutória de agentes inteligentes na exploração de ambientes.No jogo, o agente precisa passear pelos ambientes com o objetivo de capturar uma recompensa (ouro) e retornar para a posição de início (0,0) com o menor número de passos possíveis, evitando cair em poços e/ou ser capturado pelo monstro Wumpus.
O ambiente fornece percepções para o agente, como fedores do Wumpus, brisas dos poços e brilho do ouro, em ambientes adjacentes àqueles que possuem o perigo ou a recompensa.

![Explicação visual do jogo](/images/wumpus2.svg)

## Organização do código

O código está estruturado segundo a seguinte organização de pastas:

```text
MUNDO-DO-WUMPUS/
├── images/                # Recursos visuais para relatório e readme
├── main/                 
│   ├── agent.py           # Funções da lógica do agente
│   ├── main.py            # Script principal
│   ├── useful.py          # Utilitários e menus
│   └── worldmap.py        # Funções da lógica do mapa
├── .gitignore
├── README.md
└── requirements.txt
