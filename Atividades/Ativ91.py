from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
  print(f'{k} tirou {v} no dado')
  sleep(1)

ranking = sorted(jogo.items(), key=itemgetter[1], reverse=True)

print(20 * '-=')
print('  == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
  print(f'  {i}° Lugar - {v[0]} com {v[1]}')
  sleep(1)
