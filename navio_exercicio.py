#//!pip install simple-colors

#from simple_colors import *


opcoes = [
{
    'cod': 1,
    'metodo': 'Dinamite',
    'valor': 200000
},
{
    'cod': 2,
    'metodo': 'Minhocas Radioativas',
    'valor': 2500000
},
{
    'cod': 3,
    'metodo': 'Retroescavadeira',
    'valor': 500000
},
{
    'cod': 4,
    'metodo': 'Empurradores',
    'valor': 1800000
},
{
    'cod': 5,
    'metodo': 'Imãs',
    'valor': 1000000
},
{
    'cod': 6,
    'metodo': 'Fiat Uno de Firma',
    'valor': 22000 + 6.662*10000
},
{
    'cod': 7,
    'metodo': 'peixinhos',
    'valor': 200000
},
{
    'cod': 8,
    'metodo': 'rebocadores',
    'valor': 2500000
},
{
    'cod': 9,
    'metodo': 'Noé',
    'valor': 0
},                 
]

sair = False
opcao = ''
nivel_de_areia = 150
verificacao = nivel_de_areia

while sair == False:
  print("***********Operação Suez***********")
  print("-Detectamos nos nossos sistemas que o navio atingiu um grande banco de areia em uma das margens, encalhando o navio. Você tem limite de 6,5mi.")
  print("O que deseja fazer? Opções:\n1-Usar dinamite para fazer o banco de areia ceder(R$100.000,00).\n2-Usar minhocas biologicamente modifcadas para comer a areia(R$2mi)\n3-Usar retroescavadeiras para mover a areia para outro lugar(R$20.000,00)\n")
  
  for i in opcoes:
    escolha = escolha
    if escolha == i['cod']:
       opcao = i
  escolha = int(input())     
  if escolha == 1:
    print('Muito bem! Você tomou a melhor decisão.', 'bold')
    sair = True          
    print("Detectamos nos nossos sistemas que existe um grande banco de areia com aproximadamente 150cm de profundidade, precisamos fazer com que ele chegue a 0.\nPrecisamos colocar as dinamites gradualmente para que não atinga o casco do barco. Quantas deseja usar?\n")   
    print(f'Nivel de areia restante: {nivel_de_areia}cm')
    while nivel_de_areia > 0:
      dinamite = int(input())
      if dinamite > 5:
        print("Você atingiu o casco do navio.")
        sair = False
        break
      else: 
        nivel_de_areia = nivel_de_areia - (dinamite*5)
        print(f'Nivel de areia restante: {nivel_de_areia}cm')
      if nivel_de_areia <= 0:
        print("Parabéns! Conseguimos tirar o banco de areia. Agora precisamos fazer com que ele volte a sua posição original para seguir caminho.")
        for i in opcoes:
          if escolha == i['cod']:
            opcao = i
            correto = False
            print("Qual será sua próxima decisão?\n\n4- Usar imãs gigantes.\n5- Usar empurradores.\n6- Amarrar um Fiat Uno Mile Fire 2002 Álcool de firma com escada de aluminio para tirar o navio do canal(R$11.200,00 + 6,550 por litro).")
            escolha = int(input())
            if escolha == 4:
              print(red('Ta assistindo muito velozes e furiosos.'))
              break
            if escolha == 5:
              print('Parabéns! Certamente você tomou a decisão correta.')
              correto = True
              break  
            if escolha == 6:
              correto = False
              print("Opção inviavel devido ao alto custo do Álcool e a dificuldade de encontrar um uno no deserto.")
              break
    while correto ==  True:
      for i in opcoes:
        if escolha == i['cod']:
           opcao = i
      print("-Conseguimos centralizar o navio. Agora precisamos fazer com que ele volte a navegar, decida o que vamos fazer agora.")
      print("\n7- 350 peixinhos dourados amarrados no navio.(R$10.000)\n8- Usar rebocadores para tracionar o navio, fazendo com que ele pegue no tranco.\n9- Aguardar o dilúvio.(120000 anos).\n")    
          
      escolha = int(input())
      if escolha == 7:
        print(red("Provavelmente você terá problemas com Ibama, aguarde o processo."))
        sair = False
        break